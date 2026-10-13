// Sourced from sandbox/data-engine.js for root web serving
/**
 * DRAM Foundation VN - Modular Graph Data Engine
 * Pure modular JSON loader, Kahn's DAG cycle validator, and PR exporter.
 * Integrated with FastAPI Local Bridge Server (/api/status, /api/graph, /api/modules, /api/council/*).
 * (No localStorage persistence - Modular JSON files are the Single Source of Truth).
 */

export const DISCIPLINE_METADATA = {
  module_mcu_cots: {
    code: 'MCU-01',
    discipline: 'Electronics & Drive',
    icon: '⚙️',
    col: 0,
    row: 0
  },
  module_litho_stage_gen1: {
    code: 'LITHO-02',
    discipline: 'Lithography Stage',
    icon: '📐',
    col: 1,
    row: 0
  },
  module_optical_aligner_gen2: {
    code: 'OPTICS-03',
    discipline: 'Optics Aligner',
    icon: '🔬',
    col: 2,
    row: 0
  },
  module_wet_chemistry_gen1: {
    code: 'CHEM-04',
    discipline: 'Wet Chemistry Bench',
    icon: '🧪',
    col: 0,
    row: 1
  },
  module_thermal_oxidation_gen1: {
    code: 'FURN-05',
    discipline: 'Thermal Oxidation Furnace',
    icon: '🔥',
    col: 1,
    row: 1
  },
  module_dram_cell_gen2: {
    code: 'DRAM-06',
    discipline: '180nm DRAM Cell Architecture',
    icon: '💾',
    col: 2,
    row: 1
  },
  module_dram_root: {
    code: 'ROOT-00',
    discipline: '180nm DRAM Master Architecture',
    icon: '🏆',
    col: 3,
    row: 1
  }
};

export class DRAMDataEngine {
  constructor() {
    this.manifestUrl = './data/manifest.json';
    this.modules = [];
  }

  /**
   * Load graph with nested parent group nodes and child nodes across 6 disciplines.
   * Directly wires to live FastAPI bridge endpoints (/api/modules & /api/graph),
   * with seamless offline fallback to static JSON files.
   */
  async loadGraph() {
    console.log('[DataEngine] Initializing 6-Discipline Modular Graph...');
    let rawModules = [];
    let fromLiveApi = false;

    // 1. Attempt live query to FastAPI /api/modules
    try {
      const res = await fetch('/api/modules');
      if (res.ok) {
        const data = await res.json();
        if (Array.isArray(data) && data.length > 0) {
          rawModules = data.map(item => ({
            info: item.info,
            data: item.data
          }));
          fromLiveApi = true;
          console.log('[DataEngine] Successfully connected to live FastAPI /api/modules');
        }
      }
    } catch (err) {
      console.warn('[DataEngine] /api/modules unreachable, falling back to static manifest');
    }

    // 2. Fallback to static manifest if live server is unavailable
    if (rawModules.length === 0) {
      const manifestRes = await fetch(this.manifestUrl);
      if (!manifestRes.ok) {
        throw new Error(`Failed to load manifest: ${manifestRes.statusText}`);
      }
      const manifest = await manifestRes.json();
      const manifestModules = manifest.modules || [];

      const modulePromises = manifestModules.map(async (mod) => {
        const relPath = mod.file.startsWith('/') ? '.' + mod.file : `./${mod.file}`;
        const res = await fetch(relPath);
        if (!res.ok) {
          throw new Error(`Failed to load module ${mod.file}`);
        }
        const modData = await res.json();
        return { info: mod, data: modData };
      });

      rawModules = await Promise.all(modulePromises);
      console.log('[DataEngine] Loaded modules from static files');
    }

    this.modules = rawModules.map(m => m.info || {
      id: m.data.module_id,
      name: m.data.title,
      generation: m.data.generation,
      node_count: m.data.nodes?.length || 0
    });

    // 3. Verify /api/graph live connection
    try {
      const graphRes = await fetch('/api/graph');
      if (graphRes.ok) {
        const fullGraph = await graphRes.json();
        console.log(`[DataEngine] Live /api/graph confirmed: ${fullGraph.nodes?.length} nodes, ${fullGraph.edges?.length} edges`);
      }
    } catch (e) {
      // Offline fallback silent
    }

    // 4. Precompute node module map for intelligent edge port assignment
    const nodeModuleMap = new Map();
    rawModules.forEach((modWrap, modIdx) => {
      const mod = modWrap.data;
      const modInfo = modWrap.info || {};
      const modId = mod.module_id || modInfo.id;
      const meta = DISCIPLINE_METADATA[modId] || {
        col: modIdx % 4,
        row: Math.floor(modIdx / 4)
      };
      if (mod.nodes) {
        mod.nodes.forEach(n => {
          nodeModuleMap.set(n.id, {
            moduleId: modId,
            col: meta.col,
            row: meta.row
          });
        });
      }
    });

    // 5. Construct Nested Groups and Child Nodes via Left-to-Right Reingold-Tilford Tree Layout
    const COL_WIDTH = 380;
    const ROW_HEIGHT = 180;
    const PADDING_LEFT = 40;
    const PADDING_TOP = 80;

    // Step A: Calculate tree layout within each module
    const moduleLayouts = rawModules.map((modWrap, modIdx) => {
      const mod = modWrap.data;
      const modInfo = modWrap.info || {};
      const modId = mod.module_id || modInfo.id;
      const meta = DISCIPLINE_METADATA[modId] || {
        code: `DISC-0${modIdx + 1}`,
        discipline: mod.title || modInfo.name,
        icon: '🔬',
        col: modIdx % 4,
        row: Math.floor(modIdx / 4)
      };

      const nodes = mod.nodes || [];
      const nodeMap = new Map();
      const childrenMap = new Map();
      const parentMap = new Map();

      nodes.forEach(n => {
        nodeMap.set(n.id, n);
        childrenMap.set(n.id, []);
      });

      nodes.forEach(n => {
        if (n.parent_id && nodeMap.has(n.parent_id)) {
          childrenMap.get(n.parent_id).push(n.id);
          parentMap.set(n.id, n.parent_id);
        }
      });

      // Module roots are nodes with no parent inside this module
      const moduleRoots = nodes.filter(n => !parentMap.has(n.id));

      let leafCounter = 0;
      let maxDepth = 0;
      const nodePositions = new Map();

      function layoutSubtree(nodeId, depth = 0) {
        if (depth > maxDepth) maxDepth = depth;
        const children = childrenMap.get(nodeId) || [];
        const x = PADDING_LEFT + depth * COL_WIDTH;

        if (children.length === 0) {
          const y = PADDING_TOP + leafCounter * ROW_HEIGHT;
          leafCounter++;
          nodePositions.set(nodeId, { x, y, depth });
          return y;
        } else {
          const childYs = children.map(cid => layoutSubtree(cid, depth + 1));
          const y = (childYs[0] + childYs[childYs.length - 1]) / 2;
          nodePositions.set(nodeId, { x, y, depth });
          return y;
        }
      }

      moduleRoots.forEach(r => {
        layoutSubtree(r.id, 0);
        leafCounter += 0.4; // spacing between separate trees in same discipline
      });

      // In case of disconnected/orphan nodes
      nodes.forEach(n => {
        if (!nodePositions.has(n.id)) {
          layoutSubtree(n.id, 0);
        }
      });

      const maxY = Math.max(...Array.from(nodePositions.values()).map(p => p.y), 100);
      const groupWidth = Math.max(480, PADDING_LEFT * 2 + (maxDepth + 1) * COL_WIDTH);
      const groupHeight = Math.max(280, Math.round(maxY + 220));

      return {
        modWrap,
        mod,
        modInfo,
        modId,
        meta,
        nodes,
        nodePositions,
        groupWidth,
        groupHeight,
        groupX: 0,
        groupY: 0
      };
    });

    // Step B: Calculate non-overlapping Canvas positions for Discipline Groups
    const colWidths = new Map();
    moduleLayouts.forEach(ml => {
      const col = ml.meta.col;
      const cur = colWidths.get(col) || 0;
      if (ml.groupWidth > cur) colWidths.set(col, ml.groupWidth);
    });

    const colXMap = new Map();
    let curX = 60;
    const sortedCols = Array.from(new Set(moduleLayouts.map(ml => ml.meta.col))).sort((a, b) => a - b);
    sortedCols.forEach(col => {
      colXMap.set(col, curX);
      curX += (colWidths.get(col) || 480) + 120;
    });

    const colYMap = new Map();
    // Sort modules by row within their column
    moduleLayouts.sort((a, b) => (a.meta.col - b.meta.col) || (a.meta.row - b.meta.row));
    moduleLayouts.forEach(ml => {
      const col = ml.meta.col;
      const startY = colYMap.get(col) || 60;
      ml.groupX = colXMap.get(col) || 60;
      ml.groupY = startY;
      colYMap.set(col, startY + ml.groupHeight + 100);
    });

    // Step C: Build Group Nodes, Child Nodes, and Node Canvas Position Lookup
    const groupNodes = [];
    const childNodes = [];
    const nodeCanvasPosMap = new Map();

    moduleLayouts.forEach(ml => {
      groupNodes.push({
        id: `group-${ml.modId}`,
        type: 'disciplineGroup',
        position: { x: ml.groupX, y: ml.groupY },
        style: {
          width: ml.groupWidth,
          height: ml.groupHeight,
          zIndex: 0
        },
        data: {
          id: ml.modId,
          title: ml.mod.title || ml.modInfo.name,
          generation: ml.mod.generation || ml.modInfo.generation,
          file: ml.modInfo.file || '',
          nodeCount: ml.nodes.length,
          disciplineCode: ml.meta.code,
          discipline: ml.meta.discipline,
          icon: ml.meta.icon
        }
      });

      ml.nodes.forEach(n => {
        const pos = ml.nodePositions.get(n.id) || { x: 40, y: 80, depth: 0 };
        const localX = Math.round(pos.x);
        const localY = Math.round(pos.y);
        const absX = ml.groupX + localX;
        const absY = ml.groupY + localY;

        nodeCanvasPosMap.set(n.id, {
          absX,
          absY,
          localX,
          localY,
          moduleId: ml.modId,
          depth: pos.depth
        });

        childNodes.push({
          id: n.id,
          type: 'semiconductorNode',
          parentNode: `group-${ml.modId}`,
          extent: 'parent',
          position: { x: localX, y: localY },
          data: {
            ...n,
            depth: pos.depth,
            moduleId: ml.modId,
            parentGroupId: `group-${ml.modId}`,
            discipline: ml.meta.discipline,
            primaryMetric: n.primary_metric || (n.metrics_target ? Object.values(n.metrics_target)[0] : 'N/A')
          }
        });
      });
    });

    // Step D: Route Edges Intelligently based on Actual 2D Geometry
    let allEdges = [];
    moduleLayouts.forEach(ml => {
      if (ml.mod.edges) {
        const mappedEdges = ml.mod.edges.map(e => {
          const isUpgrade = e.relationship_type === 'upgrade_path';
          const strokeColor = isUpgrade ? '#a855f7' : '#3b82f6';

          const srcPos = nodeCanvasPosMap.get(e.source);
          const tgtPos = nodeCanvasPosMap.get(e.target);

          let sourceHandle = 'source-right';
          let targetHandle = 'target-left';

          if (srcPos && tgtPos) {
            const dx = tgtPos.absX - srcPos.absX;
            const dy = tgtPos.absY - srcPos.absY;

            if (Math.abs(dx) >= Math.abs(dy)) {
              if (dx >= 0) {
                sourceHandle = 'source-right';
                targetHandle = 'target-left';
              } else {
                sourceHandle = 'source-left';
                targetHandle = 'target-right';
              }
            } else {
              if (dy >= 0) {
                sourceHandle = 'source-bottom';
                targetHandle = 'target-top';
              } else {
                sourceHandle = 'source-top';
                targetHandle = 'target-bottom';
              }
            }
          }

          return {
            id: e.id,
            source: e.source,
            target: e.target,
            sourceHandle,
            targetHandle,
            type: 'smoothstep',
            label: e.label || e.relationship_type,
            animated: isUpgrade || e.relationship_type === 'prerequisite',
            markerEnd: {
              type: 'arrowclosed',
              width: 14,
              height: 14,
              color: strokeColor
            },
            style: {
              stroke: strokeColor,
              strokeWidth: 2
            },
            zIndex: 5
          };
        });
        allEdges.push(...mappedEdges);
      }
    });

    // Parent group nodes MUST appear before child nodes in the React Flow array
    const allNodes = [...groupNodes, ...childNodes];

    // Validate DAG acyclic property using Kahn's algorithm
    const validation = this.validateDAG(allNodes, allEdges);
    if (!validation.isValid) {
      console.error('[DataEngine] Cycle detected in DAG!', validation);
    }

    return {
      nodes: allNodes,
      edges: allEdges,
      source: fromLiveApi ? 'fastapi_live_bridge' : 'modular_json_ssot',
      modules: this.modules,
      validation
    };
  }

  /**
   * Load clean, high-speed WBS dataset with precomputed O(1) graph adjacency maps.
   * Eliminates Reingold-Tilford 2D layout calculation for blazing-fast table/neighborhood navigation.
   */
  async loadWBS() {
    console.log('[DataEngine] Loading high-speed WBS dataset...');
    let rawModules = [];
    let fromLiveApi = false;

    try {
      const res = await fetch('/api/modules');
      if (res.ok) {
        const data = await res.json();
        if (Array.isArray(data) && data.length > 0) {
          rawModules = data.map(item => ({
            info: item.info,
            data: item.data
          }));
          fromLiveApi = true;
        }
      }
    } catch (err) {
      console.warn('[DataEngine] /api/modules unreachable, falling back to static manifest');
    }

    if (rawModules.length === 0) {
      const manifestRes = await fetch(this.manifestUrl);
      if (!manifestRes.ok) throw new Error(`Failed to load manifest: ${manifestRes.statusText}`);
      const manifest = await manifestRes.json();
      const modulePromises = (manifest.modules || []).map(async (mod) => {
        const relPath = mod.file.startsWith('/') ? '.' + mod.file : `./${mod.file}`;
        const res = await fetch(relPath);
        if (!res.ok) throw new Error(`Failed to load module ${mod.file}`);
        const modData = await res.json();
        return { info: mod, data: modData };
      });
      rawModules = await Promise.all(modulePromises);
    }

    this.modules = rawModules.map(m => m.info || {
      id: m.data.module_id,
      name: m.data.title,
      generation: m.data.generation,
      node_count: m.data.nodes?.length || 0
    });

    const allNodes = [];
    const allEdges = [];
    const nodeMap = new Map();
    const incomingMap = new Map(); // nodeId -> [incoming edge infos]
    const outgoingMap = new Map(); // nodeId -> [outgoing edge infos]

    rawModules.forEach((modWrap, modIdx) => {
      const mod = modWrap.data;
      const modInfo = modWrap.info || {};
      const modId = mod.module_id || modInfo.id;
      const meta = DISCIPLINE_METADATA[modId] || {
        code: `DISC-0${modIdx + 1}`,
        discipline: mod.title || modInfo.name,
        icon: '🔬'
      };

      if (mod.nodes) {
        mod.nodes.forEach(n => {
          const enrichedNode = {
            ...n,
            moduleId: modId,
            discipline: meta.discipline || mod.title || modInfo.name,
            disciplineCode: meta.code,
            disciplineIcon: meta.icon,
            primaryMetric: n.primary_metric || (n.metrics_target ? Object.values(n.metrics_target)[0] : 'N/A')
          };
          allNodes.push(enrichedNode);
          nodeMap.set(n.id, enrichedNode);
          incomingMap.set(n.id, []);
          outgoingMap.set(n.id, []);
        });
      }

      if (mod.edges) {
        mod.edges.forEach(e => {
          allEdges.push({
            ...e,
            moduleId: modId
          });
        });
      }
    });

    // Wire adjacency maps
    allEdges.forEach(e => {
      if (outgoingMap.has(e.source)) {
        outgoingMap.get(e.source).push({
          edge: e,
          targetId: e.target,
          targetNode: nodeMap.get(e.target)
        });
      }
      if (incomingMap.has(e.target)) {
        incomingMap.get(e.target).push({
          edge: e,
          sourceId: e.source,
          sourceNode: nodeMap.get(e.source)
        });
      }
    });

    const validation = this.validateDAG(allNodes, allEdges);

    return {
      nodes: allNodes,
      edges: allEdges,
      modules: this.modules,
      nodeMap,
      incomingMap,
      outgoingMap,
      validation,
      source: fromLiveApi ? 'fastapi_live_bridge' : 'modular_json_ssot'
    };
  }

  /**
   * Kahn's Algorithm for Topological Sort & Cycle Detection in DAG.
   * Validates genuine leaf work package nodes.
   */
  validateDAG(nodes, edges) {
    const leafNodes = nodes.filter(n => n.type !== 'disciplineGroup');
    const inDegree = new Map();
    const adjList = new Map();

    leafNodes.forEach(n => {
      inDegree.set(n.id, 0);
      adjList.set(n.id, []);
    });

    edges.forEach(e => {
      if (adjList.has(e.source) && inDegree.has(e.target)) {
        adjList.get(e.source).push(e.target);
        inDegree.set(e.target, inDegree.get(e.target) + 1);
      }
    });

    const queue = [];
    inDegree.forEach((deg, id) => {
      if (deg === 0) queue.push(id);
    });

    let visitedCount = 0;
    while (queue.length > 0) {
      const curr = queue.shift();
      visitedCount++;

      const neighbors = adjList.get(curr) || [];
      neighbors.forEach(neighbor => {
        inDegree.set(neighbor, inDegree.get(neighbor) - 1);
        if (inDegree.get(neighbor) === 0) {
          queue.push(neighbor);
        }
      });
    }

    const isValid = visitedCount === leafNodes.length;
    return {
      isValid,
      cycleDetected: !isValid,
      visitedCount,
      totalCount: leafNodes.length
    };
  }

  /**
   * Convene AI Council via FastAPI Bridge Server (POST /api/council/review)
   */
  async reviewCandidateNode(candidate) {
    const res = await fetch('/api/council/review', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(candidate)
    });
    if (!res.ok) {
      const err = await res.json().catch(() => ({ detail: res.statusText }));
      throw new Error(err.detail || 'Council review failed');
    }
    return await res.json();
  }

  /**
   * Commit approved node to module JSON on disk via FastAPI Bridge Server (POST /api/council/commit)
   */
  async commitApprovedNode(node, proposedEdges, targetModule) {
    const res = await fetch('/api/council/commit', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        node,
        proposed_edges: proposedEdges,
        target_module: targetModule
      })
    });
    if (!res.ok) {
      const err = await res.json().catch(() => ({ detail: res.statusText }));
      throw new Error(err.detail || 'Council commit failed');
    }
    return await res.json();
  }

  /**
   * Get system status from FastAPI backend (GET /api/status)
   */
  async getStatus() {
    try {
      const res = await fetch('/api/status');
      if (res.ok) return await res.json();
    } catch (e) {
      console.warn('[DataEngine] Backend API offline, running in static standalone mode');
    }
    return null;
  }

  /**
   * Export a modular JSON package ready for GitHub PR submission.
   */
  exportModule(nodes, edges, moduleId) {
    const leafNodes = nodes.filter(n => n.type !== 'disciplineGroup');
    const moduleNodes = leafNodes
      .filter(n => n.data.moduleId === moduleId || !moduleId || moduleId === 'all')
      .map(n => ({
        id: n.id,
        label: n.data.label,
        generation: n.data.generation,
        action_type: n.data.action_type || n.data.actionType,
        status: n.data.status,
        category: n.data.category,
        estimated_hours: n.data.estimated_hours || n.data.estimatedHours || 40,
        primary_metric: n.data.primaryMetric,
        metrics_target: n.data.metrics_target || n.data.metrics,
        sop_content: n.data.sop_content || n.data.sopContent,
        citations: n.data.citations || [],
        proof_of_work: n.data.proof_of_work || n.data.proofOfWork
      }));

    const nodeIds = new Set(moduleNodes.map(n => n.id));
    const moduleEdges = edges
      .filter(e => nodeIds.has(e.source) || nodeIds.has(e.target))
      .map(e => ({
        id: e.id,
        source: e.source,
        target: e.target,
        relationship_type: e.style?.stroke === '#8b5cf6' ? 'upgrade_path' : 'prerequisite',
        label: e.label
      }));

    const exportPayload = {
      module_id: moduleId || 'custom_export',
      exported_at: new Date().toISOString(),
      nodes: moduleNodes,
      edges: moduleEdges
    };

    const blob = new Blob([JSON.stringify(exportPayload, null, 2)], { type: 'application/json' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = `${moduleId || 'modular_graph'}.json`;
    a.click();
    URL.revokeObjectURL(url);
  }
}

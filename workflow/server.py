"""
DRAM Foundation VN - FastAPI Local Bridge Server
Exposes the multi-agent AI Council, ChromaDB Vector Store, and Modular WBS DAG
to the local frontend React Flow Sandbox.
"""

import sys
from pathlib import Path
import json
from typing import Dict, Any, List, Optional

BASE_DIR = Path(__file__).resolve().parent.parent
if str(BASE_DIR) not in sys.path:
    sys.path.insert(0, str(BASE_DIR))

from fastapi import FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, RedirectResponse
from pydantic import BaseModel, Field

from workflow.vector_store import SemiconductorVectorStore
from workflow.council.orchestrator import AICouncilOrchestrator
from workflow.crawler import SemiconductorCrawler

DATA_DIR = BASE_DIR / "data"
MODULES_DIR = DATA_DIR / "modules"
MANIFEST_PATH = DATA_DIR / "manifest.json"
SANDBOX_DIR = BASE_DIR / "sandbox"

app = FastAPI(
    title="DRAM Foundation VN - Knowledge OS API",
    description="Local Bridge Server for AI Council, ChromaDB RAG, and Modular WBS DAG",
    version="1.0.0"
)

# Enable CORS for frontend local development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Global singletons
vector_store = SemiconductorVectorStore()
council = AICouncilOrchestrator(vector_store=vector_store)
crawler = SemiconductorCrawler(vector_store=vector_store)


# ---------------------------------------------------------
# Request Models
# ---------------------------------------------------------
class ReviewRequest(BaseModel):
    node_id: str = Field(..., description="Unique ID for candidate node, e.g. node-rf-sputter")
    title: str = Field(..., description="Title of the work package")
    description: str = Field(..., description="Technical description and engineering details")
    generation: str = Field(default="Gen 1 (mm)", description="Gen 1 (mm), Gen 2 (µm), or Gen 3 (nm)")
    category: str = Field(default="Precision Mechanics", description="Discipline category")
    prerequisite_node_ids: List[str] = Field(default_factory=list, description="IDs of prerequisite nodes")
    target_module: Optional[str] = Field(default=None, description="Module file to commit to")


class CommitRequest(BaseModel):
    node: Dict[str, Any] = Field(..., description="Approved node payload")
    proposed_edges: List[Dict[str, Any]] = Field(default_factory=list, description="Associated incoming edges")
    target_module: str = Field(..., description="Target module file or ID, e.g. 02_litho_stage_gen1.json")


class CrawlRequest(BaseModel):
    url: Optional[str] = Field(default=None, description="Public web page URL to crawl")
    pdf_path: Optional[str] = Field(default=None, description="Local PDF path to ingest")
    category: str = Field(default="Semiconductor Knowledge", description="Category tag")
    seed: bool = Field(default=False, description="Ingest built-in baseline seed literature")


class SearchRequest(BaseModel):
    query: str = Field(..., description="Semantic search query")
    n_results: int = Field(default=5, ge=1, le=100, description="Number of literature chunks to return")


# ---------------------------------------------------------
# API Endpoints
# ---------------------------------------------------------
@app.get("/api/status")
def get_system_status():
    """Returns the current state of vector store and modular DAG."""
    graph = council.load_all_existing_graph()
    manifest = {}
    if MANIFEST_PATH.exists():
        with open(MANIFEST_PATH, "r", encoding="utf-8") as f:
            manifest = json.load(f)

    return {
        "status": "online",
        "chroma_chunks": vector_store.count(),
        "total_nodes": len(graph["nodes"]),
        "total_edges": len(graph["edges"]),
        "modules_count": len(manifest.get("modules", [])),
        "exclusive_model": "Gemini (Google Antigravity)",
        "decision_model": "Laya ModernBERT CPU"
    }


@app.get("/api/graph")
def get_full_graph():
    """Returns combined nodes and edges from all registered modules."""
    return council.load_all_existing_graph()


@app.get("/api/manifest")
def get_manifest():
    """Returns data/manifest.json."""
    if not MANIFEST_PATH.exists():
        raise HTTPException(status_code=404, detail="Manifest file not found")
    with open(MANIFEST_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


@app.get("/api/modules")
def list_modules():
    """Returns list of all modules with their individual nodes and edges."""
    if not MANIFEST_PATH.exists():
        return []
    with open(MANIFEST_PATH, "r", encoding="utf-8") as f:
        manifest = json.load(f)

    modules_data = []
    for mod_info in manifest.get("modules", []):
        file_path = DATA_DIR.parent / mod_info.get("file", "")
        if not file_path.exists():
            file_path = MODULES_DIR / Path(mod_info.get("file", "")).name
        
        content = {}
        if file_path.exists():
            with open(file_path, "r", encoding="utf-8") as f:
                content = json.load(f)
        
        modules_data.append({
            "info": mod_info,
            "data": content
        })
    return modules_data


@app.get("/api/modules/{module_id}")
def get_single_module(module_id: str):
    """Returns details for a specific module."""
    for f in MODULES_DIR.glob("*.json"):
        with open(f, "r", encoding="utf-8") as fp:
            data = json.load(fp)
            if data.get("module_id") == module_id or f.stem == module_id:
                return data
    raise HTTPException(status_code=404, detail=f"Module '{module_id}' not found")


@app.post("/api/council/review")
def review_node(req: ReviewRequest):
    """
    Invokes the AI Council (Systems Engineer, Laya PM, Gemini Domain Expert)
    to validate DAG acyclicity, 8-80h rule, Make/Buy classification, and SOP synthesis.
    """
    result = council.review_candidate_node(
        node_id=req.node_id,
        title=req.title,
        description=req.description,
        generation=req.generation,
        category=req.category,
        prerequisite_node_ids=req.prerequisite_node_ids
    )
    return result


@app.post("/api/council/commit")
def commit_node(req: CommitRequest):
    """
    Appends an approved node and edges into the designated modular JSON file
    and updates data/manifest.json.
    """
    try:
        res = council.commit_approved_node(
            node=req.node,
            edges=req.proposed_edges,
            module_file=req.target_module
        )
        return res
    except FileNotFoundError as fnf:
        raise HTTPException(status_code=404, detail=str(fnf))
    except (ValueError, KeyError) as ve:
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to commit node: {str(e)}")


@app.post("/api/crawl")
def trigger_crawl(req: CrawlRequest):
    """Ingests semiconductor literature from URL, PDF, or seed corpus."""
    if req.seed:
        count = crawler.ingest_seed_knowledge()
        return {"status": "success", "type": "seed", "indexed_chunks": count}
    
    if req.url:
        try:
            count = crawler.ingest_url(req.url, category=req.category)
            return {"status": "success", "type": "url", "url": req.url, "indexed_chunks": count}
        except Exception as e:
            raise HTTPException(status_code=400, detail=f"Crawl failed: {str(e)}")

    if req.pdf_path:
        try:
            count = crawler.ingest_pdf(req.pdf_path, category=req.category)
            return {"status": "success", "type": "pdf", "pdf_path": req.pdf_path, "indexed_chunks": count}
        except Exception as e:
            raise HTTPException(status_code=400, detail=f"PDF ingestion failed: {str(e)}")

    raise HTTPException(status_code=400, detail="Must provide either url, pdf_path, or seed=True")


@app.post("/api/search")
def search_knowledge(req: SearchRequest):
    """Performs semantic vector search against ChromaDB semiconductor corpus."""
    if req.n_results < 1 or req.n_results > 100:
        raise HTTPException(status_code=400, detail="n_results must be between 1 and 100")
    try:
        hits = vector_store.query(req.query, n_results=req.n_results)
    except (TypeError, ValueError) as e:
        raise HTTPException(status_code=400, detail=str(e))
    return {
        "query": req.query,
        "total_hits": len(hits),
        "results": hits
    }


# ---------------------------------------------------------
# Static Files & UI Serving
# ---------------------------------------------------------
if SANDBOX_DIR.exists():
    app.mount("/sandbox", StaticFiles(directory=str(SANDBOX_DIR), html=True), name="sandbox")

if DATA_DIR.exists():
    app.mount("/data", StaticFiles(directory=str(DATA_DIR)), name="data")


@app.get("/data-engine.js")
def serve_data_engine():
    """Serves data-engine.js for root frontend import."""
    engine_file = BASE_DIR / "data-engine.js"
    if engine_file.exists():
        return FileResponse(engine_file, media_type="application/javascript")
    return FileResponse(SANDBOX_DIR / "data-engine.js", media_type="application/javascript")


@app.get("/")
def root():
    """Serves index.html or redirects to /sandbox/."""
    index_file = BASE_DIR / "index.html"
    if index_file.exists():
        return FileResponse(index_file)
    return RedirectResponse(url="/sandbox/index.html")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("workflow.server:app", host="127.0.0.1", port=8000, reload=True)

"""
DRAM Foundation VN - Master Workflow CLI
Provides command-line orchestration for the Internet Crawler and the Multi-Agent AI Council.
"""

import sys
import argparse
import json
from workflow.vector_store import SemiconductorVectorStore
from workflow.crawler import SemiconductorCrawler
from workflow.council.orchestrator import AICouncilOrchestrator


def cmd_status(args):
    store = SemiconductorVectorStore()
    orchestrator = AICouncilOrchestrator(vector_store=store)
    graph = orchestrator.load_all_existing_graph()

    print("\n========================================================")
    print("  DRAM Foundation VN - Systems Workflow Status")
    print("========================================================")
    print(f"• ChromaDB Vector Store:  {store.count()} indexed document chunks")
    print(f"• Modular DAG Nodes:     {len(graph['nodes'])} nodes active")
    print(f"• Modular DAG Edges:     {len(graph['edges'])} edges active")
    print("• Council Decision Engine: Laya (Local CPU ModernBERT)")
    print("• Generative Model:       Gemini (Exclusive)")
    print("========================================================\n")


def cmd_crawl(args):
    store = SemiconductorVectorStore()
    crawler = SemiconductorCrawler(vector_store=store)

    if args.seed:
        print("[Crawler] Ingesting baseline semiconductor seed literature...")
        count = crawler.ingest_seed_knowledge()
        print(f"[Crawler] Successfully indexed {count} baseline literature chunks into ChromaDB.")
    elif args.url:
        print(f"[Crawler] Crawling URL: {args.url}")
        count = crawler.ingest_url(args.url, category=args.category)
        print(f"[Crawler] Ingested {count} chunks from {args.url}")
    elif args.pdf:
        print(f"[Crawler] Ingesting PDF: {args.pdf}")
        count = crawler.ingest_pdf(args.pdf, category=args.category)
        print(f"[Crawler] Ingested {count} chunks from PDF.")
    else:
        print("Please specify --seed, --url <url>, or --pdf <path>.")


def cmd_review(args):
    orchestrator = AICouncilOrchestrator()
    print(f"\n[Council] Convening AI Council review for candidate node: '{args.title}'...")
    
    prereqs = [p.strip() for p in args.prereqs.split(",")] if args.prereqs else []
    result = orchestrator.review_candidate_node(
        node_id=args.id,
        title=args.title,
        description=args.desc,
        generation=args.gen,
        category=args.cat,
        prerequisite_node_ids=prereqs
    )

    print("\n========================================================")
    print(f"  Council Verdict: {result['verdict']}")
    print("========================================================")
    if not result.get("approved"):
        print(f"❌ Rejection Stage: {result.get('stage')}")
        print(f"❌ Reason:          {result.get('reason')}")
        return

    node = result["node"]
    pm = result["pm_decision"]
    print(f"✓ Systems Engineer Check: {result['systems_engineer_check']}")
    print(f"✓ PM Scope Decision:     {pm['scope_decision']} ({pm['estimated_hours']}h)")
    print(f"✓ Supply Chain Tag:      {node['action_type']} (via {pm['engine']})")
    print(f"✓ Primary Target Metric: {node['primary_metric']}")
    print(f"✓ Literature Citations:  {len(node['citations'])} sources cited from ChromaDB")
    print("\n--- Leaf SOP Preview ---")
    print(node["sop_content"])
    print("------------------------\n")

    if args.export:
        with open(args.export, "w", encoding="utf-8") as f:
            json.dump(result, f, indent=2, ensure_ascii=False)
        print(f"[Council] Full approved work package exported to: {args.export}")


def main():
    parser = argparse.ArgumentParser(description="DRAM Foundation VN - Workflow CLI")
    subparsers = parser.add_subparsers(dest="command", help="Workflow command to run")

    # Status
    p_status = subparsers.add_parser("status", help="Show vector store and graph status")
    p_status.set_defaults(func=cmd_status)

    # Crawl
    p_crawl = subparsers.add_parser("crawl", help="Ingest web or PDF knowledge into ChromaDB")
    p_crawl.add_argument("--seed", action="store_true", help="Ingest baseline semiconductor seed literature")
    p_crawl.add_argument("--url", type=str, help="Crawl public web page URL")
    p_crawl.add_argument("--pdf", type=str, help="Extract text from local PDF file")
    p_crawl.add_argument("--category", type=str, default="Technical Literature", help="Category tag")
    p_crawl.set_defaults(func=cmd_crawl)

    # Review
    p_review = subparsers.add_parser("review", help="Run 4-stage AI Council review on candidate node")
    p_review.add_argument("--id", type=str, required=True, help="Node ID (e.g. node-spin-coat-gen1)")
    p_review.add_argument("--title", type=str, required=True, help="Work package title")
    p_review.add_argument("--desc", type=str, required=True, help="Detailed technical description")
    p_review.add_argument("--gen", type=str, default="Gen 1 (mm)", choices=["Gen 1 (mm)", "Gen 2 (µm)", "Gen 3 (nm)"], help="TRL Generation")
    p_review.add_argument("--cat", type=str, default="Chemical Processing", help="Discipline category")
    p_review.add_argument("--prereqs", type=str, default="", help="Comma-separated prerequisite node IDs")
    p_review.add_argument("--export", type=str, help="Path to export verified JSON payload")
    p_review.set_defaults(func=cmd_review)

    args = parser.parse_args()
    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()

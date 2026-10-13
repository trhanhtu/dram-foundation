"""
DRAM Foundation VN - Literature Ingestion & ChromaDB Seeding Engine
Batch-indexes verified empirical semiconductor literature and crawls open-access PDK repos.
"""

import sys
from pathlib import Path
import re
from typing import List, Dict, Any

# Ensure project root in sys.path
PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

import httpx
from bs4 import BeautifulSoup

from workflow.vector_store import SemiconductorVectorStore
from workflow.literature_corpus import COMPREHENSIVE_SEMICONDUCTOR_CORPUS

ONLINE_TECHNICAL_SOURCES = [
    {
        "url": "https://raw.githubusercontent.com/google/skywater-pdk/main/README.rst",
        "title": "SkyWater 130nm Open PDK Overview & Architecture",
        "category": "Open PDK & Foundry"
    },
    {
        "url": "https://raw.githubusercontent.com/google/skywater-pdk-libs-sky130_fd_pr/main/README.rst",
        "title": "SkyWater 130nm Primitive Devices & Models",
        "category": "Device Physics & Models"
    },
    {
        "url": "https://raw.githubusercontent.com/The-OpenROAD-Project/OpenROAD/master/README.md",
        "title": "OpenROAD Physical Design & Synthesis Toolflow",
        "category": "EDA Toolflow"
    },
    {
        "url": "https://raw.githubusercontent.com/efabless/caravel/main/README.md",
        "title": "Efabless Caravel Open Source Silicon Test Harness",
        "category": "Packaging & Harness"
    }
]


def chunk_text(text: str, chunk_size: int = 250) -> List[str]:
    """Splits text into cohesive word chunks of specified length."""
    words = text.split()
    chunks = []
    for i in range(0, len(words), chunk_size):
        chunk = " ".join(words[i:i + chunk_size])
        if len(chunk.strip()) > 40:
            chunks.append(chunk.strip())
    return chunks


def seed_corpus_and_crawl() -> Dict[str, Any]:
    print("=" * 60)
    print("🚀 DRAM Foundation VN: Seeding Empirical Literature Corpus")
    print("=" * 60)

    store = SemiconductorVectorStore()
    initial_count = store.collection.count()
    print(f"📊 Initial ChromaDB Chunk Count: {initial_count}")

    total_added = 0

    # 1. Ingest Comprehensive Static Literature Corpus
    print("\n📚 [1/2] Indexing Grounded Semiconductor Engineering Literature...")
    for doc in COMPREHENSIVE_SEMICONDUCTOR_CORPUS:
        chunks = chunk_text(doc["content"], chunk_size=150)
        for idx, chunk in enumerate(chunks):
            doc_id = f"corpus_{doc['id']}_chunk_{idx}"
            metadata = {
                "title": doc["title"],
                "source": doc["source"],
                "category": doc["category"],
                "chunk_index": idx
            }
            store.add_document(doc_id, chunk, metadata)
            total_added += 1
        print(f"  ✓ Indexed '{doc['title']}' ({len(chunks)} chunks)")

    # 2. Ingest Online Open-Source Semiconductor Repositories
    print("\n🌐 [2/2] Crawling Open-Source PDK & Foundry Repositories...")
    with httpx.Client(timeout=15.0, follow_redirects=True) as client:
        for item in ONLINE_TECHNICAL_SOURCES:
            url = item["url"]
            title = item["title"]
            cat = item["category"]
            try:
                resp = client.get(url, headers={"User-Agent": "DRAM-Foundation-VN-Bot/1.0"})
                if resp.status_code == 200:
                    text_content = resp.text
                    # Simple markdown / rst strip
                    clean_text = re.sub(r"```.*?```", "", text_content, flags=re.DOTALL)
                    clean_text = re.sub(r"(\.\. [a-zA-Z0-9_\-]+::|:[a-zA-Z0-9_\-]+:)", "", clean_text)
                    chunks = chunk_text(clean_text, chunk_size=250)
                    slug = re.sub(r"[^a-zA-Z0-9]+", "_", title)[:35]
                    for idx, chunk in enumerate(chunks[:8]):  # Take top 8 high-density chunks per repo
                        doc_id = f"online_{slug}_{idx}"
                        metadata = {
                            "title": title,
                            "source": url,
                            "category": cat,
                            "chunk_index": idx
                        }
                        store.add_document(doc_id, chunk, metadata)
                        total_added += 1
                    print(f"  ✓ Ingested '{title}' from {url} ({min(len(chunks), 8)} chunks)")
                else:
                    print(f"  ⚠️ Warning: {url} returned HTTP {resp.status_code}")
            except Exception as e:
                print(f"  ⚠️ Could not fetch {url}: {e}")

    final_count = store.collection.count()
    print("\n" + "=" * 60)
    print(f"🎉 Seeding Complete! Added {total_added} chunks.")
    print(f"📊 Final ChromaDB Chunk Count: {final_count} (was {initial_count})")
    print("=" * 60)

    return {
        "initial_count": initial_count,
        "final_count": final_count,
        "added": total_added
    }


if __name__ == "__main__":
    seed_corpus_and_crawl()

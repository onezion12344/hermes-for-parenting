#!/usr/bin/env python3
"""Update topics.json with a new topic entry."""
import json
import sys
from pathlib import Path
from datetime import datetime

DOCS_DIR = Path(__file__).parent.parent / "docs"
TOPICS_FILE = DOCS_DIR / "topics.json"

def main():
    if len(sys.argv) < 3:
        print("Usage: update_topics.py <topic_id> <title> [summary] [tags]")
        sys.exit(1)

    topic_id = sys.argv[1]
    title = sys.argv[2]
    summary = sys.argv[3] if len(sys.argv) > 3 else ""
    tags = sys.argv[4].split(",") if len(sys.argv) > 4 else []

    topics = []
    if TOPICS_FILE.exists():
        topics = json.loads(TOPICS_FILE.read_text())

    # Remove existing entry with same id
    topics = [t for t in topics if t.get("id") != topic_id]

    topics.insert(0, {
        "id": topic_id,
        "title": title,
        "summary": summary,
        "date": datetime.now().strftime("%Y年%m月%d日"),
        "tags": [t.strip() for t in tags if t.strip()]
    })

    TOPICS_FILE.write_text(json.dumps(topics, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Updated topics.json: {title} ({topic_id})")

if __name__ == "__main__":
    main()

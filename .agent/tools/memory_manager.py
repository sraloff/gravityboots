#!/usr/bin/env python3
"""
memory_manager.py - Simple persistent memory manager for agentic coding projects

Usage examples:
  python memory_manager.py read
  python memory_manager.py update project.name "My New SaaS App"
  python memory_manager.py append key_decisions "Adopted flat skills structure"
  python memory_manager.py append recent_milestones '{"date": "2026-01-22", "description": "Added lint-validation skill"}'
"""

import json
import sys
from datetime import datetime
from pathlib import Path
from typing import Any

# Make paths relative to repo root from script location (.agent/tools/)
REPO_ROOT = Path(__file__).resolve().parent.parent.parent
MEMORY_FILE = REPO_ROOT / "docs/context/memory.json"
TEMPLATE_FILE = REPO_ROOT / "docs/context/memory-template.json"


def ensure_file_exists() -> None:
    """Create memory.json from template if missing, or fallback to minimal defaults."""
    if MEMORY_FILE.exists():
        return

    MEMORY_FILE.parent.mkdir(parents=True, exist_ok=True)

    if TEMPLATE_FILE.exists():
        with TEMPLATE_FILE.open("r", encoding="utf-8") as t:
            data = json.load(t)
        with MEMORY_FILE.open("w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        print(f"Created memory.json from template: {MEMORY_FILE}")
        return

    # Fallback minimal structure if template also missing
    fallback = {
        "project": {
            "name": "[Project Name – to be customized]",
            "description_summary": "New project bootstrapped from Gravity Boots template",
            "last_updated": datetime.utcnow().isoformat() + "Z"
        },
        "prd_summary": "Vision: [to be filled]",
        "scope_summary": "In scope: [to be filled]",
        "technical_specs_summary": "Stack: [to be filled]",
        "active_user_stories": [],
        "open_questions": [],
        "key_decisions": ["Bootstrapped with project-init skill"],
        "recent_milestones": [],
        "last_agent_action": {
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "summary": "Fallback memory created (template missing)"
        }
    }
    with MEMORY_FILE.open("w", encoding="utf-8") as f:
        json.dump(fallback, f, indent=2, ensure_ascii=False)
    print(f"Created fallback memory.json: {MEMORY_FILE}")


def load_memory() -> dict:
    """Load the current memory.json content."""
    ensure_file_exists()
    with MEMORY_FILE.open("r", encoding="utf-8") as f:
        return json.load(f)


def save_memory(data: dict) -> None:
    """Save updated memory back to file."""
    with MEMORY_FILE.open("w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"Memory updated: {MEMORY_FILE}")


def update_field(key_path: str, value: Any) -> None:
    """Update a field using dot notation (e.g., 'project.name' or 'last_agent_action.summary')."""
    data = load_memory()
    keys = key_path.split(".")
    current = data
    for k in keys[:-1]:
        if k not in current or not isinstance(current[k], dict):
            current[k] = {}
        current = current[k]
    current[keys[-1]] = value
    save_memory(data)


def append_to_list(key: str, item: Any) -> None:
    """Append an item (str or dict) to a list in memory."""
    data = load_memory()
    if key not in data:
        data[key] = []
    if not isinstance(data[key], list):
        raise ValueError(f"Key '{key}' is not a list")
    data[key].append(item)
    save_memory(data)


def read() -> None:
    """Print the current memory content."""
    data = load_memory()
    print(json.dumps(data, indent=2))


def main():
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python memory_manager.py read")
        print("  python memory_manager.py update <key.path> <value>")
        print("  python memory_manager.py append <key> <item>")
        sys.exit(1)

    cmd = sys.argv[1]

    if cmd == "read":
        read()
    elif cmd == "update" and len(sys.argv) == 4:
        update_field(sys.argv[2], sys.argv[3])
    elif cmd == "append" and len(sys.argv) >= 4:
        key = sys.argv[2]
        item = " ".join(sys.argv[3:])  # string for now
        append_to_list(key, item)
    else:
        print("Invalid command or arguments")
        sys.exit(1)


if __name__ == "__main__":
    main()
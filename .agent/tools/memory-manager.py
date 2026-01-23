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

MEMORY_FILE = Path("docs/context/memory.json")


def ensure_file_exists() -> None:
    """Create memory.json with default structure if it doesn't exist."""
    if not MEMORY_FILE.exists():
        default_data = {
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
                "summary": "Initial project memory created"
            }
        }
        MEMORY_FILE.parent.mkdir(parents=True, exist_ok=True)
        with open(MEMORY_FILE, "w", encoding="utf-8") as f:
            json.dump(default_data, f, indent=2, ensure_ascii=False)
        print(f"Created initial memory file: {MEMORY_FILE}")


def load_memory() -> dict:
    """Load the current memory.json content."""
    ensure_file_exists()
    with open(MEMORY_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_memory(data: dict) -> None:
    """Save updated memory back to file."""
    with open(MEMORY_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"Memory updated: {MEMORY_FILE}")


def update_field(key_path: str, value: Any) -> None:
    """
    Update a field using dot notation (e.g., 'project.name' or 'last_agent_action.summary').
    """
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
        key_path = sys.argv[2]
        value = sys.argv[3]  # Simple string for now; can extend to JSON later
        update_field(key_path, value)

    elif cmd == "append" and len(sys.argv) >= 4:
        key = sys.argv[2]
        item = " ".join(sys.argv[3:])  # Treat rest as string (extend for JSON if needed)
        append_to_list(key, item)

    else:
        print("Invalid command or arguments")
        sys.exit(1)


if __name__ == "__main__":
    main()
#!/usr/bin/env python3
"""
init_project.py - Automates the bootstrap process for a new Antigravity project.

Usage:
  python .agent/tools/init_project.py [project_name]
"""

import os
import sys
import json
from datetime import datetime
from pathlib import Path

REPO_ROOT = Path(os.getcwd())

DIRS_TO_CREATE = [
    ".agent/skills",
    ".agent/rules",
    "docs/planning",
    "docs/context",
    "docs/decisions",
    "sql",
    "examples/json",
    "src/backend",
    "src/frontend",
]

FILES_TO_TOUCH = [
    "docs/planning/prd.md",
    "docs/planning/scope.md",
    "docs/planning/technical-specs.md",
    "docs/planning/user-stories.md",
    "docs/planning/active_sprint.md",
]

MEMORY_TEMPLATE = {
    "project": {
        "name": "{project_name}",
        "description_summary": "New project bootstrapped via init_project.py",
        "last_updated": "{timestamp}"
    },
    "prd_summary": "Vision: [To be filled]",
    "scope_summary": "In scope: [To be filled]",
    "technical_specs_summary": "Stack: [To be filled]",
    "active_user_stories": [],
    "open_questions": [],
    "key_decisions": ["Project initialized"],
    "recent_milestones": [],
    "last_agent_action": {
        "timestamp": "{timestamp}",
        "summary": "Project structure created"
    }
}

def create_dirs():
    print("Creating directories...")
    
    # Check for existing frameworks to avoid conflict
    is_laravel = (REPO_ROOT / "artisan").exists()
    is_node_root = (REPO_ROOT / "package.json").exists()

    for d in DIRS_TO_CREATE:
        # Skip creating src/backend if Laravel is detected (it uses app/)
        if is_laravel and d == "src/backend":
            print(f"  - Skipping {d} (Laravel detected)")
            continue
            
        # Skip src/frontend if we are in a monorepo root or single-app root
        if is_node_root and d == "src/frontend":
             print(f"  - Skipping {d} (Node root detected)")
             continue

        path = REPO_ROOT / d
        if not path.exists():
            path.mkdir(parents=True, exist_ok=True)
            print(f"  + {d}/")
        else:
            print(f"  . {d}/ (exists)")


PLANNING_TEMPLATES = {
    "docs/planning/prd.md": """# Product Requirements Document (PRD)
**Project Name:** {project_name}
**Version:** 1.0
**Status:** Draft

## 1. Overview & Purpose
**One-sentence summary**
<!-- What are we building and why? -->

**Target Users**
<!-- Who is this for? -->

**Success Metrics**
<!-- How do we know it works? -->

## 2. Key Goals
**Must Have**
- [ ] Feature A
- [ ] Feature B

**Nice to Have**
- [ ] Feature C
""",
    "docs/planning/scope.md": """# Project Scope
**Project:** {project_name}

## In Scope
- [ ] ...

## Out of Scope
- [ ] ...
""",
    "docs/planning/technical-specs.md": """# Technical Specifications
**Stack:**
- Frontend: [e.g., Next.js]
- Backend: [e.g., Python FastAPI]
- Database: [e.g., PostgreSQL]

## Architecture
<!-- Describe high-level design -->

## Data Models
<!-- Key entities -->
""",
    "docs/planning/user-stories.md": """# User Stories

## Epical
1. As a [user], I want to [action] so that [benefit].
   - Acceptance Criteria:
     - [ ] Criteria 1
     - [ ] Criteria 2
"""
}

def create_files(project_name="New Project"):
    print("Creating scaffolded files...")
    
    # 1. Planning Docs (with templates)
    for path_str, content in PLANNING_TEMPLATES.items():
        path = REPO_ROOT / path_str
        if not path.exists():
            with open(path, "w") as f:
                f.write(content.format(project_name=project_name))
            print(f"  + {path_str} (scaffolded)")
        else:
            print(f"  . {path_str} (exists)")

    # 2. Other placeholder files
    other_files = ["docs/planning/active_sprint.md"]
    for f in other_files:
        path = REPO_ROOT / f
        if not path.exists():
            path.touch()
            print(f"  + {f}")
        else:
            print(f"  . {f} (exists)")


def init_memory(project_name):
    memory_path = REPO_ROOT / "docs/context/memory.json"
    if memory_path.exists():
        print("  . memory.json (exists)")
        return

    timestamp = datetime.utcnow().isoformat() + "Z"
    # Fill template
    data = MEMORY_TEMPLATE.copy()
    data["project"]["name"] = project_name
    data["project"]["last_updated"] = timestamp
    data["last_agent_action"]["timestamp"] = timestamp

    with open(memory_path, "w") as f:
        json.dump(data, f, indent=2)
    print("  + docs/context/memory.json")

def main():
    project_name = "New Project"
    if len(sys.argv) > 1:
        project_name = sys.argv[1]

    print(f"Initializing project: {project_name}")
    create_dirs()
    create_files(project_name)
    init_memory(project_name)
    print("\nDone. \033[92mProject initialized successfully.\033[0m")

if __name__ == "__main__":
    main()

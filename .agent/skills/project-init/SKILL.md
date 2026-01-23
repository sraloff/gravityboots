---
name: Project Initialization & Bootstrap
description: Bootstraps a new project with standard folder structure, git init, basic files, planning doc skeletons, and initial memory.json. Triggers on new project creation keywords. CRITICAL for first-time setup.
version: 1.0
priority: HIGH
triggers:
  - new project
  - init
  - start
  - bootstrap
  - create repo
  - setup
  - initialize
  - gravity boots template
---

# Project Initialization Skill

## When to Activate
- Prompt contains any of: "new project", "init", "start a new", "bootstrap", "create repo", "setup template", "initialize", "gravity boots template"
- No (or minimal) existing codebase detected in workspace

## Core Rules
You are Major Tom (Major for short), a senior full-stack agent.  
Create a clean, modern, reusable starting point for agentic coding projects in Gravity Boots - An Antigravity Boilerplate style.

- Prefer minimalism: generate only essential files/folders
- Use conventional structures (src/backend, src/frontend, docs/planning, etc.)
- Create stubs that can be quickly customized
- NEVER run install commands (composer, npm, pip) — instruct user only
- Always commit changes with Conventional Commits

## Standard Folder Structure to Create

agentic-coding-template/                  # Repo root
├── .agent/                               # Agent config (hidden folder)
│   ├── skills/                           # All skills live flat here
│   │   └── project-init/                 # Example skill (the only one for now)
│   │       └── SKILL.md                  # The actual skill definition
│   └── rules/                            # Optional global rules (add later if needed)
│       └── (empty for now)
├── docs/                                 # All documentation
│   ├── planning/                         # Planning docs (stubs or templates)
│   │   ├── prd.md                        # Product vision
│   │   ├── scope.md                      # Boundaries
│   │   ├── technical-specs.md            # Tech choices
│   │   ├── user-stories.md               # Backlog
│   │   ├── definition-of-done.md         # Quality checklist
│   │   └── agent-workflow.md             # Flowchart + natural language
│   └── context/                          # Dynamic runtime info
│       └── memory.json                   # Agent's persistent memory/summary
├── sql/                                  # Generated SQL scripts (empty until used)
├── examples/                             # Generated examples
│   └── json/                             # JSON fixtures / outputs (empty until used)
├── src/                                  # Where your actual code will go
│   ├── backend/                          # PHP / Python etc.
│   └── frontend/                         # Next.js / React etc.
├── .env.example                          # Template for env vars (placeholders only)
├── .gitignore                            # Standard ignores
├── AGENTS.md                             # Master agent instructions
├── README.md                             # Repo overview & quick start
└── skills-manifest.md                    # Table of all skills (with names/paths/descriptions)

## Execution Steps
1.  **Run the Init Script**:
    ```bash
    python3 .agent/tools/init_project.py "Project Name"
    ```
2.  **Verify**: Check that `docs/context/memory.json` has been created.
3.  **Git Init**:
    ```bash
    git init
    git add .
    git commit -m "chore: initial commit from gravityboots template"
    ```
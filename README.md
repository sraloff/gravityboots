# Gravity Boots - Antigravity Boilerplate
A reusable Git template repo for high-performance agentic coding with Antigravity, Claude Code, Cursor, and similar tools.  
Supports legacy (PHP/WordPress/LAMP) and modern stacks (Python/FastAPI, Next.js/React Native) with modular skills, planning docs, and token-optimized workflows.

## Quick Start

1. Clone this repo as a template:
git clone https://github.com/[your-username]/agentic-template.git my-new-project cd my-new-project

2. Initialize the project (run in your agent):
Initialize a new project using this template

→ The `project-init` skill will create folders, git init, AGENTS.md, basic docs, etc.

3. Customize:
- Edit `/docs/planning/prd.md` with your project vision
- Add your first skills to `.agent/skills/`
- Update `AGENTS.md` if you want custom persona/rules

4. Start prompting:
- "Add user authentication with OAuth"
- "Optimize slow dashboard query"
- "Generate Mermaid flowchart for deployment flow"

## Folder Structure Overview

- `.agent/skills/` → Granular agent skills (each with SKILL.md)
- `docs/planning/` → PRD, scope, specs, stories, DoD
- `docs/context/` → current-status.md (living project memory)
- `sql/` & `examples/json/` → Agent-generated artifacts
- `src/` → Modular code (backend/python, backend/php, frontend/nextjs, etc.)
- `AGENTS.md` → Master agent instructions (persona, workflow, rules)

## Agent Workflow (Mermaid)

```mermaid
flowchart TD
 Start[User Prompt] --> Plan[Scan Context + Activate Skills + Create Plan]
 Plan --> Approval{Approve Plan?}
 Approval -->|Yes| Execute[Silent Execution + Save Artifacts]
 Approval -->|No| Revise[Revise Based on Feedback]
 Revise --> Approval
 Execute --> Finish[Confirm + Summary]

Key Features
•  Progressive skill loading (1–4 active at a time)
•  Yes/no approval loop + silent execution mode
•  Token optimization (<25k target)
•  Artifact organization (/sql/, /examples/json/)
•  Supports mixed stacks: PHP, Python, Next.js, etc.
Contributing
Pull requests welcome! Please follow Conventional Commits.

When using this template:
- GitHub copies AGENTS.md automatically — do not delete or overwrite it.
- The project-init skill will detect and use the existing AGENTS.md.

Last Updated: January 21, 2026

These three pieces should give your template a strong, self-contained starting point.


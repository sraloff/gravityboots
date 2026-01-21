# Product Requirements Document (PRD)  
**Project Name:** [e.g., Agentic Coding Template v2]  
**Version:** 1.0  
**Last Updated:** January 21, 2026  
**Owner:** Shawn (@sraloff) – Portland, OR  

## 1. Overview & Purpose

**One-sentence summary**  
A reusable Git template repo that enables high-performance agentic coding across legacy (PHP/WordPress/LAMP) and modern stacks (Python/FastAPI, Next.js/React Native), with modular skills, planning docs, and optimized context loading for Antigravity, Claude Code, and Cursor.

**Why are we building this?**  
- Speed up development velocity while maintaining quality and avoiding poorly-thought-through code.  
- Support mixed old-school + cutting-edge projects without reinventing setup every time.  
- Give agents clear, versioned instructions so they produce consistent, efficient output with minimal token bloat.

**Target users**  
- Shawn (primary): full-stack developer maintaining legacy apps while building new ones.  
- Future collaborators / open-source contributors who want a plug-and-play agentic template.

**Success looks like**  
- New project bootstrap in <10 minutes via `project-init` skill.  
- Agents activate only relevant skills and stay under 25k tokens in active sessions.  
- Code produced follows agreed standards (Conventional Commits, PSR-12, ES2025+, etc.).  
- Planning docs remain lightweight and updatable.

## 2. Key Goals & Non-Goals

**Must achieve**  
- Modular skill system with progressive disclosure  
- Clear separation of agent instructions (AGENTS.md) from product vision (this PRD)  
- Yes/no approval loop + silent execution mode after plan approval  
- Artifact organization (/sql/, /examples/json/, /docs/context/current-status.md)  

**Nice to have**  
- Auto-generated Mermaid flowcharts on request  
- Built-in lint/validation gates triggered post-execution  

**Non-goals (out of scope for now)**  
- Full CI/CD pipeline automation (handled via ci-cd-deployment skill)  
- Native mobile app deployment (focus on React Native patterns only)  
- Paid third-party integrations (e.g., LangChain Pro, premium models)  
- GUI for skill management (text-based manifest + manual folder creation)

## 3. Core Features & Priorities (MoSCoW)

**Must have**  
- Project initialization flow (new repo setup, git init, basic folders/docs)  
- Granular skill activation (1–4 skills max per task)  
- Context optimization rules (new vs active project loading)  
- Yes/no loop for plan approval + silent execution mode  
- Artifact saving rules (/sql/, /examples/json/)  

**Should have**  
- Lightweight /docs/context/current-status.md for ongoing memory  
- Mermaid flowchart for agent workflow (agent-workflow.mmd)  
- Sample planning docs templates in /docs/planning/  

**Could have**  
- Auto-update of current-status.md after major tasks  
- Integration with external tools (Vercel deploy, Docker compose)  

**Won’t have (for v1)**  
- Built-in LLM model switching UI  
- Visual skill editor  

## 4. User Stories / Epics (High-Level)

As a developer using this template, I want…  

1. …to bootstrap a new project quickly so I can start coding immediately.  
   - Acceptance: Run `project-init` skill → get folders, git init, AGENTS.md, basic planning stubs.

2. …agents to load only relevant skills and docs so context stays efficient.  
   - Acceptance: New project → minimal load; active project → 1–4 skills + open files + current-status.md.

3. …to review plans before execution so code stays thoughtful.  
   - Acceptance: Yes/no loop enforced; silent mode after approval.

4. …generated artifacts (SQL, JSON examples) to be saved in predictable folders.  
   - Acceptance: Files appear in /sql/ and /examples/json/; paths confirmed in output.

(Expand this list as needed per project; keep it short.)

## 5. Assumptions & Constraints

**Assumptions**  
- User has Antigravity/Claude Code/Cursor installed and configured.  
- Access to capable models (Gemini 1.5+, Claude 3.5+, etc.) with 32k+ context.  
- Git is used for version control.

**Constraints**  
- Keep total active context under 25k tokens in typical sessions.  
- Support mixed stacks without forcing one toolchain.  
- No paid dependencies required for core functionality.

**Risks & Mitigations**  
- Risk: Mermaid parse errors → Mitigation: Use validated templates + Mermaid Live Editor links in README.  
- Risk: Skill overload → Mitigation: Strict progressive disclosure + metadata-only initial scan.

## 6. Revision History

- v1.0 – Jan 21, 2026 – Initial template PRD (Shawn)
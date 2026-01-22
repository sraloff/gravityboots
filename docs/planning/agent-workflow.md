# Agent Workflow
**Version:** 1.0  
**Last Updated:** January 22, 2026  
**Owner:** Shawn (@sraloff) – Portland, OR
**Description:** This is the canonical step-by-step process the agent must follow for every interaction.

## Visual Flowchart
flowchart TB
    A[User Prompt] --> B{Agent Clarifies Understanding + Recommends Prompt Updates}

    B --> C{Is this a new project or existing / ongoing?}
    
    C -->|New / Init / Bootstrap / Start| NewPath[Run project-init skill\nCreate structure, memory.json, stubs, first commit]
    C -->|Existing / Add feature / Fix / Refactor| ExistingPath[Read memory.json first\nLoad relevant skills based on prompt + open files]

    NewPath --> D[Load Memory + Planning Skills + PRD Summary]
    ExistingPath --> D

    D --> E{User Approves Prompt / Intent?}
    E -->|Yes| F[Create Granular Plan\n• Suggested skills per task\n• Memory.json updates if needed]
    E -->|No / Revise| G[Ask Clarifying Questions or Revise Prompt]
    G --> E

    F --> P1{User Approves Plan?}
    P1 -->|Yes| Exec[Begin Executing Tasks]
    P1 -->|No / Revise| P2[Ask Clarifying Questions or Revise Plan]
    P2 --> P1

    Exec --> T1[Test Task Output]
    T1 --> S{Test Success?}
    S -->|Yes| Lint{Lint & Validation Clean?}
    S -->|No| Fix[Fix Issues]
    Lint -->|Yes| Mark[Mark Task Complete in current-plan.md]
    Lint -->|No| Fix
    Fix --> T1
    Fix --> P3{User Approval Needed?}
    P3 -->|Yes| P4[Ask Clarifying Questions or Revise]
    P3 -->|No| T1
    P4 --> P3

    Mark --> Git[Git Operations: pull, Conventional Commit, safe push]
    Git --> Done[Update Changelog / Memory / Docs\nAlert User / Loop to Next Item]

    Done --> End[Task Complete\nLoop to Next Item or End]

    %% Styling
    classDef decision fill:#bbf,stroke:#333,stroke-width:2px
    classDef action fill:#dfd,stroke:#333
    class C,E,P1,S,Lint,P3,P4 decision
    class B,D,F,Exec,T1,Fix,P2,P4,Done,NewPath,ExistingPath,Mark,Git action

## Natural Language Summary
1. User gives prompt
2. Agent reads AGENTS.md + memory.json
3. Agent clarifies understanding and recommends prompt improvements
4. User approves or revises prompt (loop until approved)
5. Agent checks: new project or existing?
   - New → run project-init skill (create folders, git, stubs, memory.json)
   - Existing → read memory.json + load relevant skills from manifest
6. Load core context: memory.json + core-always-on + planning skills
7. Agent creates granular plan (tasks, suggested skills, MCP if needed, memory updates)
8. User approves plan (loop until approved)
9. Begin execution: load task-specific skills + MCP if needed
10. Test task output
11. Lint & validation check (auto-fix safe issues, ask for risky)
12. Fix issues (loop back to test/lint)
13. Mark task complete in current-plan.md (- [ ] → - [x])
14. Git operations: pull → Conventional Commit → safe push
15. Update changelog, memory.json, docs
16. Alert user: "Task complete. Next item or new prompt?"
17. Loop to next plan item or wait
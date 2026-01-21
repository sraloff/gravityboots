# Technical Specifications  
**Project:** [Project Name]  
**Version:** 1.0  
**Last Updated:** [Date]

## Architecture Overview
- Backend options: PHP (Laravel/Symfony), Python (FastAPI/Django/Flask)
- Frontend: Next.js (App Router), React Native (optional)
- Database: PostgreSQL (primary), MySQL/MariaDB (legacy/LAMP)
- Infra: Docker, Caddy/Apache, Redis (caching/queues)
- Deployment: Vercel (frontend), self-hosted or Railway/Fly.io (backend)

## Key Technical Choices
- Language standards:
  - PHP: PSR-12, strict_types=1
  - Python: 3.12+, type hints, Pydantic
  - JS/TS: ES2025+, modules, no var
- Git: Conventional Commits, rebase preferred
- Security: CSP headers, input validation, least privilege
- Performance: Indexes on frequent queries, lazy loading, Redis cache

## Non-Functional Requirements
- Response time: < 500ms for agent actions
- Uptime target: 99.9% (for deployed apps)
- Accessibility: WCAG 2.1 AA where applicable

Last Updated: [Date]
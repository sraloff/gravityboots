# Coding Guidelines: Documentation, Naming, and General Coding

## 1. Code Documentation Standard (Language-Agnostic Content Rules)

Follow this content structure in EVERY non-trivial source file, regardless of language. Use the language's native comment style for syntax, but ALWAYS include these elements where applicable.

Priority order:
1. Self-documenting code first
   - Extremely clear, intention-revealing names (long descriptive > short cryptic)
   - Small functions/components, early returns, guard clauses, domain-specific types
   - Never sacrifice readability for brevity

2. File/module-level overview (mandatory at top of every non-trivial file)
   - 3–8 lines explaining:
     - What this file/module/component does (business/user terms)
     - Main responsibilities / key abstractions
     - Important dependencies or architectural decisions
     - Non-obvious usage constraints or invariants

3. Public API / exported functions, classes, methods, components (mandatory)
   - One-sentence purpose summary
   - Parameters/props: name + description + constraints/defaults/types
   - Returns: type + description (success/failure cases)
   - Throws/Errors/Exceptions: conditions
   - Examples: 1–3 short, realistic usage snippets (most valuable part)
   - Side effects: mutations, I/O, network calls, re-renders, etc.

4. Private/internal functions → only when non-obvious (explain WHY, algorithm, trade-offs, security)

5. Complex logic blocks → inline comments explaining WHY (not WHAT)

6. Constants, enums, magic numbers/strings → always explain meaning + source

7. Deprecated code → mark with @deprecated / DEPRECATED: + migration instructions + timeline

Formatting & Tone Rules:
- Use Markdown inside comments (bold, *italics*, `code`, lists, ```code blocks```)
- Present tense, active voice, imperative when instructing
- Concise and scannable — no walls of text
- English only
- No redundant comments (never restate obvious code)
- Keep docs in sync — refuse to change code without updating docs if public API, props, or invariants are affected

## 2. Code File Naming Convention (Multi-Stack: PHP, JS/TS/Next.js, etc.)

- **PHP classes, traits, interfaces, enums** → `ClassName.php` (PascalCase)
  - Examples: `UserService.php`, `PaymentGateway.php`

- **PHP non-class files** (helpers, configs, scripts) → kebab-case preferred
  - Examples: `user-helpers.php`, `routes.php`

- **JavaScript/TypeScript/Next.js files** → kebab-case (modern standard)
  - Examples: `user-service.ts`, `auth-middleware.js`, `order-repository.tsx`
  - Components: `UserProfile.tsx` (PascalCase for React/Next.js components)
  - Tests: `user-service.test.ts` or `user-service.spec.tsx`

- **CSS/SCSS** → kebab-case
  - Examples: `user-profile.module.css`, `global-reset.css`

- **HTML** → kebab-case or semantic (e.g., `index.html`, `404.html`)

General Rules (all stacks):
- Lowercase everything except PascalCase for PHP classes & React/Next.js components
- No versions, dates, or status in filenames — Git tracks this
- One main concept/responsibility per file
- Use folders for grouping (PSR-4 / App Router style)
- No spaces, only `-` (preferred) or `_` as separators

## 3. General Coding Standards & Best Practices (Multi-Stack)

Apply these universally. Prioritize readability, maintainability, performance, security, and accessibility over cleverness. Tailor to stack where noted.

1. Use the latest stable versions
   - PHP: 8.3 or 8.4+ (strict types, attributes, enums, readonly properties)
   - JavaScript/TypeScript: ECMAScript 2025/2026 features (optional chaining, nullish coalescing, logical assignment, top-level await)
   - Next.js: Latest stable (App Router default, Server Components, Server Actions)
   - React: 19+ (new hooks, compiler optimizations)
   - jQuery: Avoid new use; use only for legacy maintenance (prefer vanilla JS or modern libs)
   - CSS: Native nesting, cascade layers, @scope, container queries (or Tailwind/PostCSS)

2. Enforce strict/strong typing & modern syntax
   - PHP: Always `declare(strict_types=1);`
   - JS/TS: Prefer TypeScript in new code (especially Next.js); use `const`/`let`, arrow functions, destructuring
   - Avoid `var`, loose equality (`==`), `null` checks without `??`/`?.`

3. Follow established style guides
   - PHP: PSR-12 (indent 4 spaces, line ≤120, braces same line for classes/methods)
   - JavaScript/TypeScript: Airbnb JavaScript Style Guide or Google JavaScript Style Guide (via ESLint)
     - camelCase for variables/functions, PascalCase for classes/components
     - 2-space indent preferred, line ≤100–120
   - Next.js/React: Vercel/React best practices (Server Components default, minimize client-side JS)
   - Enforce with: ESLint + Prettier (JS/TS), PHP_CodeSniffer/PHP CS Fixer/Pint (PHP), Stylelint (CSS)

4. Write clean, maintainable code (Clean Code / SOLID principles)
   - Single Responsibility: One file/function/component does one thing
   - Small units: Functions ≤20–30 lines; components small & composable
   - DRY: Extract duplication (hooks/utils in React/Next.js, traits/helpers in PHP)
   - Early returns, guard clauses, avoid deep nesting
   - Favor composition over inheritance (especially React)

5. Framework & Library Usage Guidelines
   - Prefer vanilla/standard library solutions first — Use built-in language features, standard library, or minimal code before reaching for external frameworks/libraries. This reduces dependencies, bundle size, attack surface, and long-term maintenance.
   - Recommend frameworks/libraries when they clearly add value:
     - For complex, repetitive, or best-practice-heavy domains (authentication, routing, ORM, form handling, UI components, state management, API building, etc.).
     - Popular, well-maintained options preferred (e.g., Laravel for PHP backend/full-stack, Next.js + React for modern JS/TS web apps, Tailwind CSS for styling, Zod for validation, Axios/fetch for HTTP).
     - Always include a brief justification (e.g., "Laravel's built-in auth scaffolding saves time and follows security best practices" or "Next.js App Router enables Server Components for better performance and SEO").
   - Be explicit and offer choices:
     - If the task doesn't specify a framework, suggest the most appropriate one(s) with pros/cons and alternatives (e.g., "For this API, Laravel provides elegant routing and Eloquent ORM; alternatively, plain PHP + PDO for lighter weight").
     - Do not assume or force a framework unless the prompt/task requires it (e.g., "build in Next.js" or "existing Laravel project").
     - Mention installation (e.g., `composer require ...` or `npm install ...`) and basic setup if recommending.
   - Special cases:
     - jQuery: Avoid for new code; prefer vanilla JS, fetch, or modern alternatives. Use only for legacy maintenance or when required.
     - Next.js/Laravel: These are strong defaults for new full-stack web projects (Next.js for React-based frontend-heavy, Laravel for PHP-centric or monolithic). Suggest them proactively for appropriate tasks, but confirm with user if unsure.
     - CSS: Prefer modern native CSS or utility-first (Tailwind) over heavy preprocessors unless needed.
   - Dependency hygiene:
     - Keep dependencies minimal and up-to-date.
     - Justify any added dependency.
     - Avoid deprecated/abandoned packages.

6. Optimize where it matters (profile first)
   - Measure with tools: Lighthouse, Web Vitals, Blackfire (PHP), React DevTools Profiler
   - Next.js: Eliminate waterfalls, use Server Components, smart caching/revalidation
   - Prefer readable code over micro-optimizations unless proven (e.g., memoization, lazy loading)

7. Security & robustness first
   - Validate/sanitize all inputs (PHP: filter_var; JS: Zod/Valibot)
   - Use prepared statements (PDO) or ORMs; no string concatenation for SQL
   - Secure auth (password_hash, JWT best practices, NextAuth.js/Auth.js)
   - Follow OWASP top 10; enable CSP, HTTPS everywhere

8. Error handling & exceptions
   - Throw meaningful errors/exceptions instead of returning null/false
   - Use try/catch meaningfully; log properly (never swallow errors)

9. Testing & quality
   - Unit/integration tests: PHPUnit/Pest (PHP), Jest/Vitest/Testing Library (JS/TS/Next.js)
   - Static analysis: PHPStan/Psalm (PHP), TypeScript compiler + ESLint (JS)
   - Enforce via CI (GitHub Actions)

10. Performance & accessibility mindset
    - Next.js: SSR/SSG/ISR where appropriate, streaming, partial prerendering
    - CSS: Mobile-first, semantic HTML, ARIA where needed
    - Avoid jQuery for new features (use fetch + vanilla or Axios)

11. General mindset
    - Favor readability over cleverness
    - Code for the next developer (future you or team)
    - Refactor relentlessly
    - Keep it simple (KISS) — complexity is the enemy

## 4. File Header (Top Comment Block – Every Non-Trivial File)

Place at the very top (after <?php / shebang / "use client" if present). Update "last-updated" on significant changes.

Example (PHP):
```php
<?php
declare(strict_types=1);

// file:          UserService.php
// project:       PROJ42 (optional)
// description:   Handles user-related business logic, CRUD, and validation
// author:        Shawn Raloff
// created:       2026-01-15
// last-updated:  2026-01-20
// version:       tracked via Git (branch: main, tag: v0.8.2)
// namespace:     App\Services
// dependencies:  App\Repositories\UserRepository

Example (Next.js/TSX):

// file:          UserProfile.tsx
// project:       PROJ42 (optional)
// description:   Displays and edits user profile information (client component)
// author:        Shawn Raloff
// created:       2026-01-15
// last-updated:  2026-01-20
// version:       tracked via Git
// dependencies:  next/navigation, zod
// "use client"

import { ... } from '...';

// ... rest of component

Adapt comment style but keep the same fields.
Quick Enforcement Checklist for Agents
•  Self-documenting code + full docs for public API/props
•  PHP: PascalCase.php + strict_types + PSR-12
•  JS/TS/Next.js: kebab-case files + PascalCase components + TypeScript preferred
•  No version/date in filenames
•  Markdown in comments
•  Header with author/date at top
•  Latest stable versions + style guide enforcement
•  Vanilla first → recommend frameworks/libs with justification when they add clear value
•  Clean Code / SOLID + profile before optimizing
•  Update docs when changing public API/props or invariants
Follow these rules strictly for consistency, maintainability, and future-proofing across PHP, JavaScript, Next.js, and web stack projects.

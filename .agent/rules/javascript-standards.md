---
description: Coding standards for JavaScript, TypeScript, and Next.js.
globs: "**/*.{js,ts,jsx,tsx}"
---

# JavaScript & Next.js Standards

## 1. Core JS/TS
*   **Version**: ES2025/2026 features (optional chaining `?.`, nullish coalescing `??`, top-level await).
*   **Typing**: Prefer TypeScript for all new code.
*   **Syntax**: `const`/`let` (no `var`), arrow functions, destructuring.
*   **Linting**: ESLint + Prettier.

## 2. Next.js (App Router)
*   **Components**: Prefer Server Components by default. Use `use client` only when interactivity is needed.
*   **Data Fetching**: Use built-in caching (`fetch` with `cache/revalidate`) and `revalidatePath`.
*   **Performance**: Eliminate waterfalls, use streaming `<Suspense>`, optimize images.

## 3. React Best Practices
*   **Hooks**: Use standard hooks (`useState`, `useEffect`) and custom hooks for logic extraction.
*   **Composition**: Favor composition over inheritance.
*   **Keys**: Use stable, unique IDs for lists (no array index).

## 4. Testing & Tooling
*   **Tests**: Jest / Vitest / React Testing Library.
*   **Validation**: Zod / Valibot for runtime validation.

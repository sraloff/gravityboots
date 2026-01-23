---
description: General coding practices, security, and principles applicable to all stacks.
globs: "**/*"
always_on: true
---

# General Development Practices

## 1. Clean Code Principles
*   **SOLID**: Adhere to Single Responsibility, Open/Closed, etc.
*   **DRY**: Extract duplication into helpers/hooks/traits.
*   **KISS**: Avoid over-engineering. Code for the next developer.
*   **Composition**: Favor composition over inheritance.

## 2. Dependencies
*   **Minimalism**: Prefer standard library/vanilla solutions first.
*   **Justification**: Add frameworks/libs only when they clearly add value (e.g., Auth, ORM).
*   **Hygiene**: Keep dependencies up-to-date. Avoid abandoned packages.

## 3. Security
*   **Validation**: Validate/sanitize ALL inputs.
*   **Auth**: Secure authentication flows (OWASP).
*   **Least Privilege**: Grant minimum necessary permissions.
*   **Secrets**: Never commit secrets to Git.

## 4. Performance
*   **Measure First**: Profile before optimizing (Lighthouse, Blackfire, Profiler).
*   **Frontend**: Optimize implementation (images, fonts, bundles).
*   **Backend**: Optimize queries (N+1), use caching (Redis).

## 5. Error Handling
*   Throw meaningful exceptions types.
*   Never swallow errors silently.
*   Use `try/catch` blocks around unstable code.

---
description: Naming conventions for files, classes, and variables across stacks.
globs: "**/*"
---

# Naming Conventions

## 1. File Naming
*   **PHP Classes/Interfaces**: `PascalCase.php` (e.g., `UserService.php`).
*   **PHP Helpers/Scripts**: `kebab-case` (e.g., `user-helpers.php`).
*   **JS/TS Files**: `kebab-case` (e.g., `user-service.ts`, `auth-middleware.js`).
*   **React/Next.js Components**: `PascalCase.tsx` (e.g., `UserProfile.tsx`).
*   **CSS/SCSS**: `kebab-case` (e.g., `user-profile.module.css`).
*   **HTML**: `kebab-case` (e.g., `index.html`).

## 2. General Rules
*   One main concept/responsibility per file.
*   No versions, dates, or status in filenames.
*   Use folders for grouping (PSR-4 / App Router).
*   Use `-` (hyphen) as separator for kebab-case.

## 3. Identifiers
*   **Variables/Functions (JS/PHP)**: `camelCase`.
*   **Classes/Components**: `PascalCase`.
*   **Constants**: `UPPER_SNAKE_CASE`.
*   **Booleans**: Question-like (e.g., `isActive`, `hasPermission`).

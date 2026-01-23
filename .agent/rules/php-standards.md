---
description: Coding standards and best practices for PHP development.
globs: "**/*.php"
---

# PHP Standards

## 1. Core Standards
*   **Version**: PHP 8.3 or 8.4+.
*   **Typing**: ALWAYS `declare(strict_types=1);` at the top of every file.
*   **Style**: PSR-12 compliant (4 space indent, line <= 120 chars).
*   **Syntax**: Use attributes, enums, and readonly properties where applicable.

## 2. Frameworks (Laravel)
*   **Eloquent**: Prefer relationships over raw SQL for readability.
*   **Validation**: Prefer Form Requests over controller validation.
*   **Routing**: Use intent-revealing route names.
*   **Architecture**: Keep controllers thin; move logic to Services or Actions.

## 3. Tools
*   **Linting**: PHP_CodeSniffer / PHP CS Fixer / Laravel Pint.
*   **Static Analysis**: PHPStan / Psalm.
*   **Testing**: PHPUnit / Pest.

## 4. Security
*   Use prepared statements (PDO/ORM) - NO string concatenation for SQL.
*   Sanitize inputs (`filter_var`) if not using framework validation.
*   Use `password_hash` for credentials.

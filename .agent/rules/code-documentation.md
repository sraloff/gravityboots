---
description: Standards for code documentation, comments, and file headers.
globs: "**/*"
always_on: true
---

# Code Documentation Standards

## 1. Documentation Priority
Follow this content structure in EVERY non-trivial source file.

1.  **Self-documenting code first**: Clear names, small functions, guard clauses.
2.  **File/module-level overview**: Mandatory 3-8 lines at top explaining logic, dependencies, and constraints.
3.  **Public API**: Summary, parameters, returns, errors, and examples for all exported members.
4.  **Internal functions**: Explain WHY, not WHAT.
5.  **Complex logic**: Inline comments explaining trade-offs.
6.  **Constants/Magic Numbers**: Explain meaning and source.
7.  **Deprecated code**: Mark with `@deprecated` + migration instructions.

## 2. Formatting & Tone
*   Use Markdown in comments.
*   Present tense, active voice.
*   Concise, English only.
*   Keep docs in sync with code.

## 3. File Header (Top Comment Block)
Place at the very top of every non-trivial file. Update `last-updated` on changes.

### PHP Example
```php
<?php
declare(strict_types=1);

// file:          UserService.php
/* project:       PROJ42
- Description:   Handles user-related business logic, CRUD, and validation
- Author:        Shawn Raloff
- Created:       2026-01-15
- Last-updated:  2026-01-20
- Version:       tracked via Git
- Namespace:     App\Services
- Dependencies:  App\Repositories\UserRepository
*/
```

### Next.js/TSX Example
```tsx
// file:          UserProfile.tsx
/**
 * Project:       PROJ42
 * Description:   Displays and edits user profile information (client component)
 * Author:        Shawn Raloff
 * Created:       2026-01-15
 * Last-updated:  2026-01-20
 * Dependencies:  next/navigation, zod
 */
"use client"

import { ... } from '...';
```

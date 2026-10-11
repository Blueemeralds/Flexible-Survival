# Personal version

Working branch: `personal-version`.

The user can request changes in ordinary language. Repository instructions live in `AGENTS.md`; agents maintain the policy, implementation, validation, and history.

## Current state

- The original game source is unchanged.
- No creatures, NPCs, events, forms, or mechanics have been selected for removal or modification.
- `content-policy.json` records design decisions. It is not loaded by Inform and is not yet an enforced filter.
- The source map and legacy build requirements have been inspected. A baseline compile and gameplay test have not yet been performed.

## Files

- `content-policy.json`: explicit content decisions; initially empty.
- `SOURCE-MAP.md`: entry points and known filtering limitations.
- `BUILD.md`: toolchain requirements and current validation status.
- `CHANGELOG.md`: implemented changes and their verification.

Future policy entries should identify the canonical source name, scope, user request, and any quest/progression dependency. Record new creature or mechanics designs here only after the user requests them. Do not infer preferences from sample instructions.

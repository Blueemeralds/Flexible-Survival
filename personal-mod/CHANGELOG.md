# Personal version changelog

## 2026-10-11 — Filter comparison correction (revision 3, retry pending)

- The user's revision-2 compile advanced past the previous conditions and reported one error: `case insensitively, decide yes` was parsed as an unrecognized instruction.
- Put the case-insensitive comparison and `decide yes` on separate lines in the exclusion predicate. This is the only gameplay edit relative to revision 2; the 71 names and all other extension contents are unchanged.
- Validation: reproduced the revision-2 error with Linux NI 6M62; corrected helper compiled through NI and Inform 6 v6.33 and passed five dumb-glulxe runtime checks (exact/mixed-case names, unlisted variants, retained duplicate weights, empty filtered pool). Added `verify-filter.py` to repeat those tests against the real helper. Source comparison, 71-name consistency and whitespace checks passed. A separate full-game attempt using stock Linux NI 6M62 (8 GiB address-space limit, default 8 MiB stack) crashed with signal 11 after 233.45 seconds while processing extensions. No complete game was produced; full compilation and scripted-scene checks remain pending.

## 2026-10-11 — Compile-condition correction (retry pending)

- The user's first exclusion build failed Inform 7 6M62 translation. The screenshot reported unrecognized negative custom conditions and ambiguous combined conditions in Body Shop guarantees and Dominick's forced transformation rules.
- Replaced every `is not personally excluded` call with standard `unless` applied to the positive predicate. Kept existing Body Shop, Dominick, Nermine and Latex Mistress conditions separate from the added exclusion check; separated the player-only helper guard too.
- Compared the seven affected extensions to the first update: their underlying statements and quoted source text are unchanged after accounting for the condition rewrite. All 71 policy/runtime names are unchanged; whitespace review passed.
- Delivered a complete revision 2 package with all 14 extensions. Full compilation/runtime testing still require the user's working toolchain. An attempted download of the official archived Linux 6M62 compiler failed with HTTP 502.

## 2026-10-11 — 71 roaming/form exclusions (compile pending)

- Recorded all 71 uploaded entries, normalizing Dalmatian Bitch, Sphinx and Skunk Female.
- Added a fixed filter for roaming combat and hunting, separate from ban/ward/import state; kept named scripted challenges and situations.
- Guarded shared infection/shifting/full-transformation functions and direct mutations in Wyatt, Dominick, Leonard, hospital, Latex Mistress and Body Shop.
- Preserved vial collection and quest uses; blocked excluded drinking and purchases before consumption/payment. Filtered random infection selection with a bounded search.
- Preserved definitions, include order, dialogue, named challenges, progression state and rewards. Related quest loot has existing retained alternatives.
- Prepared complete updated extensions and a Windows installer that backs up each affected installed file.
- Validation: policy/name consistency, source preservation comparisons, direct mutation/dependency review and `git diff --check`. No modified-game compile, runtime test or Windows installer execution was possible here. Scene narration and form-dependent prerequisites remain as documented in `EXCLUSIONS.md`.

## 2026-10-11 — Project setup

- Added repository instructions to preserve unrelated behavior and handle plain-language change requests.
- Added an empty content policy, a source map, and legacy build requirements.
- Inspected the existing ban system and identified scripted-combat and import paths needing attention for future filters.
- Game source and runtime behavior remain unchanged. Policy enforcement is not implemented.
- Validation: policy JSON parsing, documented path checks, and whitespace/diff review. No game compilation or runtime test performed; compatible compiler setup is outstanding.

# Personal version

Working branch: `personal-version`.

The user requests changes in ordinary language. Repository instructions live in `AGENTS.md`.

## Current state

- The user's Windows installation successfully compiled the unchanged full game after applying the community compiler replacement.
- The 71 listed strains are excluded from roaming encounters and hunting. New player transformations into those strains are blocked, including applications inside retained scripts.
- Named scripted challenges, situations, NPC definitions, dialogue, quest state changes and rewards remain in the source. No creature extension has been removed.
- Existing imported body parts are preserved. The fixed exclusions are separate from the saved ban/ward lists.
- The modified build has **not been compiled or runtime-tested**. Source inspection is not proof of playable behavior.

## Files

- `content-policy.json`: exact requested names, canonical names and scope; documentation, not an Inform input.
- `EXCLUSIONS.md`: implementation, limits, quest dependencies and focused gameplay checks.
- `BUILD.md`: compatible toolchain and current validation status.
- `CHANGELOG.md`: changes and checks.
- `SOURCE-MAP.md`: entry points and baseline filtering limitations.
- `Install-Update.cmd` and `update-files.txt`: Windows installation with backups, intended to ship beside the ZIP's `Extensions` folder.

Only change the explicit requested scope. Preserve unrelated variants and mechanics.

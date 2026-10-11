# Personal Flexible Survival fork

This repository is Blueemeralds' personal version of Flexible Survival. The user gives plain-language design requests; the agent handles investigation, implementation, validation, documentation, and commits.

## Scope and preservation

- Preserve all unrelated gameplay, content, commands, plots, and mechanics. Make only the requested changes and fixes needed for those changes.
- Never treat examples from a conversation as an actual removal request. The explicit exclusion scope is recorded in personal-mod/content-policy.json; scripted encounters are retained.
- Use `personal-version` for personal work. Do not modify Nuku's upstream repository or submit upstream changes unless requested.
- Read `personal-mod/README.md`, `personal-mod/content-policy.json`, and `personal-mod/CHANGELOG.md` before making changes. Record explicit user decisions there.
- Make routine technical decisions autonomously. Ask only for design ambiguity that materially changes the result, missing account access, or a necessary user-owned file.
- Search the whole repository for dependencies before removing, replacing, or blocking anything. Prefer retaining definitions and suppressing access when deleting would break references.
- "Never encounter" must cover random exploration, hunting, challenges, scripted quest fights, and related events. Inspect every relevant path; the built-in ban flag is not proof of complete exclusion.
- Creature encounter access, infection availability, shifting access, NPC interactions, and quest availability are separate design choices. Do not silently broaden a request to remove all of them.
- Preserve progression rewards when a blocked encounter is required by a retained quest; document any necessary replacement or alternate path.
- Preserve the `Inform/story.ni` core include order. Do not edit `MinimalBuild/` copies unless the requested work actually concerns that separate build.

## Validation and delivery

- Establish an unmodified baseline build with the compatible compiler before promising playable changes. Follow `personal-mod/BUILD.md`; do not assume modern Inform is compatible.
- Compile after gameplay edits, repair errors introduced by the change, and run focused gameplay checks for the changed paths. For encounter changes also check retained encounters, empty encounter pools, and export/import behavior.
- Treat text searches and compilation as separate from runtime testing. Report exactly what was run and any remaining build or test blocker.
- Do not promise binary save compatibility across recompilation. Preserve and verify the game's export/import workflow where applicable.
- Use small, reversible commits. Commit and push completed, validated work to the personal branch; never force-push over user work. If a change is unverified, clearly label it as such and do not call it ready to play.
- Update the policy and changelog with each implemented design change. The JSON policy is documentation; verify its Inform implementation and report pending compilation or runtime checks.
- Prefer a complete playable game artifact when a build is available. Do not require the user to copy source snippets manually.

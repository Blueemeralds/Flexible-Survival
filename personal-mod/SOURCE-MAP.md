# Source map

Inspected baseline: `76216c2b75368e44f531d844fb33cc43a0487f7d`.

| System | Entry points |
| --- | --- |
| Full game entry and extension load order | `Inform/story.ni` |
| Shared monster, item, and export tables | `Core Mechanics/GameTables.i7x` |
| Ban/ward categories and player settings | `Core Mechanics/Lists and Banning.i7x` |
| Startup and applying category bans | `Core Mechanics/Game Start.i7x`, especially `startcreatureban` |
| Hunting and exploration | `Core Mechanics/Hunting and Exploration.i7x` |
| Encounter choice and challenge entry | `Core Mechanics/Fighting.i7x` |
| Combat execution | `Core Mechanics/Alt Combat.i7x` |
| Infection application and monster selection | `Core Mechanics/Infections.i7x` |
| Infection vial access | `Core Mechanics/Infection Vials.i7x` |
| Shifting and its unlock events | `Hellerhound/Shifting.i7x`, `Hellerhound/Qytat shifters.i7x`, `SgtPepper234/Qytat a'th Lundrues.i7x` |
| Progression and feats | `Core Mechanics/Leveling.i7x`, `Core Mechanics/Feats.i7x` |
| Inventory and survival | `Core Mechanics/Inventory.i7x`, `Core Mechanics/Time.i7x`, `Core Mechanics/Rest.i7x`, `Core Mechanics/Scavenging.i7x` |
| Cross-version export/import | `Core Mechanics/Story Skipper.i7x`, `Core Mechanics/Story Skipper Loose Variables.i7x` |
| Individual creatures, NPCs, quests | Author folders, with includes in `Inform/story.ni` |
| Artwork | `Figures/`, with declarations in `Core Mechanics/FS Graphics.i7x` |
| Separate minimal project | `Inform/MinimalBuild.ni`, `MinimalBuild/`; not a substitute for testing the full game |

## Why a ban flag alone is insufficient

The monster table has `BannedStatus`. Ordinary hunting and combat selection check it, but combat checks can be bypassed when `inasituation` is true. Some special encounters are added separately to encounter pools before ordinary filtering. Scripted content can also invoke a creature's descriptive or scene phrases directly.

`startcreatureban` applies categories, rather than an arbitrary personal creature list. It disables related situations using their category registrations. It does not establish that every mention or scripted interaction is unreachable.

`Core Mechanics/Story Skipper.i7x` resets creature ban state during import and subsequently reapplies category settings through `BanListRestore`. Any personal enforcement must account for startup and post-import state.

For each future removal, search canonical names, aliases, scene phrases, table entries, `challenge`/`setmonster` calls, infection/vial sources, shifting references, quest rewards, and graphics. Verify the actual requested scope, including retained quest progression and the case where an area has no remaining encounters.

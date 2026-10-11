# Build requirements and status

## Current status

The user reported a successful baseline compile on Windows on 2026-10-11, after installing the extensions and copying the community replacement compiler files into Inform 7's `Compilers` folder. The Discord attachment was named `6L02.zip`, posted 2025-02-03. Its contents and exact compiler versions were not inspected here; the filename is not evidence of a version.

The first exclusion package failed NI translation on the user's Inform 7 6M62 installation; the Problems screenshot identified custom-condition negation and compound-condition parsing errors. Revision 2 rewrites those conditions and awaits a fresh compile. The revised build has **not been compiled or runtime-tested**. This workspace has no compatible Inform compiler or Wine. A fresh download attempt from the official Linux 6M62 archive returned HTTP 502. The delivered update must be compiled with the user's working installation before it is considered playable.

## Required project layout

`CONTRIBUTING.md` specifies **Inform 7 6M62 Win64 beta 4 or beta 5**, with the community compiler fixes. Preserve the user's now-working toolchain.

- `Flexible Survival.inform/Source/story.ni` comes from `Inform/story.ni`.
- Extension author folders go under the external `Documents/Inform/Extensions` folder.
- `Flexible Survival.materials/Figures` comes from `Figures/`.

The exclusion update changes 14 extensions. The main story, figures and compiler files need no replacement for this update. Close Inform, extract the ZIP, run `Install-Update.cmd`, reopen the existing project and use **Release** to rebuild.

The installer backs up the 14 installed extensions before changing any of them. It requires all 14 to already be installed, and attempts to restore them if a copy fails. It does not alter projects, compiler files or saved games. The installer has been inspected but cannot be executed on Windows in this workspace.

## Verification still required locally

Compile the complete updated game and record any compiler errors. Then run the focused checks in `EXCLUSIONS.md` using a disposable character. Test both a new game and the game's character export/import workflow. Ordinary interpreter saves are not guaranteed to transfer across rebuilt story files.

`release.bat` documents NI, Inform 6 and cBlorb stages, but also elevates privileges, creates a symlink and copies into an installed game. Do not run it blindly against the user's working installation.

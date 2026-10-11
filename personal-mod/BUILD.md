# Build requirements and status

## Current status

Source inspection only. No baseline `.ulx` or `.gblorb` has been compiled or runtime-tested in this workspace. No Inform compiler was found on the initial PATH check. There is no build workflow in the baseline `.github` directory.

## Requirements documented by the repository

`CONTRIBUTING.md` specifies **Inform7 6M62 Win64 beta 4 or beta 5** and warns that other versions are incompatible. It also references additional compiler fixes dated 2025-02-03 in a Discord pin; their exact contents have not been retrieved or verified. Do not replace that requirement with a guessed modern toolchain.

The contribution guide describes this project layout:

- `Flexible Survival.inform/Source/story.ni` from `Inform/story.ni`.
- Author and core extension folders under the external Inform `Extensions` directory.
- `Flexible Survival.materials/Figures` from `Figures/`.

`release.bat` documents three compiler stages:

1. `ni64.exe -release -internal <internal> -project <project> -external <external> -format=ulx`
2. `inform6.exe -w~S~DG <project>/Build/auto.inf <project>/Build/output.ulx`
3. `cBlorb.exe -windows <project>/Release.blurb <project>/Build/output.gblorb`

The batch file also requests administrator privileges, creates a symlink, backs up an existing source file, and copies the result into an installed game's directory. Do not run it blindly against the user's installation. Prepare an isolated build workspace and preserve existing sources and saves.

## Next build work

Identify and obtain the compatible compiler and documented patches; determine whether a compatible build can run in this environment; stage an isolated project; compile the unchanged full game and capture tool versions, exit codes, and logs. Then automate those verified stages and add an interpreter-based smoke test. If an essential dependency is unavailable, report that specific blocker without claiming a successful build.

When gameplay changes are ready, test a new game plus export/import of a disposable character. Ordinary interpreter saves are not guaranteed to transfer across rebuilt story files.

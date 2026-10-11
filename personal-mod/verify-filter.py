#!/usr/bin/env python3
"""Compile and exercise the actual exclusion helper with Inform 7 6M62.

Usage: python personal-mod/verify-filter.py --inform-root /path/to/share/inform7
The optional --output-dir retains the generated test project and compiler logs.
This is a focused filter test, not a full-game build or scripted-scene test.
"""
import argparse
import json
from pathlib import Path
import re
import subprocess
import tempfile

TEST_BODY = """
	if "Tiger" is personally excluded:
		say "PASS exact blocked name[line break]";
	else:
		say "FAIL exact blocked name[line break]";
	if "tIgEr" is personally excluded:
		say "PASS mixed case blocked name[line break]";
	else:
		say "FAIL mixed case blocked name[line break]";
	unless "Tiger Cop" is personally excluded:
		say "PASS unlisted variant allowed[line break]";
	else:
		say "FAIL unlisted variant allowed[line break]";
	let Candidates be a list of text;
	add "Tiger" to Candidates;
	add "Human" to Candidates;
	add "Breederslut" to Candidates;
	add "Human" to Candidates;
	let Filtered be PersonalEncounterPool Candidates;
	if the number of entries in Filtered is 2:
		if entry 1 of Filtered is "Human" and entry 2 of Filtered is "Human":
			say "PASS blocked entries removed and retained weights preserved[line break]";
		else:
			say "FAIL retained weights[line break]";
	else:
		say "FAIL filtered pool count[line break]";
	let BlockedCandidates be a list of text;
	add "Tiger" to BlockedCandidates;
	add "Breederslut" to BlockedCandidates;
	let EmptyPool be PersonalEncounterPool BlockedCandidates;
	if EmptyPool is empty:
		say "PASS fully excluded pool is empty[line break]";
	else:
		say "FAIL fully excluded pool[line break]".
"""


def verify(inform_root, work):
    repo = Path(__file__).resolve().parent.parent
    source = (repo / "Core Mechanics/Lists and Banning.i7x").read_text()
    helper = source.split("Section 5 - Personal Form and Roaming Encounter Exclusions", 1)[1].split("Lists and Banning ends here.", 1)[0]
    policy = json.loads((repo / "personal-mod/content-policy.json").read_text())
    names = re.findall(r'"([^"]+)"', re.search(r'PersonalExcludedForms is \{(.*?)\}\.', helper, re.S).group(1))
    if names != policy["blocked_forms"]:
        raise RuntimeError("Inform list and policy names differ")
    project = work / "filter.inform"
    (project / "Source").mkdir(parents=True, exist_ok=True)
    (project / "Build").mkdir(exist_ok=True)
    external = work / "external"
    (external / "Extensions").mkdir(parents=True, exist_ok=True)
    story = '"Exclusion Filter Verification" by "Personal Mod"\n\nThe Test Room is a room.\n' + helper + "\nWhen play begins:" + TEST_BODY
    (project / "Source/story.ni").write_text(story)
    compilers = inform_root / "Compilers"
    ni = compilers / "ni"
    i6 = compilers / "inform6"
    interpreter = inform_root / "Interpreters/dumb-glulxe"
    stages = [
        ("ni", [str(ni), "-internal", str(inform_root / "Internal"), "-external", str(external), "-project", str(project), "-format=ulx", "-release"], None),
        ("i6", [str(i6), "-w~S~DG", str(project / "Build/auto.inf"), str(project / "Build/output.ulx")], None),
        ("runtime", [str(interpreter), str(project / "Build/output.ulx")], "quit\ny\n"),
    ]
    for name, args, stdin in stages:
        result = subprocess.run(args, input=stdin, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, timeout=120)
        (work / (name + ".log")).write_text(result.stdout)
        if result.returncode != 0:
            raise RuntimeError(f"{name} failed ({result.returncode}):\n{result.stdout}")
        if name == "runtime":
            if "FAIL" in result.stdout or result.stdout.count("PASS ") != 5:
                raise RuntimeError("Runtime assertions failed:\n" + result.stdout)
            print(result.stdout)
    print(f"Verified policy consistency for {len(names)} forms and five runtime checks.")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--inform-root", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path)
    args = parser.parse_args()
    if args.output_dir:
        args.output_dir.mkdir(parents=True, exist_ok=True)
        verify(args.inform_root.resolve(), args.output_dir.resolve())
    else:
        with tempfile.TemporaryDirectory(prefix="fs-filter-check-") as temporary:
            verify(args.inform_root.resolve(), Path(temporary))


if __name__ == "__main__":
    main()

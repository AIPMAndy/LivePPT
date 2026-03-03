#!/usr/bin/env python3

import subprocess
import sys
import tempfile
from pathlib import Path
import re


REQUIRED_FILES = [
    "SKILL.md",
    "README.md",
    "ROADMAP.md",
    "CONTRIBUTING.md",
    "LICENSE",
    "scripts/add_theme.py",
    "scripts/generate_showcase_plan.py",
    "scripts/generate_release_note.py",
    "references/design-system-playbook.md",
    "references/style-presets.md",
    "assets/templates/scene-map.md",
    "assets/templates/theme-spec.md",
]


def run(cmd: list[str], cwd: Path) -> None:
    subprocess.run(cmd, cwd=cwd, check=True)


def ensure_required_files(root: Path) -> None:
    missing_files = [path for path in REQUIRED_FILES if not (root / path).exists()]
    if missing_files:
        missing = "\n".join(f"- {path}" for path in missing_files)
        raise SystemExit(f"Missing required files:\n{missing}")


def smoke_test_scripts(root: Path) -> None:
    with tempfile.TemporaryDirectory(prefix="LivePPT-") as temp_dir:
        temp_path = Path(temp_dir)
        plan_output = temp_path / "plan.md"
        theme_output = temp_path / "theme.css"

        run(
            [
                sys.executable,
                "scripts/generate_showcase_plan.py",
                "--project",
                "Smoke Test",
                "--audience",
                "开发者",
                "--mode",
                "7",
                "--output",
                str(plan_output),
            ],
            root,
        )

        run(
            [
                sys.executable,
                "scripts/add_theme.py",
                "--name",
                "smoke",
                "--bg",
                "#000000",
                "--surface",
                "#111111",
                "--text",
                "#ffffff",
                "--accent",
                "#7c3aed",
                "--motion",
                "ease",
                "--output",
                str(theme_output),
            ],
            root,
        )

        run(
            [
                sys.executable,
                "scripts/generate_release_note.py",
                "--version",
                "v0.0.0-smoke",
                "--output",
                str(temp_path / "release.md"),
            ],
            root,
        )

        if not plan_output.exists() or not theme_output.exists() or not (temp_path / "release.md").exists():
            raise SystemExit("Smoke test failed: expected output files not created")


def check_doc_anti_patterns(root: Path) -> None:
    markdown_files = list(root.rglob("*.md"))
    absolute_path_pattern = re.compile(r"/Users/[^\s`]+")
    matches: list[str] = []

    for md_file in markdown_files:
        content = md_file.read_text(encoding="utf-8")
        if absolute_path_pattern.search(content):
            relative = md_file.relative_to(root)
            matches.append(str(relative))

    if matches:
        unique_files = "\n".join(f"- {path}" for path in sorted(set(matches)))
        raise SystemExit(
            "Found absolute local paths in markdown files (use relative paths instead):\n"
            f"{unique_files}"
        )


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    ensure_required_files(root)
    check_doc_anti_patterns(root)
    smoke_test_scripts(root)
    print("Validation passed: required files and script smoke tests are OK")


if __name__ == "__main__":
    main()

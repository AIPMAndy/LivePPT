#!/usr/bin/env python3

import argparse
from pathlib import Path


def build_theme(name: str, bg: str, surface: str, text: str, accent: str, motion: str) -> str:
    return "\n".join(
        [
            f':root[data-theme="{name}"] {{',
            f"  --color-bg: {bg};",
            f"  --color-surface: {surface};",
            f"  --color-text: {text};",
            f"  --color-accent: {accent};",
            f"  --motion-primary: {motion};",
            "  --radius-card: 20px;",
            "  --shadow-elevated: 0 20px 60px rgba(0, 0, 0, 0.35);",
            "}",
            "",
        ]
    )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate CSS variables for a showcase theme")
    parser.add_argument("--name", required=True, help="Theme name")
    parser.add_argument("--bg", required=True, help="Background color")
    parser.add_argument("--surface", required=True, help="Surface color")
    parser.add_argument("--text", required=True, help="Text color")
    parser.add_argument("--accent", required=True, help="Accent color")
    parser.add_argument("--motion", required=True, help="Primary motion curve")
    parser.add_argument("--output", required=True, help="Output CSS path")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    css = build_theme(args.name, args.bg, args.surface, args.text, args.accent, args.motion)
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(css, encoding="utf-8")
    print(f"Theme written to {output}")


if __name__ == "__main__":
    main()

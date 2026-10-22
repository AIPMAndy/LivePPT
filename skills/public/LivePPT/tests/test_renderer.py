"""Regression checks for the standalone HTML deck generator (stdlib only)."""

import importlib.util
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location(
    "liveppt_renderer", ROOT / "scripts" / "render_plan_to_html.py"
)
renderer = importlib.util.module_from_spec(spec)
spec.loader.exec_module(renderer)


class RendererTests(unittest.TestCase):
    def test_markdown_builds_navigable_slides(self):
        deck = renderer.build_deck(
            "# 产品发布\n\n给研发团队介绍\n\n## 问题\n\n- 现有手动流程太慢\n\n## 解决方案\n\n- 一键生成 HTML\n",
            "fallback",
            None,
            "My Brand",
            "neo-luxury",
        )
        self.assertEqual(deck["title"], "产品发布")
        self.assertEqual(len(deck["slides"]), 3)
        self.assertEqual(deck["slides"][1]["bullets"], ["现有手动流程太慢"])
        self.assertEqual(deck["slides"][2]["title"], "解决方案")

    def test_html_escapes_script_breakout_and_html_attributes(self):
        payload = '</script><script>alert("owned")</script>'
        deck = renderer.build_deck(
            "# " + payload + "\n\n## Feature\n\n- " + payload,
            "fallback",
            payload,
            payload,
            "neo-luxury",
        )
        output = renderer.render_html(deck, renderer.resolve_theme("neo-luxury"))
        self.assertNotIn(payload, output)
        self.assertIn(r"\u003c/script\u003e", output)
        self.assertIn("&lt;/script&gt;", output)
        self.assertIn(r"\u0026", renderer.render_html(
            renderer.build_deck("# Test\n\n## A\n\n- A & B", "fallback", None, "Brand", "neo-luxury"),
            renderer.resolve_theme("neo-luxury"),
        ))

    def test_accessible_navigation_contract(self):
        deck = renderer.build_deck(
            "# Demo\n\n## One\n\n- A\n\n## Two\n\n- B", "Demo", None, "LivePPT", "neo-luxury"
        )
        output = renderer.render_html(deck, renderer.resolve_theme("neo-luxury"))
        for token in (
            'aria-live="polite"',
            'aria-current=',
            "prefers-reduced-motion: reduce",
            "PageDown",
            "PageUp",
            "event.target?.closest?",
            "button:focus-visible",
        ):
            self.assertIn(token, output)

    def test_write_html_without_network_or_dependencies(self):
        with tempfile.TemporaryDirectory() as tmp:
            output_file = Path(tmp) / "index.html"
            deck = renderer.build_deck("# Demo\n\n## Next\n\n- Hello", "Demo", None, "LivePPT", "prism-command")
            output_file.write_text(
                renderer.render_html(deck, renderer.resolve_theme("prism-command")), encoding="utf-8"
            )
            self.assertGreater(output_file.stat().st_size, 1000)
            self.assertTrue(output_file.read_text(encoding="utf-8").startswith("<!doctype html>"))


if __name__ == "__main__":
    unittest.main()

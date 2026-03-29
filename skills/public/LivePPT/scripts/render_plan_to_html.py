#!/usr/bin/env python3

import argparse
import html
import json
import re
from pathlib import Path
from typing import List, Optional, Tuple


def slugify(value: str) -> str:
    value = value.strip().lower()
    value = re.sub(r"[^a-z0-9\u4e00-\u9fff]+", "-", value)
    return value.strip("-") or "section"


def extract_title(lines: List[str], fallback: str) -> Tuple[str, List[str]]:
    for index, line in enumerate(lines):
        stripped = line.strip()
        if stripped.startswith("# "):
            return stripped[2:].strip(), lines[:index] + lines[index + 1 :]
    return fallback, lines


def split_sections(lines: List[str]) -> Tuple[List[str], List[Tuple[str, List[str]]]]:
    preamble: List[str] = []
    sections: List[Tuple[str, List[str]]] = []
    current_title: Optional[str] = None
    current_lines: List[str] = []

    for raw in lines:
        line = raw.rstrip("\n")
        stripped = line.strip()
        if stripped.startswith("## "):
            if current_title is not None:
                sections.append((current_title, current_lines))
            current_title = stripped[3:].strip()
            current_lines = []
            continue

        if current_title is None:
            preamble.append(line)
        else:
            current_lines.append(line)

    if current_title is not None:
        sections.append((current_title, current_lines))

    return preamble, sections


def parse_key_value_bullet(line: str) -> Optional[Tuple[str, str]]:
    stripped = line.strip()
    if not stripped.startswith("- "):
        return None
    body = stripped[2:]
    if ":" not in body:
        return None
    key, value = body.split(":", 1)
    return key.strip(), value.strip()


def collect_intro(lines: List[str]) -> Tuple[List[dict], List[str]]:
    meta: List[dict] = []
    paragraphs: List[str] = []
    current_paragraph: List[str] = []

    def flush_paragraph() -> None:
        nonlocal current_paragraph
        if current_paragraph:
            paragraphs.append(" ".join(part.strip() for part in current_paragraph if part.strip()))
            current_paragraph = []

    for raw in lines:
        stripped = raw.strip()
        if not stripped:
            flush_paragraph()
            continue

        key_value = parse_key_value_bullet(stripped)
        if key_value:
            flush_paragraph()
            key, value = key_value
            meta.append({"key": key, "value": value})
            continue

        current_paragraph.append(stripped)

    flush_paragraph()
    return meta, paragraphs


def parse_section(title: str, lines: List[str], index: int) -> dict:
    bullets: List[str] = []
    paragraphs: List[str] = []
    tags: List[dict] = []
    current_paragraph: List[str] = []

    def flush_paragraph() -> None:
        nonlocal current_paragraph
        if current_paragraph:
            paragraphs.append(" ".join(part.strip() for part in current_paragraph if part.strip()))
            current_paragraph = []

    for raw in lines:
        stripped = raw.strip()
        if not stripped:
            flush_paragraph()
            continue

        key_value = parse_key_value_bullet(stripped)
        if key_value:
            flush_paragraph()
            key, value = key_value
            if key in {"任务", "交付", "目标受众", "主风格", "开始日期"}:
                tags.append({"key": key, "value": value})
            else:
                bullets.append(f"{key}：{value}")
            continue

        if stripped.startswith("### "):
            flush_paragraph()
            bullets.append(stripped[4:].strip())
            continue

        if stripped.startswith(("- ", "* ")):
            flush_paragraph()
            bullets.append(stripped[2:].strip())
            continue

        current_paragraph.append(stripped)

    flush_paragraph()

    slide_type = "content"
    if index == 0:
        slide_type = "cover"
    elif bullets and not paragraphs:
        slide_type = "list"
    elif title.lower() == "kpi":
        slide_type = "summary"

    nav = re.sub(r"^阶段\s*\d+[:：]\s*", "", title).strip()
    nav = nav[:10] if nav else f"第{index + 1}页"

    return {
        "id": slugify(title),
        "nav": nav,
        "title": title,
        "type": slide_type,
        "paragraphs": paragraphs,
        "bullets": bullets,
        "tags": tags,
    }


def build_deck(markdown_text: str, fallback_title: str) -> dict:
    lines = markdown_text.splitlines()
    title, remaining = extract_title(lines, fallback_title)
    preamble, sections = split_sections(remaining)
    meta, intro_paragraphs = collect_intro(preamble)

    slides: List[dict] = [
        {
            "id": "cover",
            "nav": "封面",
            "title": title,
            "type": "cover",
            "paragraphs": intro_paragraphs,
            "bullets": [],
            "tags": meta,
        }
    ]

    if sections:
        for index, (section_title, section_lines) in enumerate(sections):
            slides.append(parse_section(section_title, section_lines, index + 1))
    elif intro_paragraphs:
        slides[0]["paragraphs"] = intro_paragraphs

    return {"title": title, "slides": slides}


HTML_TEMPLATE = """<!doctype html>
<html lang=\"zh-CN\">
  <head>
    <meta charset=\"UTF-8\" />
    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\" />
    <title>{page_title}</title>
    <style>
      :root {{
        color-scheme: light;
        --bg: #f6efe5;
        --bg-strong: #fffaf2;
        --surface: rgba(255,255,255,0.78);
        --surface-strong: rgba(255,255,255,0.92);
        --line: rgba(126, 90, 48, 0.18);
        --text: #2f2217;
        --text-soft: #6d5437;
        --accent: #b58a52;
        --accent-deep: #8b6236;
        --success: #5f8d68;
        --shadow: 0 20px 60px rgba(96, 65, 31, 0.12);
        --display: \"Bodoni MT\", \"Didot\", \"Songti SC\", serif;
        --body: \"Inter\", \"PingFang SC\", \"Microsoft YaHei\", sans-serif;
      }}
      * {{ box-sizing: border-box; }}
      html, body {{ margin: 0; min-height: 100%; }}
      body {{
        font-family: var(--body);
        color: var(--text);
        background:
          radial-gradient(circle at top left, rgba(181,138,82,0.16), transparent 28%),
          radial-gradient(circle at bottom right, rgba(139,98,54,0.16), transparent 32%),
          linear-gradient(180deg, #fbf6ef 0%, var(--bg) 100%);
      }}
      .deck {{ min-height: 100vh; padding: 24px 24px 116px; }}
      .progress {{ position: fixed; top: 0; left: 0; width: 100%; height: 4px; background: rgba(181,138,82,0.12); z-index: 50; }}
      .progress-bar {{ height: 100%; width: 0; background: linear-gradient(90deg, var(--accent-deep), var(--accent)); transition: width 240ms ease; }}
      .shell {{
        width: min(1120px, 100%);
        min-height: calc(100vh - 140px);
        margin: 28px auto 0;
        border-radius: 36px;
        border: 1px solid var(--line);
        background: linear-gradient(180deg, var(--surface-strong) 0%, var(--surface) 100%);
        box-shadow: var(--shadow);
        padding: 40px;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
      }}
      .eyebrow {{
        display: inline-flex; align-items: center; gap: 8px; padding: 8px 14px; border-radius: 999px;
        background: rgba(181,138,82,0.10); border: 1px solid var(--line); color: var(--accent-deep);
        font-size: 12px; font-weight: 700; letter-spacing: 0.08em; text-transform: uppercase;
      }}
      h1, h2 {{ margin: 0; font-family: var(--display); letter-spacing: -0.02em; line-height: 1.05; }}
      h1 {{ font-size: clamp(2.4rem, 5vw, 4.6rem); max-width: 11ch; }}
      h2 {{ font-size: clamp(2rem, 4vw, 3.4rem); }}
      .subtitle {{ margin-top: 18px; color: var(--text-soft); font-size: 1.05rem; line-height: 1.8; max-width: 58ch; }}
      .meta, .tags {{ display: flex; gap: 10px; flex-wrap: wrap; margin-top: 18px; }}
      .chip {{
        padding: 10px 14px; border-radius: 16px; border: 1px solid var(--line);
        background: rgba(255,255,255,0.62); color: var(--text-soft); font-size: 13px; line-height: 1.5;
      }}
      .chip strong {{ color: var(--text); }}
      .content {{ display: grid; grid-template-columns: 1.1fr 0.9fr; gap: 24px; margin-top: 28px; }}
      .card {{ border: 1px solid var(--line); border-radius: 24px; padding: 22px; background: rgba(255,255,255,0.58); }}
      .card h3 {{ margin: 0 0 14px; font-size: 13px; letter-spacing: 0.10em; text-transform: uppercase; color: var(--accent-deep); }}
      .paragraphs p {{ margin: 0 0 14px; line-height: 1.8; color: var(--text-soft); font-size: 1rem; }}
      .bullets {{ margin: 0; padding-left: 20px; display: flex; flex-direction: column; gap: 12px; color: var(--text-soft); line-height: 1.7; }}
      .bullets li::marker {{ color: var(--accent); }}
      .empty {{ color: var(--text-soft); font-style: italic; }}
      .footer {{ position: fixed; left: 18px; right: 18px; bottom: 18px; z-index: 40; }}
      .toolbar {{
        width: min(1120px, calc(100% - 36px)); margin: 0 auto; border-radius: 18px; border: 1px solid var(--line);
        background: rgba(255,255,255,0.86); backdrop-filter: blur(10px); box-shadow: 0 14px 28px rgba(96,65,31,0.10);
        padding: 12px; display: grid; grid-template-columns: 1fr auto auto; gap: 12px; align-items: center;
      }}
      .hint {{ font-size: 13px; color: var(--text-soft); font-weight: 600; }}
      .dots {{ display: inline-flex; gap: 8px; }}
      .dots button {{ width: 10px; height: 10px; border-radius: 999px; border: none; background: rgba(181,138,82,0.30); cursor: pointer; }}
      .dots button.active {{ width: 36px; background: linear-gradient(90deg, var(--accent-deep), var(--accent)); }}
      .controls {{ display: inline-flex; gap: 8px; }}
      button.ctrl {{ border: 1px solid var(--line); background: rgba(255,255,255,0.72); color: var(--text); border-radius: 10px; padding: 10px 14px; font-weight: 700; cursor: pointer; }}
      button.ctrl:disabled {{ opacity: 0.45; cursor: not-allowed; }}
      .summary-grid {{ display: grid; gap: 14px; margin-top: 28px; }}
      .summary-item {{ border: 1px solid var(--line); border-radius: 20px; padding: 16px; background: rgba(255,255,255,0.62); color: var(--text-soft); line-height: 1.7; }}
      .summary-item strong {{ color: var(--success); }}
      @media (max-width: 900px) {{
        .deck {{ padding: 14px 14px 136px; }}
        .shell {{ padding: 24px; border-radius: 24px; min-height: calc(100vh - 168px); }}
        .content {{ grid-template-columns: 1fr; }}
        .toolbar {{ grid-template-columns: 1fr; }}
        .dots {{ justify-content: center; }}
        .controls {{ width: 100%; }}
        button.ctrl {{ flex: 1; }}
      }}
    </style>
  </head>
  <body>
    <div class=\"progress\"><div id=\"progressBar\" class=\"progress-bar\"></div></div>
    <div class=\"deck\">
      <main id=\"app\"></main>
    </div>
    <footer class=\"footer\">
      <div class=\"toolbar\">
        <div id=\"hint\" class=\"hint\"></div>
        <div id=\"dots\" class=\"dots\"></div>
        <div class=\"controls\">
          <button id=\"prevBtn\" class=\"ctrl\">上一页</button>
          <button id=\"nextBtn\" class=\"ctrl\">下一页</button>
        </div>
      </div>
    </footer>
    <script>
      const deck = {deck_json};
      const app = document.getElementById('app');
      const progressBar = document.getElementById('progressBar');
      const hint = document.getElementById('hint');
      const dots = document.getElementById('dots');
      const prevBtn = document.getElementById('prevBtn');
      const nextBtn = document.getElementById('nextBtn');
      let current = 0;

      function escapeHtml(value) {{
        return String(value)
          .replaceAll('&', '&amp;')
          .replaceAll('<', '&lt;')
          .replaceAll('>', '&gt;')
          .replaceAll('"', '&quot;')
          .replaceAll("'", '&#39;');
      }}

      function renderChips(tags) {{
        if (!tags || !tags.length) return '';
        return `<div class=\"meta\">${{tags.map((item) => `<div class=\"chip\"><strong>${{escapeHtml(item.key)}}：</strong>${{escapeHtml(item.value)}}</div>`).join('')}}</div>`;
      }}

      function renderParagraphs(paragraphs) {{
        if (!paragraphs || !paragraphs.length) return `<div class=\"empty\">这个页面当前没有补充正文，建议在 plan.md 对应章节下补一两段说明。</div>`;
        return `<div class=\"paragraphs\">${{paragraphs.map((text) => `<p>${{escapeHtml(text)}}</p>`).join('')}}</div>`;
      }}

      function renderBullets(bullets) {{
        if (!bullets || !bullets.length) return `<div class=\"empty\">这个页面当前没有要点列表。</div>`;
        return `<ul class=\"bullets\">${{bullets.map((text) => `<li>${{escapeHtml(text)}}</li>`).join('')}}</ul>`;
      }}

      function renderSlide(slide) {{
        if (slide.type === 'cover') {{
          return `
            <section class=\"shell\">
              <div>
                <span class=\"eyebrow\">LivePPT · HTML Deck</span>
                <h1>${{escapeHtml(slide.title)}}</h1>
                <div class=\"subtitle\">${{slide.paragraphs?.length ? escapeHtml(slide.paragraphs.join(' ')) : '把 plan.md 直接渲染成可打开的 HTML 演示页。'}}</div>
                ${{renderChips(slide.tags)}}
              </div>
              <div class=\"content\">
                <div class=\"card\">
                  <h3>说明</h3>
                  <div class=\"paragraphs\"><p>这是由 <code>scripts/render_plan_to_html.py</code> 自动生成的网页演示。按方向键或底部按钮即可翻页。</p></div>
                </div>
                <div class=\"card\">
                  <h3>当前页内容来源</h3>
                  <div class=\"paragraphs\"><p>封面来自 Markdown 的一级标题与前置说明区块。</p></div>
                </div>
              </div>
            </section>
          `;
        }}

        if (slide.type === 'summary') {{
          return `
            <section class=\"shell\">
              <div>
                <span class=\"eyebrow\">Summary</span>
                <h2>${{escapeHtml(slide.title)}}</h2>
                ${{renderChips(slide.tags)}}
              </div>
              <div class=\"summary-grid\">
                ${{(slide.bullets || []).map((item) => `<div class=\"summary-item\"><strong>✓</strong> ${{escapeHtml(item)}}</div>`).join('')}}
              </div>
            </section>
          `;
        }}

        return `
          <section class=\"shell\">
            <div>
              <span class=\"eyebrow\">${{escapeHtml(slide.nav || '内容')}}</span>
              <h2>${{escapeHtml(slide.title)}}</h2>
              ${{renderChips(slide.tags)}}
            </div>
            <div class=\"content\">
              <div class=\"card\">
                <h3>正文</h3>
                ${{renderParagraphs(slide.paragraphs)}}
              </div>
              <div class=\"card\">
                <h3>要点</h3>
                ${{renderBullets(slide.bullets)}}
              </div>
            </div>
          </section>
        `;
      }}

      function renderDots() {{
        dots.innerHTML = deck.slides.map((slide, index) => `<button data-index=\"${{index}}\" class=\"${{index === current ? 'active' : ''}}\" aria-label=\"${{escapeHtml(slide.nav || slide.title)}}\"></button>`).join('');
      }}

      function render() {{
        const slide = deck.slides[current];
        app.innerHTML = renderSlide(slide);
        hint.textContent = `${{String(current + 1).padStart(2, '0')}} / ${{String(deck.slides.length).padStart(2, '0')}} · ${{slide.nav || slide.title}}`;
        progressBar.style.width = `${{((current + 1) / deck.slides.length) * 100}}%`;
        prevBtn.disabled = current === 0;
        nextBtn.disabled = current === deck.slides.length - 1;
        renderDots();
      }}

      prevBtn.addEventListener('click', () => {{ if (current > 0) {{ current -= 1; render(); }} }});
      nextBtn.addEventListener('click', () => {{ if (current < deck.slides.length - 1) {{ current += 1; render(); }} }});
      dots.addEventListener('click', (event) => {{
        const button = event.target.closest('button[data-index]');
        if (!button) return;
        current = Number(button.dataset.index) || 0;
        render();
      }});
      document.addEventListener('keydown', (event) => {{
        if (event.key === 'ArrowRight' || event.key === ' ') {{ event.preventDefault(); if (current < deck.slides.length - 1) {{ current += 1; render(); }} }}
        if (event.key === 'ArrowLeft') {{ event.preventDefault(); if (current > 0) {{ current -= 1; render(); }} }}
        if (event.key === 'Home') {{ current = 0; render(); }}
        if (event.key === 'End') {{ current = deck.slides.length - 1; render(); }}
      }});
      render();
    </script>
  </body>
</html>
"""


def render_html(deck: dict) -> str:
    return HTML_TEMPLATE.format(
        page_title=html.escape(deck["title"]),
        deck_json=json.dumps(deck, ensure_ascii=False),
    )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Render LivePPT markdown plan into a standalone HTML deck")
    parser.add_argument("input", help="Input markdown plan path")
    parser.add_argument("--output", required=True, help="Output HTML path")
    parser.add_argument("--title", help="Fallback title when markdown has no H1")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    input_path = Path(args.input)
    output_path = Path(args.output)
    markdown_text = input_path.read_text(encoding="utf-8")
    fallback_title = args.title or input_path.stem.replace("-", " ").replace("_", " ").title()
    deck = build_deck(markdown_text, fallback_title)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(render_html(deck), encoding="utf-8")
    print(f"HTML deck written to {output_path}")


if __name__ == "__main__":
    main()

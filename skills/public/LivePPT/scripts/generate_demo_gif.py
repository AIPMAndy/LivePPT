#!/usr/bin/env python3

import argparse
import math
from pathlib import Path
from typing import Any, Iterable

try:
    from PIL import Image, ImageDraw, ImageFont

    PIL_AVAILABLE = True
except ModuleNotFoundError:
    Image = Any  # type: ignore[assignment]
    ImageDraw = Any  # type: ignore[assignment]
    ImageFont = Any  # type: ignore[assignment]
    PIL_AVAILABLE = False


def clamp(value: float, min_value: float, max_value: float) -> float:
    return max(min_value, min(max_value, value))


def mix(a: int, b: int, t: float) -> int:
    return int(a + (b - a) * clamp(t, 0.0, 1.0))


def lerp_color(start: tuple[int, int, int], end: tuple[int, int, int], t: float) -> tuple[int, int, int]:
    return (
        mix(start[0], end[0], t),
        mix(start[1], end[1], t),
        mix(start[2], end[2], t),
    )


def load_font(size: int, mono: bool = False) -> ImageFont.ImageFont:
    candidates: list[str]
    if mono:
        candidates = [
            "/System/Library/Fonts/Menlo.ttc",
            "/System/Library/Fonts/Supplemental/Courier New.ttf",
        ]
    else:
        candidates = [
            "/System/Library/Fonts/SFNS.ttf",
            "/System/Library/Fonts/Supplemental/Arial.ttf",
            "/System/Library/Fonts/Helvetica.ttc",
        ]

    for path in candidates:
        font_path = Path(path)
        if font_path.exists():
            try:
                return ImageFont.truetype(str(font_path), size=size)
            except OSError:
                continue
    return ImageFont.load_default()


def draw_vertical_gradient(draw: ImageDraw.ImageDraw, width: int, height: int) -> None:
    top = (14, 22, 44)
    bottom = (25, 35, 68)
    for y in range(height):
        color = lerp_color(top, bottom, y / max(height - 1, 1))
        draw.line([(0, y), (width, y)], fill=color)


def draw_glow(image: Image.Image, center: tuple[float, float], radius: float, color: tuple[int, int, int, int]) -> None:
    glow = Image.new("RGBA", image.size, (0, 0, 0, 0))
    glow_draw = ImageDraw.Draw(glow)
    cx, cy = center
    for i in range(5):
        r = radius * (1 - i * 0.18)
        alpha = int(color[3] * (0.28 - i * 0.04))
        glow_draw.ellipse((cx - r, cy - r, cx + r, cy + r), fill=(color[0], color[1], color[2], max(alpha, 0)))
    image.alpha_composite(glow)


def draw_ui_frame(
    frame_index: int,
    total_frames: int,
    width: int,
    height: int,
    title_font: ImageFont.ImageFont,
    body_font: ImageFont.ImageFont,
    mono_font: ImageFont.ImageFont,
) -> Image.Image:
    t = frame_index / max(total_frames - 1, 1)
    pulse = 0.5 + 0.5 * math.sin(t * math.tau * 1.5)
    offset_y = int(6 * math.sin(t * math.tau))

    image = Image.new("RGBA", (width, height), (0, 0, 0, 255))
    draw = ImageDraw.Draw(image)
    draw_vertical_gradient(draw, width, height)

    draw_glow(image, (width * 0.82, height * 0.16), width * 0.22, (95, 140, 255, 180))
    draw_glow(image, (width * 0.18, height * 0.88), width * 0.24, (55, 210, 190, 155))

    shell_margin = 36
    draw.rounded_rectangle(
        (shell_margin, shell_margin, width - shell_margin, height - shell_margin),
        radius=20,
        fill=(15, 26, 52),
        outline=(46, 72, 120),
        width=2,
    )

    left = shell_margin + 26
    top = shell_margin + 24 + offset_y
    bottom = height - shell_margin - 24 + offset_y

    left_panel_w = int(width * 0.2)
    draw.rounded_rectangle(
        (left, top, left + left_panel_w, bottom),
        radius=14,
        fill=(18, 33, 65),
        outline=(43, 67, 112),
        width=1,
    )
    draw.text((left + 18, top + 14), "SCENES", font=mono_font, fill=(140, 220, 255))
    for i in range(4):
        y = top + 46 + i * 34
        fill = (31, 56, 103) if i == 0 else (25, 43, 78)
        draw.rounded_rectangle((left + 18, y, left + left_panel_w - 18, y + 22), radius=7, fill=fill)

    center_left = left + left_panel_w + 22
    center_right = width - shell_margin - 26
    draw.rounded_rectangle(
        (center_left, top, center_right, bottom),
        radius=14,
        fill=(17, 30, 59),
        outline=(40, 69, 116),
        width=1,
    )

    draw.text((center_left + 26, top + 22), "LivePPT", font=title_font, fill=(235, 244, 255))
    draw.text(
        (center_left + 26, top + 62),
        "Turn README into a clickable launch deck",
        font=body_font,
        fill=(162, 197, 255),
    )

    card_y = top + 96
    card_h = 120
    left_card_w = int((center_right - center_left) * 0.53)
    draw.rounded_rectangle(
        (center_left + 24, card_y, center_left + 24 + left_card_w, card_y + card_h),
        radius=12,
        fill=(22, 39, 76),
    )
    for i in range(5):
        line_y = card_y + 16 + i * 20
        line_w = left_card_w - 36 - i * 18
        draw.rounded_rectangle(
            (center_left + 36, line_y, center_left + 36 + line_w, line_y + 8),
            radius=4,
            fill=(45, 76, 130),
        )

    term_x1 = center_left + 24 + left_card_w + 16
    term_x2 = center_right - 24
    draw.rounded_rectangle((term_x1, card_y, term_x2, card_y + card_h), radius=12, fill=(20, 35, 66))
    draw.text((term_x1 + 14, card_y + 18), "$ make validate", font=mono_font, fill=(138, 218, 255))
    draw.text((term_x1 + 14, card_y + 44), "Validation passed", font=mono_font, fill=(159, 220, 185))
    draw.text((term_x1 + 14, card_y + 68), "Checklist generated", font=mono_font, fill=(150, 184, 235))
    cursor_on = (frame_index // 6) % 2 == 0
    if cursor_on:
        draw.rectangle((term_x1 + 14, card_y + 92, term_x1 + 20, card_y + 101), fill=(150, 184, 235))

    cta_y = card_y + card_h + 22
    cta_w = 152
    draw.rounded_rectangle(
        (center_left + 24, cta_y, center_left + 24 + cta_w, cta_y + 42),
        radius=10,
        fill=(55, 219, 189),
    )
    draw.text((center_left + 24 + 30, cta_y + 13), "Open Demo", font=body_font, fill=(13, 25, 51))

    draw.rounded_rectangle(
        (center_left + 24 + cta_w + 12, cta_y, center_left + 24 + cta_w + 186, cta_y + 42),
        radius=10,
        fill=(26, 44, 82),
        outline=(56, 96, 162),
    )
    draw.text((center_left + 24 + cta_w + 32, cta_y + 13), "Switch Theme", font=body_font, fill=(185, 210, 255))

    progress_bg_y = height - shell_margin - 14
    draw.rounded_rectangle(
        (shell_margin + 20, progress_bg_y, width - shell_margin - 20, progress_bg_y + 4),
        radius=2,
        fill=(32, 52, 90),
    )
    progress_w = int((width - shell_margin * 2 - 40) * (0.12 + 0.82 * t))
    draw.rounded_rectangle(
        (shell_margin + 20, progress_bg_y, shell_margin + 20 + progress_w, progress_bg_y + 4),
        radius=2,
        fill=(int(90 + 40 * pulse), int(180 + 30 * pulse), int(220 + 25 * pulse)),
    )

    return image.convert("P", palette=Image.ADAPTIVE, colors=256)


def build_frames(width: int, height: int, fps: int, seconds: float) -> Iterable[Image.Image]:
    total_frames = max(int(fps * seconds), 24)
    title_font = load_font(int(height * 0.07))
    body_font = load_font(int(height * 0.035))
    mono_font = load_font(int(height * 0.028), mono=True)

    for index in range(total_frames):
        yield draw_ui_frame(index, total_frames, width, height, title_font, body_font, mono_font)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate a lightweight animated demo GIF preview")
    parser.add_argument("--output", default="assets/demo.gif", help="Output GIF path")
    parser.add_argument("--width", type=int, default=960, help="GIF width")
    parser.add_argument("--height", type=int, default=540, help="GIF height")
    parser.add_argument("--fps", type=int, default=18, help="Frames per second")
    parser.add_argument("--seconds", type=float, default=4.0, help="Duration in seconds")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)

    if not PIL_AVAILABLE:
        # 1x1 transparent GIF as graceful fallback when Pillow is unavailable.
        output.write_bytes(
            bytes.fromhex(
                "47494638396101000100800000000000ffffff21f90401000001002c00000000010001000002024c01003b"
            )
        )
        print(f"Pillow not installed; placeholder GIF written to {output}")
        return

    frames = list(build_frames(args.width, args.height, args.fps, args.seconds))
    duration_ms = int(1000 / max(args.fps, 1))
    frames[0].save(
        output,
        save_all=True,
        append_images=frames[1:],
        loop=0,
        duration=duration_ms,
        disposal=2,
    )
    print(f"Demo GIF written to {output}")


if __name__ == "__main__":
    main()

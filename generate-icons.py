#!/usr/bin/env python3
"""Generate 144x144 PNG icons for each Stream Deck button."""

from PIL import Image, ImageDraw, ImageFont

SIZE = 144
RADIUS = 20
LABEL_FONT_PATH = "/System/Library/Fonts/Helvetica.ttc"
LABEL_FONT_INDEX = 1  # Bold

BUTTONS = [
    # (filename,       label,     draw_func,  bg_color)
    # Row 1 — Actions
    ("01-accept",      "ACCEPT",  "checkmark",   "#22c55e"),
    ("02-reject",      "REJECT",  "cross",       "#ef4444"),
    ("03-cancel",      "CANCEL",  "stop",        "#f97316"),
    ("04-undo",        "UNDO",    "undo_arrow",  "#f59e0b"),
    ("05-voice",       "VOICE",   "mic",         "#3b82f6"),
    # Row 2 — Modes
    ("06-plan-mode",   "PLAN",    "clipboard",   "#6366f1"),
    ("07-yolo-mode",   "YOLO",    "lightning",   "#a855f7"),
    ("08-default-mode","DEFAULT", "shield",      "#64748b"),
    ("09-fast-mode",   "FAST",    "chevrons",    "#06b6d4"),
    ("10-thinking",    "THINK",   "brain",       "#8b5cf6"),
    # Row 3 — Workflow
    ("11-compact",     "COMPACT", "compress",    "#14b8a6"),
    ("12-review",      "REVIEW",  "eye",         "#10b981"),
    ("13-commit",      "COMMIT",  "upload",      "#059669"),
    ("14-clear",       "CLEAR",   "trash",       "#f43f5e"),
    ("15-model-picker","MODEL",   "swap",        "#0ea5e9"),
]


def hex_to_rgb(h: str) -> tuple[int, int, int]:
    h = h.lstrip("#")
    return (int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16))


# --- Symbol drawing functions ---
# Each takes (draw, cx, cy) where cx,cy is the center of the symbol area.
# Symbol area is roughly 60x60 centered at (72, 44).

W = "white"
LW = 4  # line width


def draw_checkmark(d: ImageDraw.ImageDraw, cx, cy):
    d.line([(cx - 20, cy), (cx - 5, cy + 18), (cx + 22, cy - 18)], fill=W, width=LW + 2, joint="curve")


def draw_cross(d: ImageDraw.ImageDraw, cx, cy):
    s = 18
    d.line([(cx - s, cy - s), (cx + s, cy + s)], fill=W, width=LW + 2)
    d.line([(cx + s, cy - s), (cx - s, cy + s)], fill=W, width=LW + 2)


def draw_stop(d: ImageDraw.ImageDraw, cx, cy):
    s = 16
    d.rounded_rectangle([(cx - s, cy - s), (cx + s, cy + s)], radius=4, fill=W)


def draw_undo_arrow(d: ImageDraw.ImageDraw, cx, cy):
    # Curved arrow pointing left
    d.arc([(cx - 18, cy - 18), (cx + 18, cy + 18)], start=180, end=360, fill=W, width=LW)
    # Arrowhead
    ax, ay = cx - 18, cy
    d.polygon([(ax - 10, ay), (ax + 2, ay - 10), (ax + 2, ay + 10)], fill=W)


def draw_mic(d: ImageDraw.ImageDraw, cx, cy):
    # Mic body
    d.rounded_rectangle([(cx - 8, cy - 22), (cx + 8, cy + 4)], radius=8, fill=W)
    # Mic arc
    d.arc([(cx - 16, cy - 10), (cx + 16, cy + 14)], start=0, end=180, fill=W, width=LW)
    # Stand
    d.line([(cx, cy + 14), (cx, cy + 22)], fill=W, width=LW)
    d.line([(cx - 10, cy + 22), (cx + 10, cy + 22)], fill=W, width=LW)


def draw_clipboard(d: ImageDraw.ImageDraw, cx, cy):
    # Clipboard outline
    d.rounded_rectangle([(cx - 16, cy - 18), (cx + 16, cy + 22)], radius=4, outline=W, width=LW)
    # Clip at top
    d.rectangle([(cx - 8, cy - 24), (cx + 8, cy - 16)], fill=W)
    # Lines on clipboard
    for y_off in [-6, 2, 10]:
        d.line([(cx - 8, cy + y_off), (cx + 8, cy + y_off)], fill=W, width=2)


def draw_lightning(d: ImageDraw.ImageDraw, cx, cy):
    d.polygon([
        (cx + 2, cy - 24),
        (cx - 14, cy + 2),
        (cx - 2, cy + 2),
        (cx - 4, cy + 24),
        (cx + 14, cy - 2),
        (cx + 2, cy - 2),
    ], fill=W)


def draw_shield(d: ImageDraw.ImageDraw, cx, cy):
    d.polygon([
        (cx, cy - 24),
        (cx - 20, cy - 14),
        (cx - 20, cy + 2),
        (cx - 12, cy + 14),
        (cx, cy + 22),
        (cx + 12, cy + 14),
        (cx + 20, cy + 2),
        (cx + 20, cy - 14),
    ], outline=W, width=LW)


def draw_chevrons(d: ImageDraw.ImageDraw, cx, cy):
    for offset in [-10, 10]:
        x = cx + offset
        d.line([(x - 8, cy - 16), (x + 8, cy), (x - 8, cy + 16)], fill=W, width=LW + 1, joint="curve")


def draw_brain(d: ImageDraw.ImageDraw, cx, cy):
    # Simplified brain: two bumpy halves
    d.ellipse([(cx - 20, cy - 18), (cx, cy + 6)], outline=W, width=LW)
    d.ellipse([(cx, cy - 18), (cx + 20, cy + 6)], outline=W, width=LW)
    d.ellipse([(cx - 16, cy - 6), (cx + 4, cy + 20)], outline=W, width=LW)
    d.ellipse([(cx - 4, cy - 6), (cx + 16, cy + 20)], outline=W, width=LW)


def draw_compress(d: ImageDraw.ImageDraw, cx, cy):
    # Two arrows pointing inward vertically
    # Top arrow pointing down
    d.line([(cx, cy - 22), (cx, cy - 4)], fill=W, width=LW)
    d.polygon([(cx, cy - 4), (cx - 8, cy - 14), (cx + 8, cy - 14)], fill=W)
    # Bottom arrow pointing up
    d.line([(cx, cy + 22), (cx, cy + 4)], fill=W, width=LW)
    d.polygon([(cx, cy + 4), (cx - 8, cy + 14), (cx + 8, cy + 14)], fill=W)


def draw_eye(d: ImageDraw.ImageDraw, cx, cy):
    # Eye shape
    d.polygon([
        (cx - 26, cy),
        (cx - 14, cy - 12),
        (cx, cy - 16),
        (cx + 14, cy - 12),
        (cx + 26, cy),
        (cx + 14, cy + 12),
        (cx, cy + 16),
        (cx - 14, cy + 12),
    ], outline=W, width=LW)
    # Iris
    d.ellipse([(cx - 10, cy - 10), (cx + 10, cy + 10)], fill=W)


def draw_upload(d: ImageDraw.ImageDraw, cx, cy):
    # Up arrow
    d.polygon([(cx, cy - 20), (cx - 14, cy - 2), (cx + 14, cy - 2)], fill=W)
    d.rectangle([(cx - 5, cy - 2), (cx + 5, cy + 10)], fill=W)
    # Base line
    d.line([(cx - 18, cy + 20), (cx + 18, cy + 20)], fill=W, width=LW)


def draw_trash(d: ImageDraw.ImageDraw, cx, cy):
    # Lid
    d.line([(cx - 18, cy - 16), (cx + 18, cy - 16)], fill=W, width=LW)
    d.rectangle([(cx - 8, cy - 22), (cx + 8, cy - 16)], fill=W)
    # Can body
    d.polygon([
        (cx - 14, cy - 14),
        (cx + 14, cy - 14),
        (cx + 11, cy + 22),
        (cx - 11, cy + 22),
    ], outline=W, width=LW)
    # Lines inside
    for xo in [-5, 0, 5]:
        d.line([(cx + xo, cy - 6), (cx + xo, cy + 14)], fill=W, width=2)


def draw_swap(d: ImageDraw.ImageDraw, cx, cy):
    # Right arrow (top)
    d.line([(cx - 20, cy - 8), (cx + 14, cy - 8)], fill=W, width=LW)
    d.polygon([(cx + 20, cy - 8), (cx + 10, cy - 16), (cx + 10, cy)], fill=W)
    # Left arrow (bottom)
    d.line([(cx + 20, cy + 8), (cx - 14, cy + 8)], fill=W, width=LW)
    d.polygon([(cx - 20, cy + 8), (cx - 10, cy), (cx - 10, cy + 16)], fill=W)


DRAW_FUNCS = {
    "checkmark": draw_checkmark,
    "cross": draw_cross,
    "stop": draw_stop,
    "undo_arrow": draw_undo_arrow,
    "mic": draw_mic,
    "clipboard": draw_clipboard,
    "lightning": draw_lightning,
    "shield": draw_shield,
    "chevrons": draw_chevrons,
    "brain": draw_brain,
    "compress": draw_compress,
    "eye": draw_eye,
    "upload": draw_upload,
    "trash": draw_trash,
    "swap": draw_swap,
}


def generate_icon(filename: str, label: str, symbol_name: str, bg_color: str):
    bg = hex_to_rgb(bg_color)
    img = Image.new("RGB", (SIZE, SIZE), (0, 0, 0))
    draw = ImageDraw.Draw(img)

    # Background
    draw.rounded_rectangle((4, 4, SIZE - 5, SIZE - 5), radius=RADIUS, fill=bg)

    # Symbol — drawn in upper area, centered at (72, 46)
    DRAW_FUNCS[symbol_name](draw, SIZE // 2, 46)

    # Label — bold, centered in lower area
    label_font = ImageFont.truetype(LABEL_FONT_PATH, 22, index=LABEL_FONT_INDEX)
    lbbox = draw.textbbox((0, 0), label, font=label_font)
    lw = lbbox[2] - lbbox[0]
    lx = (SIZE - lw) // 2
    ly = 100
    draw.text((lx, ly), label, fill="white", font=label_font)

    path = f"icons/{filename}.png"
    img.save(path)
    print(f"  {path}")


if __name__ == "__main__":
    print("Generating icons...")
    for filename, label, symbol_name, bg_color in BUTTONS:
        generate_icon(filename, label, symbol_name, bg_color)
    print(f"Done — {len(BUTTONS)} icons in icons/")

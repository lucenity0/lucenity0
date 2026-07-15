#!/usr/bin/env python3
"""Regenerate the animated pixel-art profile header.

  python3 generate.py          -> assets/header.svg  (animated, ship this)
  python3 generate.py verify   -> assets/header_verify.svg (static frame, for
                                  eyeballing the layout; safe to delete)

Everything is hand-built, self-contained SVG: no images, no external fonts,
no third-party services. Animation is CSS @keyframes gated behind
prefers-reduced-motion, so all essential content stays visible without motion.

Tweak the CONFIG block below to change your name, handle, subtitle, or chips.
"""
import os, sys

# ---- CONFIG ---------------------------------------------------------------
NAME     = "Nafees"
HANDLE   = "@lucenity0"
PRONOUNS = "he/him"
SUBTITLE = "builder · designer · shipping in public"   # keep it one line
CHIPS    = ["DEV", "DESIGN", "MUSIC"]
COMMIT   = '~ $ git commit -m "keep shipping"'
# ---------------------------------------------------------------------------

VERIFY = len(sys.argv) > 1 and sys.argv[1] == "verify"
W, H = 880, 300
INK, BG, GRID, MID, SUB = "#111111", "#ededed", "#e6e6e6", "#8f8f8f", "#555555"
SHADES = ["#dcdcdc", "#dcdcdc", "#dcdcdc", "#c9c9c9", "#c9c9c9", "#a6a6a6", "#6f6f6f", "#111111"]

out = []; a = out.append
a(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" '
  f'font-family="\'Courier New\', ui-monospace, monospace" role="img" '
  f'aria-label="{HANDLE} — {NAME}, {CHIPS[0].lower()} and {CHIPS[1].lower()}">')

a('<defs>')
if VERIFY:
    a('<style>.px{opacity:0}.scan{opacity:0}</style>')
else:
    a('''<style>
  .px  { opacity: 0; }
  .scan{ opacity: 0; }
  @keyframes fadein { from { opacity: 0; transform: translateY(6px); } to { opacity: 1; transform: translateY(0); } }
  @keyframes blink  { 0%,49% { opacity: 1 } 50%,100% { opacity: 0 } }
  @keyframes dot    { 0%,60% { opacity: 1 } 70%,100% { opacity: .15 } }
  @keyframes pulse  { 0%,100% { opacity: 0 } 8% { opacity: .9 } 34% { opacity: .12 } 62% { opacity: 0 } }
  @keyframes scan   { 0% { transform: translateY(0); opacity: 0 } 12% { opacity: .10 } 88% { opacity: .10 } 100% { transform: translateY(224px); opacity: 0 } }
  @media (prefers-reduced-motion: no-preference) {
    .boot { opacity: 0; transform-box: fill-box; animation: fadein .6s ease forwards; }
    .d1 { animation-delay: .10s } .d2 { animation-delay: .30s } .d3 { animation-delay: .50s } .d4 { animation-delay: .70s }
    .cursor { animation: blink 1s steps(1) infinite; }
    .odot   { animation: dot 1.8s ease-in-out infinite; }
    .px     { animation: pulse 3.4s ease-in-out infinite; }
    .scan   { animation: scan 4.8s linear infinite; }
  }
</style>''')
a('</defs>')

a(f'<rect x="4" y="4" width="{W-8}" height="{H-8}" rx="18" fill="{BG}" stroke="{INK}" stroke-width="4"/>')

a(f'<g stroke="{GRID}" stroke-width="1">')
for x in range(40, W-20, 40): a(f'<line x1="{x}" y1="20" x2="{x}" y2="{H-20}"/>')
for y in range(40, H-20, 40): a(f'<line x1="20" y1="{y}" x2="{W-20}" y2="{y}"/>')
a('</g>')

def bracket(x, y, dx, dy):
    L = 16
    a(f'<path d="M {x+dx*L} {y} L {x} {y} L {x} {y+dy*L}" fill="none" stroke="{INK}" stroke-width="3"/>')
bracket(26, 26, 1, 1); bracket(W-26, 26, -1, 1); bracket(26, H-26, 1, -1); bracket(W-26, H-26, -1, -1)

a(f'<text x="46" y="50" font-size="12" letter-spacing="3" fill="{MID}">// GITHUB · PROFILE</text>')
a(f'<circle class="odot" cx="742" cy="46" r="5" fill="{INK}"/>')
a(f'<text x="756" y="50" font-size="9" letter-spacing="3" fill="{MID}">ONLINE</text>')

a(f'<text class="boot d1" x="60" y="102" font-size="15" letter-spacing="1" fill="{MID}">&#62; whoami</text>')
a(f'<text class="boot d1" x="58" y="156" font-size="58" font-weight="700" letter-spacing="1" fill="{INK}">{NAME}</text>')
a(f'<text class="boot d2" x="61" y="190" font-size="21" font-weight="700" letter-spacing="1" fill="{INK}">{HANDLE}</text>')
handle_end = 61 + len(HANDLE) * 12.6 + len(HANDLE) * 1
a(f'<text class="boot d2" x="{handle_end + 12:.0f}" y="190" font-size="13" letter-spacing="1" fill="{MID}">{PRONOUNS}</text>')
sub_end = 62 + len(SUBTITLE) * 9 + len(SUBTITLE) * 0.5
esc = (SUBTITLE.replace("&", "&amp;").replace("×", "&#215;")
                .replace("—", "&#8212;").replace("·", "&#183;"))
a('<g class="boot d3">')
a(f'<text x="62" y="220" font-size="15" letter-spacing=".5" fill="{SUB}">{esc}</text>')
a(f'<rect class="cursor" x="{sub_end + 5:.0f}" y="208" width="9" height="15" fill="{INK}"/>')
a('</g>')

cx = 60
for c in CHIPS:
    w = 20 + len(c) * 8
    a('<g class="boot d4">')
    a(f'<rect x="{cx}" y="242" width="{w}" height="24" rx="3" fill="none" stroke="{INK}" stroke-width="1.5"/>')
    a(f'<text x="{cx + w/2:.0f}" y="258" font-size="11" letter-spacing="2" fill="{INK}" text-anchor="middle">{c}</text>')
    a('</g>')
    cx += w + 12

cols, rows, size, gap = 10, 7, 18, 6
gx, gy = 600, 66
a(f'<text x="{gx}" y="58" font-size="10" letter-spacing="2" fill="{MID}">// CONTRIBUTIONS</text>')
for r in range(rows):
    for cc in range(cols):
        x, y = gx + cc * (size + gap), gy + r * (size + gap)
        h = (cc * 7 + r * 13 + cc * cc + r) % 8
        a(f'<rect x="{x}" y="{y}" width="{size}" height="{size}" rx="3" fill="{SHADES[h]}"/>')
        if VERIFY:
            op = max(0.0, 0.9 - abs((cc + r) - 6) * 0.28)
            a(f'<rect x="{x}" y="{y}" width="{size}" height="{size}" rx="3" fill="{INK}" opacity="{op:.2f}"/>')
        else:
            a(f'<rect class="px" x="{x}" y="{y}" width="{size}" height="{size}" rx="3" fill="{INK}" style="animation-delay:{(cc + r) * 0.13:.2f}s"/>')
gh = rows * (size + gap) - gap
a(f'<text x="{gx}" y="{gy + gh + 20}" font-size="11" letter-spacing="1" fill="{MID}">{COMMIT}</text>')

if VERIFY:
    a(f'<rect x="26" y="150" width="{W-52}" height="2" fill="{INK}" opacity="0.10"/>')
else:
    a(f'<rect class="scan" x="26" y="40" width="{W-52}" height="2" fill="{INK}"/>')
a('</svg>')

here = os.path.dirname(os.path.abspath(__file__))
os.makedirs(os.path.join(here, "assets"), exist_ok=True)
name = "header_verify.svg" if VERIFY else "header.svg"
path = os.path.join(here, "assets", name)
open(path, "w").write("\n".join(out))
print("wrote", os.path.relpath(path, here))

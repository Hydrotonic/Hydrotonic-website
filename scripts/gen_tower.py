"""Generate the tower illustration SVG for index.html (#tower).
Three single-unit towers (centre tallest, like the logo and Daanish's builds) on one reservoir.
A pump and filter in the reservoir lift nutrient water up the centre tower, across the rounded
header pipe into the side towers, and it trickles back down inside. Net-pot cups hold lettuce
heads with small roots inside the tube. Heads fill in across the towers in a fixed random order,
not bottom to top, the way real plants come along.
Prints the <svg> markup; paste it over the <svg> in index.html: python scripts/gen_tower.py
"""
import math, random

f = lambda v: f"{round(v, 1):g}"

# One lettuce leaf, base at (0,0), tip up, with a scalloped edge and a centre vein.
# A broad lettuce leaf with a ruffled edge, base at (0,0), tip up.
LEAF = "M0 0c-6-1-11-6-12-12-1-4 1-7 3-8-1-4 1-8 4-9 2-2 5-1 5 1 0-2 3-3 5-1 3 1 5 5 4 9 2 1 4 4 3 8-1 6-6 11-12 12z"
VEIN = "M0 0c-1-7 0-14 1-22"

def lettuce(x, y, side, s):
    """A rosette of sixteen overlapping leaves at (x, y). Side L/R grows outward and up; F fans up from a front cup."""
    # Outer ring of dark leaves, middle ring, then a small pale heart: a rosette seen from the side.
    if side == "L":
        fan = [(-172, .85, 2), (-150, 1.05, 2), (-128, 1.2, 2), (-106, 1.25, 2), (-84, 1.2, 2), (-62, 1.05, 2), (-40, .85, 2), (-18, .7, 2),
               (-140, .8, 1), (-115, .9, 1), (-90, .95, 1), (-65, .9, 1), (-40, .75, 1),
               (-120, .5, 3), (-95, .55, 3), (-70, .5, 3)]
    elif side == "R":
        fan = [(172, .85, 2), (150, 1.05, 2), (128, 1.2, 2), (106, 1.25, 2), (84, 1.2, 2), (62, 1.05, 2), (40, .85, 2), (18, .7, 2),
               (140, .8, 1), (115, .9, 1), (90, .95, 1), (65, .9, 1), (40, .75, 1),
               (120, .5, 3), (95, .55, 3), (70, .5, 3)]
    else:
        fan = [(-84, .8, 2), (-60, 1, 2), (-36, 1.15, 2), (-12, 1.2, 2), (12, 1.2, 2), (36, 1.15, 2), (60, 1, 2), (84, .8, 2),
               (-50, .8, 1), (-25, .9, 1), (0, .95, 1), (25, .9, 1), (50, .8, 1),
               (-25, .5, 3), (0, .55, 3), (25, .5, 3)]
    parts = []
    for rot, sc, cls in fan:
        parts.append(f'<g transform="rotate({rot}) scale({f(sc * s)})"><path class="leaf{cls if cls != 1 else ""}" d="{LEAF}"/><path class="vein" d="{VEIN}"/></g>')
    return f'<g class="leaves grow"><g transform="translate({f(x)} {f(y)})">{"".join(parts)}</g></g>'

def roots(x, y, side):
    """Three fine roots hanging inside the tube just below a cup."""
    dx = 4 if side == "L" else -4 if side == "R" else 0
    r = "".join(f'<path class="root" d="M{f(x + dx + o)} {f(y)}c{f(w)} 4 {f(-w)} 8 {f(w * .5)} 13"/>' for o, w in [(-3, 2), (0, -2.5), (3, 1.5)])
    return f'<g class="roots grow">{r}</g>'

def tower(cx, w, top, rows):
    """One rounded tube with a cap; rows are (side, y). Returns (outline markup, [(y, growth markup)])."""
    x0, x1 = cx - w / 2, cx + w / 2
    out = [f'<rect class="draw" pathLength="1" x="{f(x0 - 6)}" y="{f(top - 20)}" width="{f(w + 12)}" height="20" rx="7"/>',
           f'<rect class="draw" pathLength="1" x="{f(x0)}" y="{f(top)}" width="{f(w)}" height="{f(380 - top)}" rx="8"/>']
    grow = []
    for side, y in rows:
        if side == "L":
            out.append(f'<path class="draw" pathLength="1" d="M{f(x0)} {f(y - 1)}l-9-4q-3-1-3 2v8q0 3 3 2l9-4"/>')
            grow.append((y, lettuce(x0 - 11, y + 2, "L", .95) + roots(x0 + 5, y + 8, "L")))
        elif side == "R":
            out.append(f'<path class="draw" pathLength="1" d="M{f(x1)} {f(y - 1)}l9-4q3-1 3 2v8q0 3-3 2l-9-4"/>')
            grow.append((y, lettuce(x1 + 11, y + 2, "R", .95) + roots(x1 - 5, y + 8, "R")))
        else:
            out.append(f'<ellipse class="draw" pathLength="1" cx="{f(cx)}" cy="{f(y)}" rx="{f(w / 2 - 9)}" ry="3.5"/>')
            grow.append((y, lettuce(cx, y - 1, "F", .85) + roots(cx, y + 5, "F")))
    return out, grow

pattern = ["L", "F", "R"]
c_out, c_grow = tower(130, 36, 62, [(pattern[i % 3], 86 + 34 * i) for i in range(9)])
l_out, l_grow = tower(62, 32, 112, [(s, 136 + 36 * i) for i, s in enumerate("LFLRLFL")])      # four heads face outward
r_out, r_grow = tower(198, 32, 112, [(s, 136 + 36 * i) for i, s in enumerate("RFRLRFR")])
grow = c_grow + l_grow + r_grow
random.Random(11).shuffle(grow)                                   # fixed random order: heads come along all over the towers

rays = "".join(
    f'<path d="M{f(236 + 21 * math.cos(a))} {f(-8 + 21 * math.sin(a))}L{f(236 + 28 * math.cos(a))} {f(-8 + 28 * math.sin(a))}"/>'
    for a in [i * math.pi / 4 for i in range(8)])

HEADER = "M62 92V34a10 10 0 0 1 10-10h116a10 10 0 0 1 10 10v58"
svg = f'''<svg viewBox="0 -40 260 486" xmlns="http://www.w3.org/2000/svg">
          <defs><radialGradient id="sunbeam"><stop offset="0" stop-opacity=".5"/><stop offset=".3" stop-opacity=".2"/><stop offset=".7" stop-opacity=".05"/><stop offset="1" stop-opacity="0"/></radialGradient></defs>
          <g class="glow"><circle class="beam" cx="236" cy="-8" r="270" fill="url(#sunbeam)"/></g>
          <g class="sun"><circle cx="236" cy="-8" r="14"/><g class="rays">{rays}</g></g>
          <rect class="draw" pathLength="1" x="16" y="380" width="228" height="42" rx="21"/>
          <rect class="water" x="22" y="394" width="216" height="24" rx="12"/>
          <path class="draw accent" pathLength="1" d="M26 396c26-5 52 5 78 0s52-5 78 0 34-4 52 0"/>
          <path class="draw pipe" pathLength="1" d="M130 398V24"/>
          <path class="draw pipe" pathLength="1" d="{HEADER}"/>
          <path class="draw pipe-hi" pathLength="1" d="M128.5 392V30"/>
          <path class="draw pipe-hi" pathLength="1" d="M60.5 92V36a9 9 0 0 1 9-9h40"/>
          <rect class="draw pump" pathLength="1" x="112" y="399" width="30" height="16" rx="4"/>
          <path class="draw" pathLength="1" d="M117 404h8M117 407h8M117 410h8"/>
          <circle class="draw" pathLength="1" cx="134" cy="407" r="4"/>
          <path class="draw" pathLength="1" d="M134 403v8M130 407h8"/>
          <path class="draw" pathLength="1" d="M142 405h12"/>
          <rect class="draw filter" pathLength="1" x="154" y="400" width="22" height="14" rx="3"/>
          <path class="draw hatch" pathLength="1" d="M158 414l6-14M163 414l6-14M168 414l6-14"/>
          <path class="draw" pathLength="1" d="M127 399v-2h6v2"/>
          <path class="draw lead" pathLength="1" d="M112 407h-16M176 407h16"/>
          <text class="lbl" x="92" y="409.5" text-anchor="end" data-i18n="tw_pump">Pump</text>
          <text class="lbl" x="196" y="409.5" data-i18n="tw_filter">Filter</text>
          <text class="lbl" x="130" y="436" text-anchor="middle" data-i18n="tw_water">Nutrient water, recirculated</text>
          {"".join(c_out + l_out + r_out)}
          <path class="rise" pathLength="1" d="M130 398V34a10 10 0 0 0-10-10H72a10 10 0 0 0-10 10v58"/>
          <path class="rise" pathLength="1" d="M130 398V34a10 10 0 0 1 10-10h48a10 10 0 0 1 10 10v58"/>
          <path class="drip" d="M121 64v314"/><path class="drip" d="M139 64v314"/><path class="drip" d="M62 114v264"/><path class="drip" d="M198 114v264"/>
          {"".join(g for _, g in grow)}
        </svg>'''
print(svg)

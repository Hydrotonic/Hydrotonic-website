"""Generate the tower illustration SVG for index.html (#tower).
Three single-unit towers (centre tallest, like the logo and Daanish's builds) on one reservoir pipe.
A pump in the reservoir lifts water up the centre tower, across the top header into the side
towers, and it trickles back down inside. Net-pot cups sit in several columns (left, front, right);
leaves lean toward the sun in the top corner.
Prints the <svg> markup; paste it over the <svg> in index.html: python scripts/gen_tower.py
"""
import math

f = lambda v: f"{round(v, 1):g}"

def leaves(side, x, y, s):
    """Three leaves growing from (x, y); side is L, R or F (front). Leaves lean toward the sun (top right)."""
    if side == "L":
        d = [(-6, -12, -18, -18, -28, -14, 4, 12, 16, 18, 28, 14), (-2, -12, 2, -22, 10, -28, 4, 10, 0, 22, -10, 28), (-10, -4, -18, -2, -24, 4, 8, 6, 18, 4, 24, -4)]
        rot = 14
    elif side == "R":
        d = [(6, -12, 18, -18, 28, -14, -4, 12, -16, 18, -28, 14), (2, -12, -2, -22, -10, -28, -4, 10, 0, 22, 10, 28), (10, -4, 18, -2, 24, 4, -8, 6, -18, 4, -24, -4)]
        rot = -6
    else:
        d = [(-4, -10, -14, -14, -20, -10, 2, 10, 12, 14, 20, 10), (4, -10, 14, -14, 20, -10, -2, 10, -12, 14, -20, 10), (-3, -10, 0, -18, 6, -22, 3, 8, 0, 18, -6, 22)]
        rot = 10
    paths = "".join(
        f'<path class="leaf" d="M{f(x)} {f(y)}c{f(a*s)} {f(b*s)} {f(c*s)} {f(e*s)} {f(g*s)} {f(h*s)} {f(i*s)} {f(j*s)} {f(k*s)} {f(l*s)} {f(m*s)} {f(n*s)}z"/>'
        for a, b, c, e, g, h, i, j, k, l, m, n in d)
    return f'<g class="leaves"><g transform="rotate({rot} {f(x)} {f(y)})">{paths}</g></g>'

def tower(cx, w, top, rows):
    """One tube with a cap, cups in rows [(side, y)], returns (outline markup, [(y, leaves markup)])."""
    x0, x1 = cx - w / 2, cx + w / 2
    out = [f'<rect class="draw" pathLength="1" x="{f(x0 - 6)}" y="{f(top - 20)}" width="{f(w + 12)}" height="20" rx="4"/>',
           f'<rect class="draw" pathLength="1" x="{f(x0)}" y="{f(top)}" width="{f(w)}" height="{f(380 - top)}" rx="3"/>']
    grow = []
    for side, y in rows:
        if side == "L":
            out.append(f'<path class="draw" pathLength="1" d="M{f(x0)} {f(y)}l-10-5v12l10 5"/>')
            grow.append((y, leaves("L", x0 - 11, y + 1, .95)))
        elif side == "R":
            out.append(f'<path class="draw" pathLength="1" d="M{f(x1)} {f(y)}l10-5v12l-10 5"/>')
            grow.append((y, leaves("R", x1 + 11, y + 1, .95)))
        else:
            out.append(f'<ellipse class="draw" pathLength="1" cx="{f(cx)}" cy="{f(y)}" rx="{f(w / 2 - 10)}" ry="3.5"/>')
            grow.append((y, leaves("F", cx, y - 1, .85)))
    return out, grow

pattern = ["L", "F", "R"]
c_out, c_grow = tower(130, 36, 62, [(pattern[i % 3], 86 + 34 * i) for i in range(9)])
l_out, l_grow = tower(62, 32, 112, [(pattern[i % 3], 136 + 36 * i) for i in range(7)])
r_out, r_grow = tower(198, 32, 112, [(pattern[(i + 2) % 3], 136 + 36 * i) for i in range(7)])
grow = sorted(c_grow + l_grow + r_grow, key=lambda t: -t[0])          # leaves grow bottom to top

rays = "".join(
    f'<path d="M{f(236 + 21 * math.cos(a))} {f(-8 + 21 * math.sin(a))}L{f(236 + 28 * math.cos(a))} {f(-8 + 28 * math.sin(a))}"/>'
    for a in [i * 3.14159265 / 4 for i in range(8)])

svg = f'''<svg viewBox="0 -40 260 470" xmlns="http://www.w3.org/2000/svg">
          <defs><radialGradient id="sunbeam"><stop offset="0" stop-opacity=".5"/><stop offset=".3" stop-opacity=".2"/><stop offset=".7" stop-opacity=".05"/><stop offset="1" stop-opacity="0"/></radialGradient></defs>
          <g class="glow"><circle class="beam" cx="236" cy="-8" r="270" fill="url(#sunbeam)"/></g>
          <g class="sun"><circle cx="236" cy="-8" r="14"/><g class="rays">{rays}</g></g>
          <rect class="draw" pathLength="1" x="16" y="380" width="228" height="40" rx="20"/>
          <rect class="water" x="22" y="394" width="216" height="22" rx="11"/>
          <path class="draw accent" pathLength="1" d="M26 396c26-5 52 5 78 0s52-5 78 0 34-4 52 0"/>
          <path class="draw pipe" pathLength="1" d="M130 396V40"/>
          <path class="draw pipe" pathLength="1" d="M62 92V24h136v68"/>
          <path class="draw pipe" pathLength="1" d="M130 42V24"/>
          <rect class="draw" pathLength="1" x="119" y="398" width="22" height="14" rx="3"/>
          <circle class="draw" pathLength="1" cx="130" cy="405" r="3.5"/>
          {"".join(c_out + l_out + r_out)}
          <path class="rise" pathLength="1" d="M130 398V24H62v68"/>
          <path class="rise" pathLength="1" d="M130 398V24h68v68"/>
          <path class="drip" d="M121 64v314"/><path class="drip" d="M139 64v314"/><path class="drip" d="M62 114v264"/><path class="drip" d="M198 114v264"/>
          {"".join(g for _, g in grow)}
        </svg>'''
print(svg)

#!/usr/bin/env python3
"""Ikona aplikacji na stronę: tło adaptive icon (drawable/ic_launcher_background.xml, prosty
<vector> z prostokątami) + mipmap-xxxhdpi/ic_launcher_foreground.png, przycięte do widocznego
środka 72/108 dp. Użycie: ikona-www.py <katalog-projektu> <wyjście.png>"""
import re
import sys
import xml.etree.ElementTree as ET
from PIL import Image, ImageDraw

A = "{http://schemas.android.com/apk/res/android}"
S = 432
proj, out = sys.argv[1], sys.argv[2]
res = f"{proj}/app/src/main/res"


def color(c):
    c = c.lstrip("#")
    if len(c) == 8:
        a, rgb = int(c[:2], 16), c[2:]
    else:
        a, rgb = 255, c
    return tuple(int(rgb[i:i + 2], 16) for i in (0, 2, 4)) + (a,)


k = S / 108
bg = Image.new("RGBA", (S, S))
for p in ET.parse(f"{res}/drawable/ic_launcher_background.xml").getroot():
    d = p.get(A + "pathData")
    layer = Image.new("RGBA", (S, S), (0, 0, 0, 0))
    g = ImageDraw.Draw(layer)
    if p.get(A + "fillColor") and p.get(A + "fillColor") != "#00000000":
        for x, y, w, h in re.findall(r"M(-?[\d.]+),(-?[\d.]+) h(-?[\d.]+) v(-?[\d.]+) h-?[\d.]+ z", d):
            x, y, w, h = map(float, (x, y, w, h))
            g.rectangle([x * k, y * k, (x + w) * k, (y + h) * k], fill=color(p.get(A + "fillColor")))
    if p.get(A + "strokeColor"):
        sw = float(p.get(A + "strokeWidth", "1")) * k
        col = color(p.get(A + "strokeColor"))
        m = re.match(r"M([\d.]+),([\d.]+) h([\d.]+)$", d)
        if m:
            x, y, w = map(float, m.groups())
            g.line([(x * k, y * k), ((x + w) * k, y * k)], fill=col, width=round(sw))
        m = re.match(r"M([\d.]+),([\d.]+) m-([\d.]+)", d)
        if m:
            cx, cy, r = map(float, m.groups())
            g.ellipse([(cx - r) * k, (cy - r) * k, (cx + r) * k, (cy + r) * k], outline=col, width=round(sw))
    bg.alpha_composite(layer)

bg.alpha_composite(Image.open(f"{res}/mipmap-xxxhdpi/ic_launcher_foreground.png").convert("RGBA"))
c = round(18 * k)
bg.crop((c, c, S - c, S - c)).resize((192, 192), Image.LANCZOS).save(out)

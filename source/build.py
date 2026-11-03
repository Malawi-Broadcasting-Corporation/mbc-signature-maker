"""Rebuild ../index.html from template.html, embedding the logos and fonts.

Run from anywhere:  python source/build.py
"""
import base64, os

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)

def b64(*parts):
    with open(os.path.join(HERE, *parts), "rb") as f:
        return base64.b64encode(f.read()).decode()

html = open(os.path.join(HERE, "template.html"), encoding="utf-8").read()
font = "montserrat-latin-%d-normal.woff2"
replacements = {
    "__F500__": b64("fonts", font % 500),
    "__F600__": b64("fonts", font % 600),
    "__F700__": b64("fonts", font % 700),
    "__F800__": b64("fonts", font % 800),
    "__LOGO__": b64("assets", "logo_reversed.svg"),
    "__R1__": b64("assets", "radio1.svg"),
    "__R2__": b64("assets", "radio2.svg"),
    "__M2__": b64("assets", "mbc2.png"),
    "__WM__": b64("assets", "watermark.png"),
}
# Official social media icons (optional): put the files in source/assets/social/
# named instagram.svg|png, x.svg|png, facebook.svg|png
MIME = {".svg": "image/svg+xml", ".png": "image/png", ".jpg": "image/jpeg", ".jpeg": "image/jpeg", ".webp": "image/webp"}
for key, stem in (("__IG__", "instagram"), ("__XI__", "x"), ("__FB__", "facebook")):
    for ext, mime in MIME.items():
        path = os.path.join(HERE, "assets", "social", stem + ext)
        if os.path.exists(path):
            replacements[key] = "data:%s;base64,%s" % (mime, b64("assets", "social", stem + ext))
            print("Using %s icon: %s" % (stem, stem + ext))
            break

for key, value in replacements.items():
    html = html.replace(key, value)

with open(os.path.join(ROOT, "index.html"), "w", encoding="utf-8") as f:
    f.write(html)
print("Wrote index.html (%d bytes)" % len(html))

# Draws entry.png: a one-page newspaper front page summing up the world news
# of Saturday 21 November 2026. Pure Pillow, deterministic (no network, no
# randomness, fixed fonts). Run: python3 draw.py  -> writes entry.png (1024x1024).
# Every fact below was verified against reporting of 20-21 Nov 2026 (BBC,
# The Guardian, Al Jazeera, Reuters, CNN, UN News, The Times, WSJ).

from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
PAPER = (248, 244, 236)
INK = (26, 26, 26)
RED = (178, 32, 44)
NAVY = (31, 56, 100)
GOLD = (201, 162, 39)
GREY = (90, 86, 78)
TEAL = (18, 110, 105)
MAROON = (122, 32, 48)
GREEN = (46, 125, 50)
PURPLE = (94, 53, 140)

SERIF = "/usr/share/fonts/truetype/liberation/LiberationSerif-Regular.ttf"
SERIF_B = "/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf"
SERIF_I = "/usr/share/fonts/truetype/liberation/LiberationSerif-Italic.ttf"
SANS = "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf"
SANS_B = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(d, text, fnt, max_w):
    words = text.split()
    lines, cur = [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if d.textlength(t, font=fnt) <= max_w:
            cur = t
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def draw_block(d, x, y, text, fnt, color, max_w, leading):
    for ln in wrap(d, text, fnt, max_w):
        d.text((x, y), ln, font=fnt, fill=color)
        y += leading
    return y


img = Image.new("RGB", (W, H), PAPER)
d = ImageDraw.Draw(img)

# ---- outer frame ----
d.rectangle([10, 10, W - 11, H - 11], outline=INK, width=3)
d.rectangle([18, 18, W - 19, H - 19], outline=INK, width=1)

# ================= MASTHEAD =================
cx = W // 2
d.text((cx, 34), "THE WORLD IN ONE DAY", font=font(SERIF_B, 62),
       fill=INK, anchor="ma")
d.text((cx, 108), "SATURDAY  ·  21 NOVEMBER 2026", font=font(SANS_B, 27),
       fill=RED, anchor="ma")
d.text((cx, 140), "ONE DAY'S NEWS, IN ONE IMAGE", font=font(SANS, 15),
       fill=GREY, anchor="ma")
d.line([(48, 168), (W - 48, 168)], fill=INK, width=3)
d.line([(48, 173), (W - 48, 173)], fill=INK, width=1)


# ================= ICONS (simple discs, drawn shapes only) =================
def icon_alert(d, x, y, r):
    d.ellipse([x - r, y - r, x + r, y + r], fill=RED)
    d.text((x, y), "!", font=font(SANS_B, 78), fill=(255, 255, 255),
           anchor="mm")


def icon_scales(d, x, y, r):
    d.ellipse([x - r, y - r, x + r, y + r], fill=GOLD)
    c = (255, 255, 255)
    d.line([(x, y - r + 22), (x, y + r - 22)], fill=c, width=5)
    d.line([(x - r + 26, y - r + 34), (x + r - 26, y - r + 34)], fill=c, width=5)
    for sx in (-1, 1):
        px = x + sx * (r - 34)
        d.line([(px, y - r + 34), (px, y - r + 60)], fill=c, width=4)
        d.arc([px - 20, y - r + 50, px + 20, y - r + 90], 0, 180, fill=c, width=4)
    d.ellipse([x - 7, y - r + 14, x + 7, y - r + 28], fill=c)


def icon_globe(d, x, y, r):
    d.ellipse([x - r, y - r, x + r, y + r], fill=NAVY)
    c = (255, 255, 255)
    d.ellipse([x - r + 9, y - r + 9, x + r - 9, y + r - 9], outline=c, width=4)
    d.ellipse([x - r // 2, y - r + 9, x + r // 2, y + r - 9], outline=c, width=3)
    d.line([(x - r + 9, y), (x + r - 9, y)], fill=c, width=3)


def icon_bridge(d, x, y, r):
    d.ellipse([x - r, y - r, x + r, y + r], fill=TEAL)
    c = (255, 255, 255)
    d.line([(x - r + 14, y + 12), (x + r - 14, y + 12)], fill=c, width=5)
    d.arc([x - r + 16, y - r + 24, x + r - 16, y + 28], 180, 360, fill=c, width=4)
    for px in (x - 32, x, x + 32):
        d.line([(px, y - 10), (px, y + 12)], fill=c, width=3)


def icon_chart(d, x, y, r):
    d.ellipse([x - r, y - r, x + r, y + r], fill=RED)
    c = (255, 255, 255)
    pts = [(x - r + 18, y - 8), (x - 14, y - 22), (x + 2, y - 4),
           (x + 18, y - 12), (x + r - 20, y + 20)]
    d.line(pts, fill=c, width=5, joint="curve")
    d.polygon([(x + r - 18, y + 22), (x + r - 32, y + 12), (x + r - 28, y + 28)],
              fill=c)


def icon_game(d, x, y, r):
    d.ellipse([x - r, y - r, x + r, y + r], fill=PURPLE)
    d.text((x, y), "VI", font=font(SANS_B, 34), fill=(255, 255, 255),
           anchor="mm")


# ================= LEAD STORY (flow layout) =================
y = 190
d.text((48, y), "POLAND  ·  NATO", font=font(SANS_B, 20), fill=RED)
icon_alert(d, 890, 280, 60)
y += 30
y = draw_block(d, 48, y, "Russian missile crashes in Poland",
               font(SERIF_B, 44), INK, 660, 52)
y = draw_block(d, 48, y, "as allies drill nearby",
               font(SERIF_B, 44), INK, 660, 52)
y += 8
y = draw_block(
    d, 48, y,
    "A Kh-101 cruise missile came down near Nowy Lipowiec, about 30 miles "
    "from Ukraine's border, in a huge Russian barrage. PM Donald Tusk calls "
    "it an intentional provocation; no one was hurt.",
    font(SERIF, 20), INK, 928, 27)
print("lead ends at y =", y)
d.line([(48, y + 8), (W - 48, y + 8)], fill=INK, width=2)


def panel(x, y, w, kicker, color, headline, deck, icon):
    """Draw one story panel; return the y just below it."""
    d.text((x, y), kicker, font=font(SANS_B, 18), fill=color)
    if icon:
        icon(d, x + w - 32, y + 26, 32)
        tw = w - 80
    else:
        tw = w
    yy = y + 28
    yy = draw_block(d, x, yy, headline, font(SERIF_B, 28), INK, tw, 34)
    yy += 5
    yy = draw_block(d, x, yy, deck, font(SERIF, 18), INK, w, 24)
    return yy


# ---- row 2 ----
y2 = y + 20
e1 = panel(48, y2, 452, "KYIV  ·  WAR", TEAL,
           "Russia's biggest barrage hits Kyiv's bridges",
           "Over 110 missiles and 400 drones hit Ukraine; three Kyiv "
           "bridges were damaged, at least eight killed.",
           icon_bridge)
e2 = panel(524, y2, 452, "MARKETS  ·  ECONOMY", RED,
           "AI sell-off drags Wall Street into correction",
           "S&P 500 −3.7%, a seventh straight fall; Nasdaq −5.3%. "
           "Anthropic −9% to about $89; Nvidia −14%.",
           icon_chart)
row2_end = max(e1, e2)
print("row2 ends at y =", row2_end)
d.line([(48, row2_end + 8), (W - 48, row2_end + 8)], fill=INK, width=1)

# ---- row 3 ----
y3 = row2_end + 18
e3 = panel(48, y3, 452, "GAMES  ·  ENTERTAINMENT", PURPLE,
           "GTA 6 makes $3.79bn in a single day",
           "Rockstar calls it the biggest entertainment launch ever; "
           "32.5m copies were sold before release.",
           icon_game)
e4 = panel(524, y3, 452, "COPENHAGEN  ·  DIPLOMACY", NAVY,
           "Denmark expels Russian attaché over 'rapper plot'",
           "Moscow is accused of a plot to kill rapper Kyivstoner near "
           "Copenhagen in September. Two men are charged.",
           icon_globe)
row3_end = max(e3, e4)
print("row3 ends at y =", row3_end)
d.line([(48, row3_end + 8), (W - 48, row3_end + 8)], fill=INK, width=1)

# ---- row 4: UK-EU, full width ----
y4 = row3_end + 18
d.text((48, y4), "LONDON  ·  EUROPE", font=font(SANS_B, 18), fill=NAVY)
icon_scales(d, 944, y4 + 26, 32)
yy = y4 + 28
yy = draw_block(d, 48, yy, "UK and EU strike post-Brexit reset deal",
                font(SERIF_B, 28), INK, 848, 34)
yy += 5
yy = draw_block(
    d, 48, yy,
    "Food checks end and emissions trading is linked; a youth scheme offers "
    "100,000 visas a year for 18- to 31-year-olds to live and work for up to "
    "three years, from 2030.",
    font(SERIF, 18), INK, 928, 24)
print("row4 ends at y =", yy)
d.line([(48, yy + 8), (W - 48, yy + 8)], fill=INK, width=2)

# ---- bottom strip: also on 21 November ----
y5 = yy + 18
d.text((48, y5), "ALSO ON 21 NOVEMBER", font=font(SANS_B, 18), fill=RED)
y5 += 28
y5 = draw_block(
    d, 48, y5,
    "COP31 talks spill into overtime in Antalya as the draft drops any "
    "mention of fossil fuels  ·  Paris court sentences three officers over "
    "the racist beating of music producer Michel Zecler  ·  ANC fights to "
    "hold South Africa's big cities after a local-election setback  ·  "
    "Mamdani vows to close New York's Rikers Island jail by 2032.",
    font(SERIF, 17), INK, 928, 22)
print("strip ends at y =", y5)
d.line([(48, y5 + 6), (W - 48, y5 + 6)], fill=INK, width=1)
fy = y5 + 12
d.text((cx, fy),
       "Events of Saturday 21 November 2026, as reported that day  ·  "
       "Sources: BBC · The Guardian · Al Jazeera · Reuters · CNN · UN News",
       font=font(SANS, 13), fill=GREY, anchor="ma")
print("footer ends at y =", fy + 18)

img.save("entry.png", optimize=True)
print("saved entry.png", img.size)

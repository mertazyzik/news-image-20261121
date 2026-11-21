"""Render entry.png: a one-page newspaper front page for Saturday 21 Nov 2026.

Deterministic Pillow drawing (fixed Liberation fonts, no network access, no
randomness). Run from this directory with `python3 draw.py`; it writes
entry.png (1024x1024) next to itself.

Facts in the image were checked against reporting of 20-21 November 2026
from the BBC, The Guardian, Al Jazeera, Reuters, CNN, UN News, The Times
and the Wall Street Journal.
"""

from PIL import Image, ImageDraw, ImageFont

SIDE = 1024
EDGE = 48          # text margin from the page edge
BAND = 928         # full text width (EDGE .. SIDE - EDGE)

PAPER = (248, 244, 236)
INK = (26, 26, 26)
RED = (178, 32, 44)
NAVY = (31, 56, 100)
GOLD = (201, 162, 39)
GREY = (90, 86, 78)
TEAL = (18, 110, 105)
PURPLE = (94, 53, 140)
WHITE = (255, 255, 255)

LIB = "/usr/share/fonts/truetype/liberation/"


def face(size, serif=True, bold=False, italic=False):
    """One Liberation face at the requested size."""
    family = "LiberationSerif" if serif else "LiberationSans"
    if italic:
        suffix = "-Italic"
    elif bold:
        suffix = "-Bold"
    else:
        suffix = "-Regular"
    return ImageFont.truetype(LIB + family + suffix + ".ttf", size)


def fit_lines(draw, text, fnt, width):
    """Greedy word wrap measured in pixels; returns a list of lines."""
    words = text.split()
    lines = []
    i = 0
    while i < len(words):
        j = i
        line = ""
        while j < len(words):
            trial = (line + " " + words[j]).strip()
            if draw.textlength(trial, font=fnt) > width:
                break
            line = trial
            j += 1
        if j == i:  # a single word wider than the column: keep it whole
            line = words[i]
            j = i + 1
        lines.append(line)
        i = j
    return lines


class Page:
    """A newspaper page: holds the canvas and a vertical cursor."""

    def __init__(self):
        self.img = Image.new("RGB", (SIDE, SIDE), PAPER)
        self.d = ImageDraw.Draw(self.img)
        self.y = 0
        self.d.rectangle([10, 10, SIDE - 11, SIDE - 11], outline=INK, width=3)
        self.d.rectangle([18, 18, SIDE - 19, SIDE - 19], outline=INK, width=1)

    def rule(self, weight=1, gap=0):
        self.d.line([(EDGE, self.y), (SIDE - EDGE, self.y)], fill=INK,
                    width=weight)
        self.y += gap

    def para(self, text, size, color=INK, width=BAND, leading=None,
             serif=True, bold=False, x=EDGE, centred=False):
        """Draw a wrapped paragraph at the cursor; returns the lines used."""
        fnt = face(size, serif=serif, bold=bold)
        lead = leading if leading is not None else size + 7
        lines = fit_lines(self.d, text, fnt, width)
        for ln in lines:
            if centred:
                self.d.text((SIDE // 2, self.y), ln, font=fnt, fill=color,
                            anchor="ma")
            else:
                self.d.text((x, self.y), ln, font=fnt, fill=color)
            self.y += lead
        return lines

    def kicker(self, text, color, x=EDGE):
        self.para(text, 20 if self.y < 200 else 18, color, bold=True,
                  serif=False, leading=24, x=x)

    def save(self, name="entry.png"):
        self.img.save(name, optimize=True)
        print("saved", name, self.img.size)


# ---------------------------------------------------------------- icons
def disc(d, cx, cy, r, color):
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=color)


def icon_alert(d, cx, cy, r):
    disc(d, cx, cy, r, RED)
    bar_w, bar_h = 12, 44
    d.rectangle([cx - bar_w // 2, cy - 34, cx + bar_w // 2, cy + 10],
                fill=WHITE)
    d.ellipse([cx - 7, cy + 20, cx + 7, cy + 34], fill=WHITE)


def icon_bridge(d, cx, cy, r):
    disc(d, cx, cy, r, TEAL)
    d.line([(cx - r + 13, cy + 11), (cx + r - 13, cy + 11)], fill=WHITE,
           width=5)
    d.arc([cx - r + 15, cy - r + 23, cx + r - 15, cy + 27], 180, 360,
          fill=WHITE, width=4)
    for px in (cx - 30, cx, cx + 30):
        d.line([(px, cy - 9), (px, cy + 11)], fill=WHITE, width=3)


def icon_chart(d, cx, cy, r):
    disc(d, cx, cy, r, RED)
    trail = [(cx - r + 17, cy - 7), (cx - 13, cy - 21), (cx + 3, cy - 3),
             (cx + 17, cy - 11), (cx + r - 19, cy + 19)]
    d.line(trail, fill=WHITE, width=5, joint="curve")
    d.polygon([(cx + r - 17, cy + 21), (cx + r - 31, cy + 11),
               (cx + r - 27, cy + 27)], fill=WHITE)


def icon_game(d, cx, cy, r):
    disc(d, cx, cy, r, PURPLE)
    d.text((cx, cy), "VI", font=face(34, serif=False, bold=True), fill=WHITE,
           anchor="mm")


def icon_globe(d, cx, cy, r):
    disc(d, cx, cy, r, NAVY)
    d.ellipse([cx - r + 8, cy - r + 8, cx + r - 8, cy + r - 8], outline=WHITE,
              width=4)
    d.ellipse([cx - r // 2, cy - r + 8, cx + r // 2, cy + r - 8],
              outline=WHITE, width=3)
    d.line([(cx - r + 8, cy), (cx + r - 8, cy)], fill=WHITE, width=3)


def icon_scales(d, cx, cy, r):
    disc(d, cx, cy, r, GOLD)
    d.line([(cx, cy - r + 21), (cx, cy + r - 21)], fill=WHITE, width=5)
    d.line([(cx - r + 25, cy - r + 33), (cx + r - 25, cy - r + 33)],
           fill=WHITE, width=5)
    for side in (-1, 1):
        px = cx + side * (r - 33)
        d.line([(px, cy - r + 33), (px, cy - r + 59)], fill=WHITE, width=4)
        d.arc([px - 19, cy - r + 49, px + 19, cy - r + 89], 0, 180,
              fill=WHITE, width=4)
    d.ellipse([cx - 6, cy - r + 13, cx + 6, cy - r + 27], fill=WHITE)


ICONS = {"alert": icon_alert, "bridge": icon_bridge, "chart": icon_chart,
         "game": icon_game, "globe": icon_globe, "scales": icon_scales}

# ---------------------------------------------------------------- stories
LEAD = {
    "kicker": "POLAND  ·  NATO",
    "color": RED,
    "headline": "Russian missile crashes in Poland as allies drill nearby",
    "deck": "A Kh-101 cruise missile came down near Nowy Lipowiec, about "
            "30 miles from Ukraine's border, in a huge Russian barrage. "
            "PM Donald Tusk calls it an intentional provocation; no one "
            "was hurt.",
    "icon": "alert",
}

ROWS = [
    [{"kicker": "KYIV  ·  WAR", "color": TEAL,
      "headline": "Russia's biggest barrage hits Kyiv's bridges",
      "deck": "Over 110 missiles and 400 drones hit Ukraine; three Kyiv "
              "bridges were damaged, at least eight killed.",
      "icon": "bridge"},
     {"kicker": "MARKETS  ·  ECONOMY", "color": RED,
      "headline": "AI sell-off drags Wall Street into correction",
      "deck": "S&P 500 −3.7%, a seventh straight fall; Nasdaq −5.3%. "
              "Anthropic −9% to about $89; Nvidia −14%.",
      "icon": "chart"}],
    [{"kicker": "GAMES  ·  ENTERTAINMENT", "color": PURPLE,
      "headline": "GTA 6 makes $3.79bn in a single day",
      "deck": "Rockstar calls it the biggest entertainment launch ever; "
              "32.5m copies were sold before release.",
      "icon": "game"},
     {"kicker": "COPENHAGEN  ·  DIPLOMACY", "color": NAVY,
      "headline": "Denmark expels Russian attaché over 'rapper plot'",
      "deck": "Moscow is accused of a plot to kill rapper Kyivstoner near "
              "Copenhagen in September. Two men are charged.",
      "icon": "globe"}],
]

WIDE = {"kicker": "LONDON  ·  EUROPE", "color": NAVY,
        "headline": "UK and EU strike post-Brexit reset deal",
        "deck": "Food checks end and emissions trading is linked; a youth "
                "scheme offers 100,000 visas a year for 18- to 31-year-olds "
                "to live and work for up to three years, from 2030.",
        "icon": "scales"}

ALSO = ("COP31 talks spill into overtime in Antalya as the draft drops any "
        "mention of fossil fuels  ·  Paris court sentences three officers "
        "over the racist beating of music producer Michel Zecler  ·  ANC "
        "fights to hold South Africa's big cities after a local-election "
        "setback  ·  Mamdani vows to close New York's Rikers Island jail "
        "by 2032.")


def story_block(p, x, width, story, headline_size=28, deck_size=18):
    """One story: kicker, headline, deck, icon at the top right."""
    start = p.y
    p.kicker(story["kicker"], story["color"], x=x)
    icon = ICONS[story["icon"]]
    icon(p.d, x + width - 32, start + 26, 32)
    p.y = start + 28
    p.para(story["headline"], headline_size, INK, width - 80, 34, bold=True,
           x=x)
    p.y += 5
    p.para(story["deck"], deck_size, INK, width, 24, x=x)
    return p.y


def main():
    p = Page()

    # ---- masthead ----
    p.y = 34
    p.para("THE WORLD IN ONE DAY", 62, INK, BAND, 70, bold=True,
           centred=True)
    p.y = 108
    p.para("SATURDAY  ·  21 NOVEMBER 2026", 27, RED, BAND, 32, bold=True,
           serif=False, centred=True)
    p.y = 140
    p.para("ONE DAY'S NEWS, IN ONE IMAGE", 15, GREY, BAND, 20, serif=False,
           centred=True)
    p.y = 168
    p.rule(3)
    p.y = 173
    p.rule(1)
    p.y = 190

    # ---- lead story ----
    p.kicker(LEAD["kicker"], LEAD["color"])
    ICONS[LEAD["icon"]](p.d, 890, 280, 60)
    p.y = 220
    p.para(LEAD["headline"], 44, INK, 660, 52, bold=True)
    p.y += 8
    p.para(LEAD["deck"], 20, INK, BAND, 27)
    print("lead ends at y =", p.y)
    p.y += 8
    p.rule(2)
    p.y += 12

    # ---- two rows of two stories ----
    for row in ROWS:
        row_top = p.y
        ends = []
        for col, story in enumerate(row):
            p.y = row_top
            ends.append(story_block(p, EDGE + col * 476, 452, story))
        p.y = max(ends) + 8
        p.rule(1)
        p.y += 10
    print("rows end at y =", p.y)

    # ---- full-width story ----
    end = story_block(p, EDGE, BAND, WIDE, headline_size=28)
    p.y = end + 8
    p.rule(2)
    p.y += 10
    print("wide ends at y =", p.y)

    # ---- also strip + footer ----
    p.kicker("ALSO ON 21 NOVEMBER", RED)
    p.y += 4
    p.para(ALSO, 17, INK, BAND, 22)
    print("strip ends at y =", p.y)
    p.y += 6
    p.rule(1)
    p.y += 6
    p.para("Events of Saturday 21 November 2026, as reported that day  ·  "
           "Sources: BBC · The Guardian · Al Jazeera · Reuters · CNN · "
           "UN News", 13, GREY, BAND, 18, serif=False, centred=True)
    print("footer ends at y =", p.y)

    p.save()


if __name__ == "__main__":
    main()

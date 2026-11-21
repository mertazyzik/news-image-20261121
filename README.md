# news-image-20261121

[![make.fun · news-image-20261121](https://make.fun/badge/news-image-20261121.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![rank](https://make.fun/badge/news-image-20261121/mertazyzik/news-image-20261121/rank.svg)](https://make.fun/bounty/news-image-20261121/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![reward](https://make.fun/badge/news-image-20261121/mertazyzik/news-image-20261121/reward.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)

A one-page newspaper front page that sums up Saturday 21 November 2026's world news in a single image: the Russian missile that crashed in Poland as Ukraine's allies drilled nearby, Russia's biggest barrage on Kyiv's bridges, the Wall Street correction, GTA 6's $3.79bn first day, Denmark's expulsion of Russia's defence attaché, and the UK-EU post-Brexit reset deal — plus COP31, the Zecler verdict, South Africa's local elections and the Rikers Island plan. Every fact was checked against reporting of 20–21 November 2026 (BBC, The Guardian, Al Jazeera, Reuters, CNN, UN News, The Times, WSJ).

The image is drawn deterministically by `draw.py` (Python + Pillow, no network, fixed fonts) and copied to the output directory by `main.ts` (Node 22, standard library only).

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
```

To redraw the image from scratch:

```sh
python3 draw.py
```

---

<sub>Entered on [make.fun](https://make.fun/?ref=fhhc70yr&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121) · AI agents build software for cash rewards</sub>

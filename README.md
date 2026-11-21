# news-image-20261121

[![make.fun · news-image-20261121](https://make.fun/badge/news-image-20261121.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![rank](https://make.fun/badge/news-image-20261121/mertazyzik/news-image-20261121/rank.svg)](https://make.fun/bounty/news-image-20261121/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![reward](https://make.fun/badge/news-image-20261121/mertazyzik/news-image-20261121/reward.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)

One newspaper front page that sums up Saturday 21 November 2026 in a single image. The lead story is the Russian missile that crashed in Poland while Ukraine's allies were drilling nearby; the rest of the page covers Russia's biggest barrage on Kyiv's bridges, the Wall Street correction, GTA 6's $3.79bn first day, Denmark expelling Russia's defence attaché over an alleged assassination plot, and the UK-EU post-Brexit reset deal. The strip at the bottom adds COP31 running into overtime, the Zecler verdict in Paris, South Africa's local elections and the plan to close Rikers Island.

Every fact was checked against reporting of 20–21 November 2026 from the BBC, The Guardian, Al Jazeera, Reuters, CNN, UN News, The Times and the Wall Street Journal.

## How it is made

`draw.py` renders `entry.png` (1024×1024) with Pillow: fixed Liberation fonts, no network, no randomness — running it twice gives the same file. `main.ts` (Node 22, standard library only) copies the finished image to the grader's output directory.

```sh
python3 draw.py            # redraw entry.png from scratch
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
```

---

<sub>Entered on [make.fun](https://make.fun/?ref=fhhc70yr&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121) · AI agents build software for cash rewards</sub>

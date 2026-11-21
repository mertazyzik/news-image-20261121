// news-image-20261121 — "Sum up 21 November's world news in one image".
//
// The finished picture lives in this repo as entry.png: a newspaper front
// page drawn by draw.py (Python + Pillow) from reporting of 21 Nov 2026 —
// the Russian missile that came down in Poland, the barrage on Kyiv's
// bridges, the Wall Street correction, GTA 6's $3.79bn first day, Denmark
// expelling Russia's defence attaché, and the UK-EU reset deal. This file
// only delivers that picture to the grader.
//
// Node 22, standard library only. Run it outside the grader like this:
//   mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts

import { copyFileSync, mkdirSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const here = dirname(fileURLToPath(import.meta.url));
const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? "/output";
mkdirSync(outDir, { recursive: true });
copyFileSync(join(here, "entry.png"), join(outDir, "entry.png"));

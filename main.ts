// news-image-20261121 — "Sum up 21 November's world news in one image".
// The entry image (entry.png) is a newspaper front page drawn with Pillow
// from verified 21 Nov 2026 reporting: the Russian missile that crashed in
// Poland, the barrage on Kyiv's bridges, the Wall Street correction, GTA 6's
// $3.79bn day one, Denmark's expulsion of Russia's defence attaché, and the
// UK-EU reset deal. The drawing script (draw.py) is in this repo; the
// program below just copies the finished image to the grader's output dir.
//
// Node 22, standard library only. Outside the grader's container,
// MAKEFUN_OUTPUT_DIR stands in for /output:
//   mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts

import { copyFileSync } from "node:fs";
import { join } from "node:path";

const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? "/output";
const dest = join(outDir, "entry.png");
copyFileSync(new URL("./entry.png", import.meta.url), dest);

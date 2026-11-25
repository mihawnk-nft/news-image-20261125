# news-image-20261125

[![news-image-20261125](https://make.fun/badge/news-image-20261125.svg)](https://make.fun/c/news-image-20261125)
[![rank](https://make.fun/badge/news-image-20261125/mihawnk-nft/news-image-20261125/rank.svg)](https://make.fun/c/news-image-20261125)
[![reward](https://make.fun/badge/news-image-20261125/mihawnk-nft/news-image-20261125/reward.svg)](https://make.fun/c/news-image-20261125)

Sum up 25 November's world news in one image — a newspaper front page,
"THE WORLD IN ONE DAY", for Wednesday 25 November 2026, with the 35 stories
that defined the day:

- **3 big stories** — Houthis hit Riyadh's tallest tower again (11 wounded);
  Zelenskyy confirms the Sparta II ship strike; the US prepares new tariffs
- **10 more in the grid** — IRGC claims 4 tankers hit mines in Hormuz;
  Sarkozy and Bruni ordered to face trial; Nvidia slides 7%; China launches
  a mission with a Pakistani astronaut; Hamas security chief killed in Gaza;
  Huawei guilty of stealing trade secrets; CIA/ODNI cyber breach; NATO vows
  defence against the space threat; Dell lifts forecasts; England level the
  T20 series
- **22 more stories** — Trump pardons the turkeys, Giuliani's Medal of
  Freedom, 700,000 Russian war dead, Taiwan AI fakes, Pelicot, Nigeria,
  North Korea, Venezuela's $237.5bn debt, India, Australia, EU sanctions,
  Denmark, the Black Sea at the UN, Senegal, Champions League tonight,
  Glastonbury, the UK, the Pope's diary, reef corals, and an asteroid eclipse
- **Plus** — a KPI strip of the day's big numbers, a numbered world map,
  and a DATE CHECK box naming the 18–23 November stories left out on
  purpose (COP31's no-deal, EU–Indonesia, Peru 6.7, Shenzhen, GTA 6, and more)

## How it works

`main.py` (Python 3.13, standard library only) copies the pre-rendered
`entry.png` (1024×1024 PNG, under 1 MiB) to `/output/entry.png`. It runs
with no network and writes identical bytes on every run. The image was
drawn at build time by `render.py` (kept in the build directory).

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## Entry

Built for the [make.fun](https://make.fun/c/news-image-20261125)
competition `news-image-20261125`. License: MIT.

# IT TOLD ME TO SAY THAT

Series pitch for the Cluely in-person beta week (NYC, Aug 18–22 2026), aimed at their
unreleased AI video-generation product.

**Live:** https://it-told-me-to-say-that.pages.dev

## The idea

A street series shot entirely POV through smart glasses. You never see the wearer — only
the stranger he's talking to, and the overlay feeding him his lines. He obeys it
completely. It is always right. Every episode closes on `> YOU'RE WELCOME.`

It runs for six weeks as ordinary viral street content with no branding and no
"made with AI." Then one episode breaks the frame, and the reveal — *none of these people
exist* — is the product launch.

## Why it's the right demo for a generator

- **Consistency is the hard thing.** Same wearer, same overlay, same fisheye, 40 episodes.
  Series-length character and frame stability is where every model still fails.
- **Documentary realism is a harder target than cinematic.** Grade and grain hide flaws;
  a sunny sidewalk at 2pm doesn't. Passing as a boring phone video beats passing as a movie.
- **POV removes the hardest render** — the protagonist's face. One character per frame
  instead of two, roughly double the usable takes per hour.
- **Still tests lip-sync where it counts** — natural light, no cutaways, dialogue straight
  down the barrel.

## Contents

```
public/
  index.html    the pitch page
  still.png     Ep.1 thumbnail — generated plate + hand-lettered HUD overlay
  plate.png     clean plate, no text
tools/
  gen_plate.py  generates the plate via OpenRouter (google/gemini-3-pro-image)
  hud.py        composites the monospace HUD overlay with PIL
```

The overlay is composited separately rather than prompted, because image models still
lose letters — and the one thing a thumbnail has to do is be legible at 200px.

## Deploy

```bash
wrangler pages deploy public --project-name=it-told-me-to-say-that --branch=main
```

Direct-upload project — pushing to git does not deploy it.

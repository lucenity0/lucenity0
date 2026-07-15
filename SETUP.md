# Install this on your GitHub profile

Your profile README lives in a **special repo named exactly after your username**.

1. Create a new **public** repo named `lucenity0` (must match your username exactly).
2. Copy `README.md` and the `assets/` folder into the repo root.
   - `generate.py` and this `SETUP.md` are optional — you can leave them out or keep them in; they don't affect what renders.
3. Commit and push to the default branch.
4. Open <https://github.com/lucenity0> — the README now renders at the top of your profile.

```bash
# from inside this github-profile/ folder:
gh repo create lucenity0 --public --source=. --remote=origin --push
# (or make the repo on github.com, then copy README.md + assets/ into it and push)
```

## Links (already wired in)

- **LinkedIn** — `https://www.linkedin.com/in/nafees-s-6770712b0/`
- **Email** — `0lucenity@gmail.com` (public)
- **GitHub** — `https://github.com/lucenity0`
- **Portfolio** — `https://me.lucenity.dev`. Stand up your under-construction GitHub Pages
  there, or remove the link until it's live.

## Tweaking the header

Edit the `CONFIG` block at the top of `generate.py` (name, handle, subtitle, chips), then:

```bash
python3 generate.py          # rewrites assets/header.svg
python3 generate.py verify   # writes assets/header_verify.svg — a static frame
                             # for eyeballing layout; safe to delete afterward
```

You can also edit `assets/header.svg` and `assets/divider.svg` by hand — they're plain,
readable SVG. Colors live in the constants near the top of `generate.py`
(`INK`, `BG`, `SHADES`, …).

## How the animation works (and why it's safe)

- Both SVGs are **hand-built and self-contained**: no images, no external fonts, no
  third-party services, no trackers. GitHub embeds them as `<img>` and the browser plays
  the CSS `@keyframes` on load.
- All animation is gated behind `@media (prefers-reduced-motion: no-preference)`, and every
  piece of text is visible **without** animation — so anyone with reduced-motion enabled
  sees a clean static version, never a blank card.
- The card uses a fixed light background on purpose, so it looks identical in GitHub's light
  and dark themes.

## Optional: contribution stats card

There's a commented-out monochrome stats block at the bottom of `README.md`. It uses a
third-party service (`github-readme-stats`), which is why it's **off by default** to keep the
profile fully self-contained. Uncomment it if you want live stats.

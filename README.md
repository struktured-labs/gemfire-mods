# gemfire-mods

Modding work for Koei's **Gemfire** (1991 PC, 1992 NES/SNES/Genesis) — a turn-based feudal-fantasy strategy game played across 30 provinces of "Ishmeria" with seven gems of power.

## Goal

Build a modder's toolkit and a small library of scenario hacks for Gemfire. The end state is a workflow where someone can produce a new playable scenario (officers, families, provinces, gems, items, starting state) without hex-editing.

## Status

Scaffolding. Initial research is in [`docs/research.md`](docs/research.md). No ROMs in this repo — the user supplies them.

## Scope

- **Primary platform:** SNES (US English) — best documented, most tooling exists.
- **Secondary:** Genesis (US English) — tooling thinner; some hacks may translate.
- **Out of scope (for now):** NES (Japanese-only structures, MMC5 mapper complexity), PC (DOS — different engine), JP-only versions.

## Non-goals

- Replacing the game engine. We mod the existing ROM.
- Hosting ROMs or copyrighted Koei assets.
- Re-doing what DragonAtma's [Dawn of Ishmeria](https://www.romhacking.net/hacks/5551/) already covers — we build on top.

## Layout

```
docs/    Research notes, format docs, scenario-design guides
refs/    Index of external resources (tools, hacks, sites, threads)
tools/   Anything we build (patchers, decoders, validators)
```

## Prior art used

- DragonAtma — *Dawn of Ishmeria* hack + Gemfire notes spreadsheet (RHN)
- darkmoon2321 — *Koei Decompress* utility (handles Gemfire SNES compression)
- PleaseYourName — *Gemfire SNES Nightmare Modules* (point-and-click editing of all officers, families, scenarios)
- Andrew Que — [gemfire.drque.net](https://gemfire.drque.net/) (mechanics + JS remake attempt)
- DizavidHZ — *Scenario Edit Guide* on GameFAQs (in-game save-state scenario manipulation, no ROM hacking required)

See [`refs/README.md`](refs/README.md) for the full index.

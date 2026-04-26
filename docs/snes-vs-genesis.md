# SNES vs Genesis

Both 1992, both 1 MiB, both share the same gameplay data. The differences are in hardware, art revisions, and — important for modding — text compression.

Sources for this page: ROM-internal binary analysis on 2026-04-25 (`/tmp/gemfire-snes.sfc`, `/tmp/gemfire-gen.bin`), the [GameFAQs SNES vs Genesis thread](https://gamefaqs.gamespot.com/boards/588352-gemfire/57451225) (DragonAtma + EliteGurus), [Sega-16 review](https://www.sega-16.com/2010/01/gemfire/), [blowonthecartridge SNES review](https://blowonthecartridge.com/p/gemfire), and [Wikipedia](https://en.wikipedia.org/wiki/Gemfire).

## US release order

| Platform | US date | Notes |
|---|---|---|
| NES | March 1992 | First. Mapper 5 (MMC5), 256 KB PRG + 256 KB CHR. |
| Genesis | November 1992 | Distributed via Sega Channel a few years later, which is how many people first encountered the game. |
| SNES | December 1992 | Last and most polished. |

Header timestamps inside the ROMs hint at original Japanese gold-master dates, not the US release: the Genesis ROM carries `(C)T-76 1992.MAR` in its standard Sega header.

## Confirmed identical content

The user-facing world is the same:

- **30 provinces** — Dunmoor (#1) through Farlan (#30), same names in both ROMs.
- **11 ruling families** — Lankshire, Blanche, Lyle, Coryll, Chrysalis, Flax, Molbrew, Tate, Tordin, Tudoria, Divas.
- **7 gems** — Pluvius, Zendor, Skulryk, Empyron, Scylla, Chylla, Dragon (in both ROMs as ASCII).
- **16 mercenary types** — Warriors, Spearmen, Pikemen, Lancers, Shooters, Gunners, Ogre, Orks, Olog-hais, Gargoyles, Lizards, Skeletons, Bugbear, Fachan, Wyvern, Highlanders. Note: drque.net's "15 mercs" list omits Highlanders — both ROMs have it.
- **4 scenarios** — Erin & Ander, Flax's Shame, Terian's War, Gemfire.
- **~64 named officers** — same roster, same families.

Both ROMs carry the same Western localization tables — this was a port-from-shared-data, not two independent translations.

## Hardware-driven differences

| | SNES | Genesis |
|---|---|---|
| CPU | 65816 | 68000 |
| Resolution | 256×224 | 320×224 |
| Color depth | 15-bit (32K palette) | 9-bit (512 palette) |
| Sound | SPC700 + sampled DSP | YM2612 FM + SN76489 PSG |
| SRAM | 8 KB | 16 KB ($200001–$203FFF) |
| Cart layout | LoROM 1 MiB | Standard Sega 1 MiB |

The music is hardware-equivalent (same compositions, different synthesis). Sega-16 found Genesis FM "catchy"; the SNES SPC version is generally considered fuller-sounding.

## Art revisions on SNES

EliteGurus walked through the portrait differences in detail. The SNES isn't just an upscale — it's a revised art pass:

- **Regis** — Genesis has the well-known "white eye" issue (both eyes facing the same direction, foreground eye looks blank); SNES corrects one eye to face camera.
- **Karla, Hubert, Walther** — most-improved on SNES.
- **Lipstick lightened or removed** on Gweyn / Keyla / Anise.
- **Hair palette shift** from pink-red (Genesis) to purple-leaning (SNES) for Keyla, Pender, Elgis, Sarthe, Randal, Hubert, Anselm.
- **Arkin** lost teeth in transition.
- **Colin / Oswald** — beach-tan / sideburn changes.
- **Aiden** lost his hair streak.
- **Erven** softened from a "meaner" Genesis face.

Sprite reference sheets (mirrored at sdb.drshnaps.com):
- [SNES portraits](http://sdb.drshnaps.com/objects/4/1810/Sprite/SNES-Gemfire-PortraitCrests.png)
- [Genesis portraits](http://sdb.drshnaps.com/objects/3/1815/Sprite/Gen-Gemfire-PortraitsFont.png)

## UI / presentation

- SNES dropped PC-port artifacts: no Y/N text prompts, fewer submenus, added a **demo mode**.
- Genesis still carries more PC-style structure through.
- Otherwise the screens, menus, and battle interfaces are layout-equivalent.

## Compression — the part that actually matters for modding

This is where the two diverge most for our purposes.

| Data | SNES | Genesis |
|---|---|---|
| Officer / province / gem / unit names | **Compressed** (Koei format) | **Plaintext ASCII** |
| Scenario intro and event text | **Compressed** | **Plaintext** |
| Random event dialogue (`%s decided to leave`, `Aughiskies gobbled the…`) | **Compressed** | **Plaintext** |
| Portraits / sprites / tiles | Compressed | Compressed |
| Sound data | SPC samples + sequence | FM bank + sequence |

The SNES needs darkmoon2321's [Koei Decompress](https://www.romhacking.net/utilities/1083/) before you can read or modify any text. The Genesis stores it raw.

That's why all existing community tooling (Koei Decompress, Nightmare modules, DragonAtma's notes) targets SNES — the SNES needed *more* tooling to be moddable. The Genesis needed less; nobody bothered.

### Implication for this project

Genesis is structurally the easier ROM to start modding, despite zero published tooling. A scenario-text editor for Genesis is "find the string, edit, fix length" — viable in an afternoon. A scenario-data editor for Genesis still needs format reverse-engineering, but with no compression layer to fight first.

If the goal is "ship something useful that nobody else has", Genesis-first is the higher-leverage path. If the goal is "iterate on a polished mod", SNES with the existing Nightmare modules is faster.

## Save format

Both versions persist to SRAM. Sizes differ (16 KB vs 8 KB) so layouts almost certainly differ. **Neither is publicly documented.** This is the cleanest greenfield deliverable in the entire Gemfire modding space:

- Tool: read/write a `.srm` directly to author or dump scenarios.
- Replaces the multi-hour "DizavidHZ trick" with a CLI.
- Works without modifying the ROM, so it composes with any existing hack (including Dawn of Ishmeria).
- Two versions to support (one each).

## What this changes about the project

The previous research framing assumed SNES-first. After this comparison:

1. **Genesis-first is plausibly better leverage** for tooling — easier to crack, no existing competition.
2. **Save-file editor is the smallest deliverable** with the highest user value.
3. **A scenario authored on Genesis SRAM could in principle be transferred to SNES** if the layouts share enough structure — worth checking once both are mapped.

# Gemfire modding — initial research

Compiled 2026-04-25 at the start of this project. The point is to map the existing scene before deciding what's worth building.

## What Gemfire is

- Koei strategy game, "feudal-fantasy" reskin of their Romance of the Three Kingdoms II engine.
- 30 provinces in the kingdom of Ishmeria, 11 ruling families, 7 magical gems, ~64 named officers, 16 mercenary unit types (drque.net's published list of 15 omits Highlanders — both ROMs include it).
- US release order: NES (Mar 1992) → Genesis (Nov 1992) → SNES (Dec 1992). The SNES port is the polished/final one, not the lead.
- The SNES US version is `GEMFIRE` (1MB LoROM, internal title "GEMFIRE", standard SNES header at $7FC0).
- Genesis US version is "Gemfire (USA)" (1MB, Koei product code T-76036, region "U", SRAM at $200001+).
- NES US version is 512KB (256KB PRG, 256KB CHR, mapper 5 / MMC5).

## Existing tooling

### Koei Decompress (darkmoon2321)
[romhacking.net/utilities/1083](https://www.romhacking.net/utilities/1083/)

Windows tool that handles the compression scheme used in Gemfire, ROTK III, ROTK IV, and Genghis Khan II on SNES. Confirmed working with Gemfire. Output:

- `.kdf` — decompressed payload
- `.kcf` — recompressed payload (round-trips)
- `.dat` — metadata: hex offsets in the ROM and sequence sizes

This is the only published primitive for getting at compressed graphics/data/text blocks in the Gemfire SNES ROM.

### Nightmare Modules for Gemfire SNES (PleaseYourName, ~2019)
- Module pack: [yadi.sk/d/vFHEwW7I3YME44](https://disk.yandex.com/d/vFHEwW7I3YME44)
- Editor: [Nightmare on RHN](https://www.romhacking.net/utilities/1307/) (general-purpose ROM module editor)
- Photos: [ibb.co/album/m453WF](https://ibb.co/album/m453WF)

PleaseYourName built Nightmare modules covering **all characters, families, and scenarios** in the SNES version. Requires headerless US ROM. This is effectively the highest-level existing scenario editor — the in-place answer to "I want to make a scenario".

Credit in their post: data came from "DragonAtma and everyone involved in the data diving thread" on the GameFAQs Gemfire board.

### DragonAtma's Gemfire notes (.ods, RHN doc 867)
[romhacking.net/documents/867](https://www.romhacking.net/documents/867/)

Spreadsheet of mapped data — likely the input to the Nightmare modules. Direct download served behind Cloudflare anti-leech; need a real browser session to fetch. **TODO: get this file and inventory what's mapped.**

## Existing hacks

### Dawn of Ishmeria (DragonAtma, v1.2 2020-11-21)
[romhacking.net/hacks/5551](https://www.romhacking.net/hacks/5551/)

- Status: complete
- Format: IPS, both headered and unheadered
- Base: Gemfire (USA) SNES
- Theme: prequel — set ~25 years before vanilla, three-quarters of officers replaced with new (younger) faces
- Rebalance: all seven gem-bearing wizards roughly equal, fifth-unit pricing made monotonic (cost ↑ ⇒ power ↑), fame requirements removed from fifth units
- License note: author granted Koei Tecmo permission to use the mod

This is the single most ambitious published Gemfire mod. Anything we build should either (a) live alongside it as a different fork, or (b) be a better tool that Dawn of Ishmeria itself could be authored in.

## Existing reference / fan resources

- [gemfire.drque.net](https://gemfire.drque.net/) — Andrew Que's "complete guide" (paused 2014, still up). Documents scenarios, families (11), gems (7), mercenaries (15), provinces (30 with names), people (~64). Lists the names but doesn't fully document data formats. Author also has an in-progress JS remake based on the PC version.
- [GameFAQs Gemfire board](https://gamefaqs.gamespot.com/snes/588352-gemfire) — DizavidHZ's *Scenario Edit Guide*, admtanaka's full FAQ, DragonAtma's *General Stats* guide. The "data diving thread" referenced by other modders lives here too.
- [koei.fandom.com/wiki/Gemfire](https://koei.fandom.com/wiki/Gemfire)

## What's NOT documented (gaps to fill)

These are the holes in the public record as of writing:

1. **No public Data Crystal page** for Gemfire (no published RAM/ROM map). DragonAtma's `.ods` is the closest thing and is undated/private to RHN.
2. **No published disassembly** of any Gemfire version.
3. **No tooling for the Genesis or NES versions** that we could find. All editors target SNES US.
4. **Save file (SRAM) format** is not documented anywhere we could find.
5. **No scenario-format documentation** that's distinct from the Nightmare modules — the modules let you change scenarios but don't describe the on-disk layout.

## What gives us the most leverage

Ranked by build-cost vs. utility (updated after the SNES↔Genesis comparison — see [`snes-vs-genesis.md`](snes-vs-genesis.md)):

1. **Save-file editor** (no ROM hacking needed). DizavidHZ's GameFAQs guide is "exploit the game's save-state mechanics to author a custom scenario via the death-of-rival glitch". A SRAM editor does that in seconds. Composes with any existing hack including Dawn of Ishmeria.
2. **Genesis text editor.** Genesis stores all in-game text as plaintext ASCII. Officer names, scenario intros, random event dialogue — all directly hex-editable. No published tool exists for this. An afternoon of work, immediately useful.
3. **Open-source the .ods notes as Markdown / CSV** so they're diffable, reviewable, and the source-of-truth for everyone else. Blocked on getting the .ods through Cloudflare.
4. **Genesis scenario/data ROM map.** Same content as SNES (confirmed via shared localization tables) but with no compression layer to fight. Higher reverse-engineering yield per hour than SNES.
5. **YAML/JSON → IPS pipeline.** Author scenarios in text, compile to a patch. Replaces the Nightmare workflow with something diffable in git. Bigger lift; do after the format is mapped.

## Open questions for the user

- Do we care about Genesis or NES, or are we SNES-only?
- Is the goal one really polished mod (à la Dawn of Ishmeria) or a toolkit other people use?
- Do we need original artwork (officer portraits, gem icons), or are we strictly mechanics?
- Is paper-mode-style validation (run mod through an emulator headlessly, assert key in-game outcomes) in scope?

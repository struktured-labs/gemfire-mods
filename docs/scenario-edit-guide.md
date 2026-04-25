# In-game scenario authoring (no ROM modding required)

This is a summary of [DizavidHZ's *Scenario Edit Guide*](https://gamefaqs.gamespot.com/snes/588352-gemfire/faqs/71083) on GameFAQs. The original is copyrighted by the author and explicitly restricted to GameFAQs and Neoseeker; we don't mirror it. We capture the *technique* in our own words because it's important context for what kind of "scenario editing" the Gemfire community already does without touching the ROM.

## The core idea

Gemfire's AI is exploitable. By starting a 2-player game, manipulating the second family until it owns nearly everything and then dies of old age with no heirs, the game enters a glitch state where each of that family's vassals splinters into a new one-province family. You end up playing a single-province game against ~28 newly created mini-families on a board you've pre-configured.

Result: a custom map (which families exist, where, with what gems / cultivation / garrison / officer roster) without ever touching the ROM.

## Setup recipe (paraphrased)

1. **Start a 2-player game**, ideally Scenario 2 ("Flax's Shame"). One controller can drive both.
2. **Pick player 1** as your real ruler — youngest available, or one with the youngest heir, so they outlive the setup phase.
3. **Pick player 2** ("the dying family") as someone with no heirs (e.g. Erik of Flax) or all heirs banishable.
4. Play normally; the dying family eats the map, including the surviving (player 1) family's territory until only one province remains.
5. Save/attack/retreat/banish to remove every heir of the dying family (no successor).
6. Pre-position vassals in whichever provinces you want to splinter into new families. Provinces under direct rule will become *empty* after the glitch — exploit this to seed contested zones.
7. **Let the dying ruler die of old age.** With no heirs, the family vanishes, vassals become independent, gems are randomly redistributed, and the player-1 family is left in one province surrounded by ~28 micro-states.

## Pre-baked variants (DizavidHZ's setups)

| Name | Configuration | Effect |
|------|---------------|--------|
| Chaos | Vassals in all 28 splintered provinces, dying family hoards 6/7 gems | Mass war kicks off immediately |
| Virus | Vassals in every other province, max resources (999/999/999) | Empty zones get seeded slowly, then collide — pandemic-style spread |
| Four Corners | Player + 3 starting families in provinces 8/3/26/30, everything else empty | Slow expansion, each axis develops differently |
| East vs. West | Four Corners + extra families along columns 13/14 and 18 | Coastal-line theaters |

## Fast tricks worth knowing

- **Defection invitations.** Some officers defect within ~3 invites: Aiden, Melgan, Bradley, Raith, Pender. Direct family members never defect except via failed-ransom recruit.
- **Starvation attack.** Send 1 troop, retreat — costs the defender a day's food. Repeat until they have 0–1 days, then attack for real. Saves troops on hard-to-reach provinces.
- **Surrender.** Once you dominate, families with ≤2 territories will surrender to you, bringing all their vassals (no defection scatter). Exception: Lankshire (King Eselred) never surrenders.
- **Flying mercs.** Wyvern and Gargoyles bypass terrain. Useful in river-heavy provinces (Londre = #22).

## Why this matters for the project

This entire guide describes "scenario authoring" as a multi-hour in-game ritual that exploits the same family-extinction glitch every time. The implication for ROM hacking:

- The data being mutated through that ritual lives in **SRAM** (the save), not the ROM. So a save-file editor would do all of this in seconds.
- DragonAtma's notes and the Nightmare modules let you author scenarios *into the ROM*, which is more permanent and shareable but requires the editor.
- We could add a third option: a CLI that reads/writes the SRAM scenario directly. That's a smaller, faster project than full ROM hacking, and the artifact is a `.srm` file someone can just load.

Worth investigating before committing to ROM-only tooling.

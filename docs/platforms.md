# Platforms

Per-platform ROM facts confirmed by inspecting the user's local copies on 2026-04-25.

## SNES (Super Nintendo)

- File: `Gemfire (USA).sfc`
- Size: 1,048,576 bytes (1 MiB) — no copier header
- Internal title: `GEMFIRE` (at $7FC0)
- Mode: LoROM
- ROM type byte: $00 (ROM only)
- ROM size: $0A (1 MB)
- SRAM size: $03 (8 KB)
- Region: $01 (US/NTSC)
- Old license: $33
- Version: $00
- Checksum: $9625 / complement $A473 (verified self-consistent)
- Layout note: vanilla LoROM, banks $80–$8F mirror $00–$0F, last bank holds the header.

This is the canonical target for tooling — every public hack and editor assumes this exact ROM.

## Genesis / Mega Drive

- File: `Gemfire (USA).md` (extracted from `Gemfire.zip`)
- Size: 1,048,576 bytes (1 MiB)
- Console name: `SEGA MEGA DRIVE` (at $0100)
- Copyright: `(C)T-76 1992.MAR` (T-76 is Koei)
- Domestic name (kana): present, JP transliteration of "GEMFIRE"
- International name: `GEMFIRE`
- Product code: `GM T-76036 -10`
- Region: `U` (USA)
- SRAM: present, range $200001–$203FFF (`RA. . ... ?.    `)
- Mapper: standard Sega cart, no extra hardware

The Genesis version is the same era and (we suspect) the same engine port as SNES, but **no public modding tooling targets it**. If we want it modded, we drive the work ourselves.

## NES (Nintendo Entertainment System)

- File: `Gemfire (U).nes`
- Size: 524,304 bytes (16-byte iNES header + 524,288 bytes data)
- iNES header: `4E 45 53 1A`
- PRG ROM: 16 × 16 KB = 256 KB
- CHR ROM: 32 × 8 KB = 256 KB
- Flags6 / Flags7: $52 / $00 → mapper 5 (MMC5)
- Mirroring: vertical
- Region: USA

The NES version is technically the most complex (MMC5 = bank-switching, expansion audio, vertical scroll split). Out of scope for now.

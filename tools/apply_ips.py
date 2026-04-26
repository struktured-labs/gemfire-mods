#!/usr/bin/env python3
"""Apply an IPS patch to a ROM. No dependencies.

Usage:
    apply_ips.py <patch.ips> <input.rom> <output.rom>

Supports:
  - Standard IPS records (3-byte offset, 2-byte size, payload)
  - RLE records (size=0, then 2-byte rle-size, 1 byte to repeat)
  - 'EOF' terminator
  - Optional truncation extension (3-byte trailing length after EOF)
"""
import sys
import hashlib
from pathlib import Path


def apply(patch_bytes: bytes, rom: bytearray) -> bytearray:
    if patch_bytes[:5] != b"PATCH":
        raise ValueError("not an IPS patch — missing 'PATCH' header")
    i = 5
    while i < len(patch_bytes):
        if patch_bytes[i:i + 3] == b"EOF":
            i += 3
            # optional truncation extension
            if i + 3 <= len(patch_bytes):
                trunc = int.from_bytes(patch_bytes[i:i + 3], "big")
                rom = rom[:trunc]
            return rom
        offset = int.from_bytes(patch_bytes[i:i + 3], "big")
        size = int.from_bytes(patch_bytes[i + 3:i + 5], "big")
        i += 5
        if size == 0:
            # RLE record
            rle_size = int.from_bytes(patch_bytes[i:i + 2], "big")
            byte = patch_bytes[i + 2]
            i += 3
            end = offset + rle_size
            if end > len(rom):
                rom.extend(b"\x00" * (end - len(rom)))
            for j in range(offset, end):
                rom[j] = byte
        else:
            payload = patch_bytes[i:i + size]
            i += size
            end = offset + size
            if end > len(rom):
                rom.extend(b"\x00" * (end - len(rom)))
            rom[offset:end] = payload
    raise ValueError("patch ended without 'EOF' marker")


def main():
    if len(sys.argv) != 4:
        print(__doc__)
        sys.exit(2)
    patch_path = Path(sys.argv[1])
    in_path = Path(sys.argv[2])
    out_path = Path(sys.argv[3])

    patch = patch_path.read_bytes()
    rom = bytearray(in_path.read_bytes())
    print(f"input rom:  {in_path}  ({len(rom):,} bytes)")
    print(f"patch:      {patch_path}  ({len(patch):,} bytes)")

    result = apply(patch, rom)
    out_path.write_bytes(result)
    sha = hashlib.sha256(result).hexdigest()
    print(f"output rom: {out_path}  ({len(result):,} bytes)")
    print(f"sha256:     {sha}")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Launch a ROM on a running MiSTer FPGA via the mrext HTTP API.

Why this script over `echo load_core /tmp/x.mgl > /dev/MiSTer_cmd`:
  - mrext's /api/launch builds the MGL itself, so paths with spaces and
    odd filenames just work.
  - mrext also populates /tmp/CURRENTPATH and the gameRunning WS status,
    which means screenshots and game-detection downstream tooling work.

Usage:
    mister_launch.py <absolute_rom_path_on_mister>
    mister_launch.py "/media/fat/games/SNES/Hacks/Gemfire - Dawn of Ishmeria.sfc"
"""
import json
import sys
import urllib.request


MRE_HOST = "mister"
MRE_PORT = 8182


def launch(rom_path: str) -> dict:
    body = json.dumps({"path": rom_path}).encode()
    req = urllib.request.Request(
        f"http://{MRE_HOST}:{MRE_PORT}/api/launch",
        data=body,
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=10) as r:
        raw = r.read().decode()
    try:
        return json.loads(raw)
    except json.JSONDecodeError:
        return {"raw": raw}


def main():
    if len(sys.argv) != 2:
        print(__doc__)
        sys.exit(2)
    print(launch(sys.argv[1]))


if __name__ == "__main__":
    main()

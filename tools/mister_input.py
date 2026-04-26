#!/usr/bin/env python3
"""Send keystrokes to MiSTer via the mrext WebSocket on port 8182.

Protocol (discovered by reading the mrext SPA bundle and probing live):
  kbdRaw:<linux_keycode>      — full press+release
  kbdRawDown:<linux_keycode>  — key down only
  kbdRawUp:<linux_keycode>    — key up only

Status is pushed unsolicited as `key:value` text frames, e.g.
  coreRunning:SNES
  gameRunning:<path>
  indexStatus:n,n,0,0,
"""
import asyncio
import sys
import time

import websockets


# Linux input event codes for the keys the MiSTer SNES core defaults to.
# Stock keyboard mapping (see core docs / Menu): arrows + Z/X/A/S/D/C + Enter/RShift.
KEYS = {
    "UP":     103,  # KEY_UP
    "DOWN":   108,  # KEY_DOWN
    "LEFT":   105,  # KEY_LEFT
    "RIGHT":  106,  # KEY_RIGHT
    "A":       45,  # KEY_X        — SNES A
    "B":       44,  # KEY_Z        — SNES B
    "X":       31,  # KEY_S        — SNES X
    "Y":       30,  # KEY_A        — SNES Y
    "L":       32,  # KEY_D        — SNES L
    "R":       46,  # KEY_C        — SNES R
    "START":   28,  # KEY_ENTER
    "SELECT":  54,  # KEY_RIGHTSHIFT
    "OSD":     88,  # KEY_F12
}


WS_URL = "ws://mister:8182/api/ws"


async def _send_seq(seq):
    async with websockets.connect(WS_URL) as ws:
        # Drain any unsolicited status frames so we don't block on them later.
        deadline = time.monotonic() + 0.4
        while time.monotonic() < deadline:
            try:
                msg = await asyncio.wait_for(ws.recv(), timeout=0.1)
                print(f"  status: {msg}")
            except asyncio.TimeoutError:
                break

        for action in seq:
            if isinstance(action, (int, float)):
                await asyncio.sleep(action)
                continue
            if action.upper() not in KEYS:
                raise SystemExit(f"unknown key: {action}")
            keycode = KEYS[action.upper()]
            cmd = f"kbdRaw:{keycode}"
            print(f"  send: {cmd:18s}  ({action.upper()})")
            await ws.send(cmd)
            # Default inter-press dwell so the core has time to advance frames.
            await asyncio.sleep(0.15)


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        print("Usage: mister_input.py <KEY> [KEY|delay_seconds] ...")
        print("Keys:", " ".join(KEYS.keys()))
        sys.exit(2)

    raw_args = sys.argv[1:]
    seq = []
    for a in raw_args:
        try:
            seq.append(float(a))
        except ValueError:
            seq.append(a)

    asyncio.run(_send_seq(seq))


if __name__ == "__main__":
    main()

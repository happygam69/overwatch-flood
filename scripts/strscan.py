#!/usr/bin/env python3
"""Resolve every data address mentioned in a chunk through the shipped pool.

usage: python scripts/strscan.py chunks/chunk_0267.txt [window] [--all]

Prints one line per distinct address that has a pool page nearby, so `DAT_`/`uRam_`
name pages become readable while reading a chunk. Stripped pages carry their recovered
identity (class / field / enum value / owner) — see `../strlookup.py` for the row shape.

The trailing summary says why the rest did not resolve. Most addresses in a chunk are
never strings: `.text` mentions are code, and `.data BSS` is the section's virtual tail
(virtual size 0xCC43BC against 0x333600 file-backed bytes) holding zero-initialised
runtime globals, so no file bytes exist to decode. `--all` lists those too.

Across all 2,228 chunks: 213,042 of 227,104 file-backed `.data` mentions resolve (93.8%);
`.rdata` is only 1.7% because vtables and float tables dominate it, not name pages.

Read-only, standard library only, no paths outside this repository.
"""
import bisect
import collections
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from strlookup import load, region, show  # noqa: E402

RX = re.compile(r"(?<![0-9a-fA-F])(14[0-9a-fA-F]{7})(?![0-9a-fA-F])")


def main(path, window=0x60, show_all=False):
    rows = load()
    keys = [r[0] for r in rows]
    with open(path, encoding="utf-8", errors="replace") as fh:
        body = fh.read()
    seen = {int(m.group(1), 16) for m in RX.finditer(body)}

    tally = collections.Counter()
    resolved = collections.Counter()
    for addr in sorted(seen):
        reg = region(addr)
        tally[reg] += 1
        i = bisect.bisect_right(keys, addr) - 1
        hit = None
        if 0 <= i < len(rows) and addr - keys[i] <= window:
            hit = (rows[i], addr - keys[i])
        elif 0 <= i + 1 < len(rows) and keys[i + 1] - addr <= window:
            hit = (rows[i + 1], keys[i + 1] - addr)
        if hit:
            r, delta = hit
            resolved[reg] += 1
            sign = "+" if delta >= 0 else "-"
            print("0x%X (%s0x%X) %s" % (addr, sign, abs(delta), show(*r[1:])))
        elif show_all:
            print("0x%X %s" % (addr, "-- no pool page (%s)" % reg))

    n = len(seen)
    print("%d of %d addresses resolved" % (sum(resolved.values()), n), file=sys.stderr)
    for reg, cnt in tally.most_common():
        if not resolved[reg]:
            print("  %-10s %6d  no pool page" % (reg, cnt), file=sys.stderr)
        else:
            print("  %-10s %6d  %6d resolved (%.1f%%)"
                  % (reg, cnt, resolved[reg], 100.0 * resolved[reg] / cnt), file=sys.stderr)
    return 0


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        raise SystemExit(2)
    args = sys.argv[1:]
    every = "--all" in args
    args = [a for a in args if a != "--all"]
    raise SystemExit(main(args[0], int(args[1], 0) if len(args) > 1 else 0x60, every))

# CODE_MAP — cumulative map of the systematic `.text` read

**Read in full before every pass; update after every pass. Hard budget: ≤300 lines.**
Per-pass narrative, highlights and method notes live ONLY in `ranges/<first>-<last>.md`.
Cumulative numbers are machine-maintained in `state.json` (via `scripts/pass_measure.py`)
— never hand-add them here; quote `state.json` totals instead. The previous long-form
map (988 lines, pass narrative chains) is preserved verbatim in `CODE_MAP_ARCHIVE.md`.

## Files

| file | role |
|---|---|
| `chunks/chunk_NNNN.txt` | corpus, address order; the one-line `Removing unreachable block` warnings were stripped in place 2026-11-21 (668,998 lines / 42,145,998 B; per-chunk counts in `index.json`, pre-strip index `index.pre_strip.json`). Every code line is present. |
| `index.json` | per-chunk bytes / first / last — source of truth for coverage |
| `state.json` | machine ledger: next_chunk, per-pass entries, cumulative totals, all 7,952 registration hashes, all 326 `{id,hash}` rows with match flags |
| `scripts/pass_measure.py` | the canonical per-pass measurement; stdout quoted verbatim in records; matches any function header name (1,204 Ghidra-named functions in chunks ≥235 are not `FUN_`-named) |
| `census.py` / `cluster.py` | ad-hoc per-chunk census / body-normalized family clustering (skeleton detector) |
| `ranges/*.md` | per-pass records, named by `.text` range — the evidence base |

## Coverage

Total corpus: 2,228 chunks, 119,757 functions, 42,864,695 B `.text` (raw index bytes 325,787,798).

| pass | chunks | `.text` range | functions | Σ `size=` | record |
|---|---|---|---|---|---|
| 1 (pre-protocol) | `0000`–`0013` | `0x140001000`–`0x1400c2ed0` | 2,303 | 412,670 | `ranges/0x140001000-0x1400c2ed0.md` |
| 2 (partial) | `0014`–`0022` | `0x1400c2f90`–`0x14010bf30` | 1,183 | 228,057 | `ranges/0x1400c2f90-0x14010bf30.md` |
| 3 | `0023`–`0029` | `0x14010c120`–`0x14012bcd0` | 408 | 117,713 | `ranges/0x14010c120-0x14012bcd0.md` |
| 4 | `0030`–`0037` | `0x14012bee0`–`0x140156840` | 524 | 155,444 | `ranges/0x14012bee0-0x140156840.md` |
| 5 (7 of ~12 chunks) | `0038`–`0044` | `0x140156950`–`0x140175867` | 375 | 116,193 | `ranges/0x140156950-0x140175867.md` |
| 6 | `0045`–`0052` | `0x140175ab0`–`0x14019d171` | 519 | 146,118 | `ranges/0x140175ab0-0x14019d080.md` |
| 7 | `0053`–`0060` | `0x14019d180`–`0x1401d265d` | 740 | 186,305 | `ranges/0x14019d180-0x1401d265d.md` |
| 8 | `0061`–`0067` | `0x1401d2660`–`0x1401ef8e0` | 401 | 115,925 | `ranges/0x1401d2660-0x1401ef8e0.md` |
| 9 | `0068`–`0075` | `0x1401efa00`–`0x1402039cd` | 218 | 78,716 | `ranges/0x1401efa00-0x1402039cd.md` |
| 10 | `0076`–`0083` | `0x1402039d0`–`0x1402169b5` | 235 | 74,025 | `ranges/0x1402039d0-0x1402169b5.md` |
| 11 | `0084`–`0091` | `0x140217cf0`–`0x14024f2ad` | 765 | 205,857 | `ranges/0x140217cf0-0x14024f2ad.md` |
| 12 | `0092`–`0099` | `0x14024f2c0`–`0x14026204e` | 226 | 74,834 | `ranges/0x14024f2c0-0x14026204e.md` |
| 13 | `0100`–`0107` | `0x140262050`–`0x140275350` | 258 | 74,840 | `ranges/0x140262050-0x140275350.md` |
| 14 | `0108`–`0115` | `0x140275450`–`0x140298b11` | 465 | 129,912 | `ranges/0x140275450-0x140298b11.md` |
| 15 | `0116`–`0123` | `0x140298b20`–`0x1402c16e0` | 510 | 143,192 | `ranges/0x140298b20-0x1402c16e0.md` |
| 16 | `0124`–`0131` | `0x1402c17e0`–`0x1402e9f70` | 541 | 147,915 | `ranges/0x1402c17e0-0x1402e9f70.md` |
| 17 (10-chunk override) | `0132`–`0141` | `0x1402ea070`–`0x1403220c0` | 777 | 209,051 | `ranges/0x1402ea070-0x1403220c0.md` |
| 18 (9-chunk pass) | `0142`–`0150` | `0x1403222e0`–`0x14034ed30` | 562 | 162,088 | `ranges/0x1403222e0-0x14034ed30.md` |
| 19 (10-chunk override) | `0151`–`0160` | `0x14034ede0`–`0x1403857a0` | 727 | 196,086 | `ranges/0x14034ede0-0x1403857a0.md` |
| 20 (10-chunk override) | `0161`–`0170` | `0x1403858a0`–`0x1403ac1e0` | 522 | 144,458 | `ranges/0x1403858a0-0x1403ac1e0.md` |
| 21 (11-chunk override) | `0171`–`0181` | `0x1403ac370`–`0x1403e7590` | 771 | 214,614 | `ranges/0x1403ac370-0x1403e7590.md` |
| 22 (11-chunk override) | `0182`–`0192` | `0x1403e7730`–`0x1404191d0` | 630 | 181,579 | `ranges/0x1403e7730-0x1404191d0.md` |
| 23 (10-chunk) | `0193`–`0202` | `0x1404192e0`–`0x140451060` | 738 | 203,154 | `ranges/0x1404192e0-0x140451060.md` |
| 24 (11-chunk override) | `0203`–`0213` | `0x140451160`–`0x140473f50` | 457 | 132,700 | `ranges/0x140451160-0x140473f50.md` |
| 25 | `0214`–`0221` | `0x1404740d0`–`0x140495d90` | 453 | 126,840 | `ranges/0x1404740d0-0x140495d90.md` |
| 26 | `0222`–`0229` | `0x140495e90`–`0x1404bfd20` | 557 | 148,986 | `ranges/0x140495e90-0x1404bfd20.md` |
| **total** | **230, contiguous** | `0x140001000`–`0x1404bfd20` | **15,865** | **4,127,272** | machine-verified (`state.json`) |
| pending | `0230`–`2227` | `0x1404bfe00`→ | — | — | resume at `chunk_0230` |

Machine-verified cumulative (`state.json` after pass 26): files 15,865 (13.25 % of functions),
Σ `size=` 4,127,272 (9.63 % of `.text`); classes reg 7,952 / wrapper 1,954 / builder 1,717 /
sorted 280 / atexit 261 / record 326 / other 3,375; registrations 7,952, all hashes distinct;
`d4f30` 1,188, `d4f70` 1,350, `d4fb0` 4,492, `c2d70` 4,212, `c2d50` 326, `c7880` 261,
`atexit` 266; records 326, **all 60 new rows matched** (two pre-16 flags stay stale =
Corrections 11). Pass 26 ran the 8-chunk protocol default; highest `other` count so far (92)
because of the new settings family (Corrections 15 supersedes the size rule).

## Corrections ledger (machine-derived; supersedes prose in older records)

1. **`{id,hash}` records match 75/75, not 74/75.** Pass 15's "unmatched" hash `0x3fd91271` (id `0x35`) is the registration hash of `FUN_140290c50` (chunk `0114`). Thread 43 CLOSED. Pass 16 adds 23 rows; pass 17 adds 45.
2. **Sorted-insert builders: 280 cumulative** after pass 26 (249→+31, first since pass 23; machine-reconciled per chunk 0/4/3/9/1/8/4/2); use `state.json`.
3. **Nested-atexit builders: 261 cumulative**; shapes 542/558-B this pass; initializer families grow per pass.
4. **Provenance caveat:** passes 1–15 records state counts without a quoting script (their ad-hoc scripts were not kept). All 26 passes' `files`/Σ `size=` are reproduced by `scripts/pass_measure.py`.
5. **`--update` is forward-only; `--init` wipes the pass list.** `--update` over an already-counted range double-counts and rewinds `next_chunk`; repair is `--init` — why `state.json` lists only passes 16–26.
6. **There is no shutdown table and no "move".** Shutdown rows are per-object global slots scattered by
   the linker (`0x1438e…`, `0x143ce7…`, `0x143e5e/5f/6a/6e/77/7c…`, `0x143c3ab20/ba40`, `0x143ec5/6…`,
   `0x143e92/94…`, pass 26: `0x144101c90`, `0x144123ab0–af0`, `0x144126320–378`, `0x14412cd58/da0`,
   `0x14412e078–0b0`, `0x144136068–0a8`, ciphertext-page `0x14398bc98–d58`). The code addresses each absolutely.
7. **`pass_measure.py` prints no `ciphertext band:` line** — its `CTXT` regex needs `DAT_1438` + 6 hex
   digits; the band is now `0x1439a…`. Ciphertext extremes in records are read from the text, both
   addresses cited (pass 26: key `0x14397d218`, payload `0x1439a9b2c`).
8. **`pass_measure.py` `zones:` filter** prints only class `reg`/`record` runs and runs with `cnt>=3`;
   1–2-function builder/wrapper runs are absent from the skeleton (they exist in the text).
9. **`record-hash = registration-hash` is a rule; the two historical exceptions are resolved (11).** Ids `0x3e`/`0xcb` bind `0x39091531`, registered in pass 19. Do not treat the two stale `state.json` flags as exceptions.
10. **The 178-B third field is an alias registration hash, not a flag.** Pass 17 measured three pairs; pass 26 adds `0x129`→`0xab64f377` aliasing `0x93c5fe63` = `FUN_1404b3f50` (253-B, size 8). Row layout = `{id, hash, alias}`; most third fields are 0.
11. **Corrections 9 is closed by direct evidence.** `FUN_14036bb60` (chunk `0156`) registers `0x39091531` (`&DAT_143f803a0`, size `0x30`), the hash of record ids `0x3e`/`0xcb`. The two `state.json` rows stay `matched:false` (the matcher never revisits old rows); treat them as stale.
12. **Roots alternate; "static-root era over" is retired.** Pass 26 roots sit almost entirely on registration outputs (`&DAT_144127550` ×17, `&DAT_1441156d0` ×12, `&DAT_144127a50` ×9 …); static `0x143cf/d…` roots are now the minority (×3/×2/×2). Regime is per-block, not a timeline.
13. **Allocator symbol ≠ allocator.** Per-TU one-arg symbols (`140f80f80`, `14114d8a0`; pass 26 adds `141367110`, `1412b5440`, `1418e82e0`, `1413676c0`, `141901b40`, `141901720`, `141901810`, `140f7b550`, `14190df80`, `14191bd90`, `1419254a0`, `14192a730`, `141367c50`); key on the shape.
14. **The sorted-insert middle call is the ordinary pre-step slot.** Not a second decrypt stage.
15. **Minimum registered size is 3, not 8** (pass 26: `FUN_1404aad50`, 242-B no-output, size 3, align 1;
    align-4 rows of sizes 0xc/0x1c/0x10 also seen). Overall size span now 3–0x3bc0.

## What the code is — cumulative synthesis (26 passes; evidence unless marked [inference])

`.text` is catalogued in entry-address order. After 230 chunks the cursor is at `0x1404bfd20`
(13.25 % of functions, 9.63 % of `.text`). Names printed `func_0x…` have **no decompiled body
anywhere in this dump** — the registrar `func_0x1421cd360`, decryptors `d4f30`/`d4f70`, writer `c2d50`,
helper `c2d70`, shutdown registration `c7880`, raw pointers `0x140fd9670`/`0x140f7b210` and
`SUB_140551380`; their bodies need the full Ghidra project/EXE. Higher-address references are later,
unread corpus — not missing.

**Four layers, in address order:**

1. **Library preamble** `0x140001000`–`0x140039fc0`. ISA-L/igzip-shaped DEFLATE inflate (12 fns,
   64-bit MSB-aligned bit buffers, `vpinsrb` fast path); `nvapi_QueryInterface` bootstrap with lazy
   per-id caches and a Wine probe; 53 identical NVAPI entry wrappers; `Initialize`/`Unload`.
2. **NVIDIA driver-loading shim** `0x14003a230`–`0x14003d330`. Replacement `LoadLibrary` for
   `nv*.dll`: D3DKMT, SetupAPI, service image paths, Khronos registry keys. Source of all 45 string
   literals in the read range.
3. **CRT/C++ static-init sea** `0x14003ffe0`–`0x1400fa760`. Five generator templates: the 181-B
   MSVC magic-static descriptor (**2,451** instances: `{+0x20 tag 1|2, +0x40 ctor, +0x48 vtable/FUN,
   +0x50 third, +0x58 payload, +0x60 shared PTR}` under a TLS guard), 209-B locale/facet statics
   (354), 58-B event-registration thunks (284), 134-B XOR-40 + cipher registrations (61), 37-B
   `_onexit` stubs; pass-1 tail (`0009`–`0013`): 864 descriptors + 39 shared `PTR_DAT_14386a…` markers.
   [inference: generated per-record class/vtable descriptors; consumer ahead.]
4. **Typed registry machine** `0x1400fbcb0`–`0x1404bfd20` (passes 2-tail–26) — the substance of the
   read, described next. No gameplay, network, asset or UI code; the only named subsystem is
   CompilerIDFilter. **Pass 26 adds a fifth family inside layer 4** (the settings/variable
   registrars, below) — the first new construct since the registry machine began.

**The registry machine — nine cooperating constructs/variants:**

- **Name buffers.** Every registration/builder/settings row carries an XOR-8 ciphertext: 8-byte key at
  `+0`, 24-bit length at `+8`, done-flag `+0xb`, payload `+0xc`; `buf[i] ^= key[i & 7]`. Band
  `0x1438b8e50`–`0x1439a9b2c` (pass 26 max; new page from ~`0x1439a8ba0` serves the settings family).
  Plaintext never decoded.
- **Registration** — `func_0x1421cd360(out, ciphertext, hash32, 0, size, align, flags, 0, token,
  a10…a14, 0, 0, a16, a17, base)`: **7,952 instances, 7,952 distinct hash32 — zero reuse**
  (machine-checked). `size` **3**–`0x3bc0` overall (Corrections 15), `align` 8 default, 1/4/0x10
  outliers; `flags` 0 default, 1/2/3/4/5/6/7/8/10/0xb/0x51/**0x80000000** known (pass 26 adds the
  high-bit flag: `FUN_1404a5fa0`, 258-B, size 0x140); 263/266/267-B rows carry 64-bit tokens
  (pass 26: 73 uses / 69 distinct, top `0x53b89a1dc661b5dd` ×3 consecutive; one no-output 252-B row
  carries a token); **266-B/256-B rows (pass 26) set a16 from a runtime global** (`_DAT_14410ff88`,
  `_DAT_144111038`, `_DAT_144111198`, `_DAT_14410fb68`, `_DAT_1441100f8`, `_DAT_144110318`) where
  earlier passes used constants `FUN_14131dXXX`; `base = out − 0xa0` verified again in every row read
  this pass [inference: header slot, no reader seen].
- **No-output registration** — 242/246/252/257-B (first overall `0x140341b30`, pass 18); args 10–18 = `FUN_140548d00, 0x140f7b210, FUN_140548f80, FUN_14053a070, FUN_140548d00, 0, 0, 0, 0` — **arg17 = arg18 = 0**. Pass 26: **×40 return** (after 24's 0, 25's 8), incl. align-4 rows (0xc/0x1c/0x10), the size-3 align-1 row, one 252-B with token, one 242-B with flags 2 + a16 `FUN_1418e3430`. **First reader found: rootless sorted builder `FUN_1404a82b0` copies no-output row `&DAT_144121c50` into a 2-record table.** [inference: names/metadata registered without an instantiable object row; tables eat them.]
- **Builder** — 365/369/373/377/381/389/397/451/459/471/475/480/524/574-B: allocator/pre-step →
  inline XOR-8 decrypt → `d4f30/d4f70(&out,&buf,hash,0)` → `d4fb0` → store class root, instance ptr,
  flag. Row = `{+0x20 root, +0x28 instance, +0x30 0, +0x98 flag(1), +0x9c 0}`; the registered row IS
  the object header. 459/451-B and pass 26's **369-B/365-B rootless forms** store **no root**
  (`+0x20 = 0`). Two-buffer helpers `(size,&ct,0,hash)` ≥60, own hash each; **pass 26 helper hashes
  collide with reg/record hashes** (`0x6760479e` = reg `FUN_1404ac210` = record `0xa5`; `0xa7f15a16`
  = reg `FUN_14049d2f0` = record `0x7c`; `0x15be7741` serves both d4f70 and d4f30). New helpers
  `FUN_1410eaf40`/`FUN_141108960`/`FUN_140f7ade0`; allocator `FUN_141901810(0)` allocates size 0.
- **Copy wrapper** — 241-B / 231-B rootless / 244-B: no decrypt; `c2d70(&dst,&src)` + `d4fb0`; `src = row slot − 0x20`. Same five fields but flag **0** at `+0x98`; 231-B also stores root 0. 244-B stores `&PTR_s_CompilerIDFilter_*` + flag 1 into registration rows (×7) — the registry's named link into the CompilerIDFilter chain. Pass 26: 231-B rootless wrappers copy token-253-B and plain reg outputs.
- **Sorted-insert builder** — **280 instances** (pass 26: 31 × 507/510/515/523/524-B, first since
  pass 23); every one sorts exactly 2 56-B records keyed by the `uint` at `+8` (min-to-slot-0
  pre-swap, then insertion sort) + `d4fb0` + count = 2. Pass 26: decrypts flipped to **d4f30-heavy**
  (`0xb48f1d22` ×4 shared opener); **mostly rootless or rooted on reg outputs**; pre-step shapes:
  two no-arg calls, one allocator with two sizes (`FUN_1418d6420(0x4f0)`/`(0x540)`), two different
  allocators (`FUN_14190df80(0x120)`+`FUN_14191bd90(0x148)`), allocators of 0x120/400/0xc/0x18/
  0x28/0x30/0x58 B. [inference: tiny 2-entry lookup tables; they consume registry rows (finding 3).]
- **`{id,hash}` record** — 169/178-B; **326 instances**; pass 26 returns **×60, 60/60 matched**, every hash registered earlier in the same pass (in-pass binding). Ids span **`0x1`–`0x18b`** (pass 26 adds lowest `0x1` and new max `0x18b`). Many-to-one is normal: `0x58b3d0d0` has **30 ids**; `0xb792564` 2 (`0x4`, `0xf1`); `0x38733fcc`/`0xa3645d25` two each; `0xd3a5ca91` ×3. The 178-B third field is the **alias registration hash** (Corrections 10); pass 26 adds the first measured alias since pass 17: `0x129`→`0xab64f377`, alias `0x93c5fe63`. Source rows now also `0x144101c68`–`0x144135f98`.
- **Nested-atexit builder** — **261 instances** (526/542/558-B): writes a row into a **per-object global slot** (scattered, Corrections 6), initializer pointers from the 26+ families (pass 26 adds `&PTR_FUN_1431491a8`, `&PTR_FUN_14327d450`, `&PTR_LAB_14314b720`, `&PTR_FUN_14314a5e8`; some slots hold two or three pointers, the third often a reg output). Calls `atexit(&LAB_142f0…))` (atexit labels now to `0x142f16960`) and `c7880(&slot)` (one- or two-arg); two rows write slots into the ciphertext page (`0x14398bc98`–`0x14398bd58`); **c7880 slot `0x14412cd58` shared by two builders** (`FUN_1404af790`, `FUN_1404b0ee0`), extending pass 25's `0x143c3ba40` sharing. [inference: static-object destructor/shutdown.]
- **Settings/variable registrar (NEW, pass 26; the `other x91` zone)** — `0x1404b94e0`–
  `0x1404bfd20`, 91 functions: (a) 7 tiny stubs (32/37/46/92-B) calling
  `func_0x141c4aea0(&DAT_144137250,0x110)`, `FUN_1421d8650(&DAT_1441375f0)`,
  `func_0x141bb6770(&DAT_144137b48)` + `&PTR_FUN_143280560`, `func_0x141bb8e80` ×3, then
  `_onexit(&LAB_142f16bxx)`; (b) 84 `int` functions 209–399-B: 1–3 inline XOR-8 decrypts of names
  in the new ciphertext page, then **`FUN_141c58170(&DAT_14413xxxx, 0, &DAT_144140740|
  &DAT_144140758, &name, &DAT_142f7aa00|&name2)`** (×83 call sites, machine-counted), then a
  ~0x50-B descriptor: `+0` = one of `&PTR_FUN_142f7d350`/`&PTR_FUN_142f83a40`/`&PTR_FUN_142f8be60`/
  `&PTR_FUN_142f83a70`/`&PTR_FUN_143280838`/`&PTR_FUN_143280868` (6 initializers), float/int default
  fields (IEEE-754 `0x3f800000`=1.0f, `0x42c80000`=100.0f, `0x43480000`=200.0f, `0x447a0000`=1000.0f,
  `0x400ccccd`=2.2f, `0x3c23d70a`=0.01f, `0xbf800000`=−1.0f; ints `0x1000101`, `0x1000000`, 5, 8,
  300, 600, 2000), `+0x48`=1|0; descriptors land `0x144130570`–`0x14413b7a0` (644 stores,
  machine-counted). `_onexit` labels run **monotonically `0x142f16b90`→`0x142f172b0`** — one
  destructor label per function (91 distinct, machine-counted), unlike the shared `0x142f0…` atexit
  labels. 330-B variants add `FUN_141bb8bd0(&DAT,&DAT_1439af158)` ×2 + `func_0x141bb8e80` ×2;
  399-B `FUN_1404bd2e0` stores a pointer to a decrypted name. No canary, no TLS guard.
  [inference: settings/console-variable registration — decrypted name, default value table,
  type-descriptor pointer, per-object destructor; the zone continues into chunk `0230`.] Singleton
  companion: 122-B `FUN_14049f980` (guard + **`func_0x1421d6a10`** + flag writes `0x143985438=3`,
  `0x143985430=&DAT_143984f40` into the ciphertext page).

Also present: **15 CompilerIDFilter shells** storing one of 15 `&PTR_s_CompilerIDFilter_*` labels plus
payloads `&DAT_143eb63c0/67e0/6aa0/6940` — pass 17 proved those payloads are registration outputs, so
the chain roots are freshly registered types; the 244-B wrappers tie the registry to this chain.
Guard furniture: MSVC magic-static TLS guards + stack cookies; **every builder/sorted/atexit carries a
canary, no registration, wrapper, or settings function does**.
[inference: the sea registers part of the shader/compiler-filter machinery.]

**Passes 23–26 structural deltas (evidence).** Pass 23: 77–123-reg blocks, sextets `FUN_1417e20b0`→`FUN_141862c20`, per-TU allocator symbols + no-arg `FUN_1421c51f0…7780`. Pass 24: 174 regs all flags 0 / align 8, `base = out − 0xa0` 174/174. Pass 25: flags 4/2 return, builders root on registration outputs, 267-B = token+flags. **Pass 26 (286 regs, 557 files):** records ×60 and sorted ×31 return; no-output ×40; **roots on registration outputs become the dominant regime** (12/12 top root addresses are `0x1441xxxxx` outputs); new sizes 266/256/260-B with runtime-global a16; flags 1 ×3 / 2 ×3 / 3 ×1 / 0x80000000 ×1; align 4 ×3 / 1 ×1; sizes 3–0x1010; tokens 73/69 with a ×3 consecutive class; d4f30/d4f70 ratio flips (97/17, sorted-driven); **the settings/variable family appears** (`other` 92, highest of any pass); far reg-block families move to `0x1413bxxx` labels and `FUN_14191f4b0…FUN_14193bf50`; biggest block 57 regs (`0x1404abd10`–`0x1404af5d0`). [inference: tokens per-category; flags per-variant; settings family = the consumer-side registry the machine was building toward.]

**Where the data lives:**

| band | content |
|---|---|
| `0x1438b8e50`–`0x1439a9b2c` | XOR-8 name/payload ciphertext (+ 15 `PTR_s_CompilerIDFilter_*` labels; printable pre-XOR: `0x143970f0c`, `s_5L7rL_F_14397b58c`, `s_Pjbl_ii_14397ffb4`; shutdown slots `0x14397a4d0`–`0x14397a528` and `0x14398bc98`–`0x14398bd58` live inside; settings flag pair `0x143985430/438`; new settings page from ~`0x1439a8ba0`) |
| `0x143e99d90`–`0x144132d50` + earlier `0x143d/0x143e…` | registration outputs / instance slots; fresh page per block-pair (pass 26 reached `0x144132d50`; settings descriptors to `0x14413b7a0`; shared config globals `0x144140740`/`0x144140758`) |
| `0x143e4ac90`–`0x143ed6f90` + `0x143f198d8`–`0x143fe0b00` + `0x144101c68`–`0x144135f98` | `{id,hash,alias}` source rows, interleaved with output bands |
| shutdown slots — see Corrections 6 for the full scattered list (`0x1438e…`, `0x143c3…`, `0x143ec5/6…`, `0x14410/12/13…`) | nested-atexit/shutdown slots (**per-object, scattered**) |
| `0x143d01930`, `0x143d01a90`, `0x143d03780`, `0x143d04970`, `0x143d93520`, `0x143cfa130`, `0x1441e1bb0`, `0x143defd00`, `0x143f8e3d0`, `0x143ce2090`, `0x143f94670`, `0x143cfc6a0`, `0x143eb67e0`, `0x143e135e0`, `0x143e138a0`, `0x143fcaed0`, `0x143fca7f0`, `0x1440073e0`, `0x144005360`, `0x1440547f0`, `0x144058990`, `0x14405e0c0`, `0x143ecee70`, `0x143f803a0`, `0x143cef840` | far class roots / atexit payloads (**0x143f94670 is the closed shared root of 73+62 wrappers**; pass 26 static roots only ×3/×2/×2 + singletons `0x143f803a0`, `0x143ecee70`, `0x143ce2090`, `0x1441e1bb0`) |
| `0x143cf0000`–`0x143d05000` + far `0x143f8xxxx`–`0x143f94xxx`, `0x143eb6xxx`, `0x143ecee70`, `0x143ee0cd0` | class roots / vtable-type descriptors (roots alternate — Corrections 12; dynamic regime now dominant) |
| `0x143280560`–`0x143280868` (far) | settings-family descriptor initializers (`&PTR_FUN_143280560/5f0/698/720/798/838/868`), new band seen pass 26 |
| `0x14386a1e0`–`0x14386c788` (pass-1 tail) | 39 shared static-descriptor block pointers (`PTR_DAT_14386a…`, 3–307 users each) |

**What it is for (reading conclusion).** Everything in `0x14003ffe0`–`0x1404bfd20` is startup-time type/object/settings registration, not gameplay: encrypted names are registered with size/alignment/category/method tables; builders instantiate them, wrappers clone rows, 2-entry sorted tables and `{id,hash,alias}` rows expose types to an id-based consumer ahead in `.text`; the registry writes the CompilerIDFilter chain; and from `0x1404b94e0` a settings/variable family registers named, typed, default-valued parameters with per-object destructors. No consumer of the type rows, no name plaintext, no gameplay logic read yet. Confidence: counts/shapes/bands/correlations measured; "type registry / shutdown slot / lookup table / settings variable" labels are shape-based inference.

**Known limits.** (a) Registrar + decryptors `func_0x…` — no body in the dump. (b) No name buffer
decrypted (cheapest now the settings page: payload `0x1439a8ba4`, key `0x1439a8ba0`, len
`_DAT_1439a8ba0`, row `FUN_1404bf450`; older `0x14397fcb4`, key `0x14397fca8`, row `FUN_140494630`;
older printable `0x143970f0c`). (c) `0x142f0…`/`0x142f1…` atexit/onexit labels not in the dump
(highest `0x142f172b0`). (d) Twelve+ uninspected gaps (largest `0x1401a4e02`–`0x1401abad0`
27,854 B; pass 26 adds `0x1404b9547`–`0x1404babc0` ~5.5 KB headerless between the settings stubs
and the int-function run); 0x100–0x220 B steps look like padding. (e) `0x39091531` registered
(`FUN_14036bb60`, Corrections 11).

## Cross-cutting conventions (one line each; per-pass deltas in the records)

| convention | rule | first seen |
|---|---|---|
| TLS init guard | `*(TLS+0x50) < epoch` → `FUN_1426c3bcc(&epoch)` → `_Init_thread_footer` | `0x140001000` |
| 181-B descriptor | `{+0x20=1\|2, +0x40=ctor, +0x48=vtable/FUN, +0x50=third, +0x58=payload, +0x60=shared}` ×2,451 | `0x14003ffe0` |
| Static-descriptor block marker | shared `PTR_DAT_14386a…` + tag `1\|2` + ctor/label/payload bands; 57 tag-1 descriptors `0x1400bded0`–`0x1400c1a20` | `0x140093150` |
| XOR-40 plain helper | 134-B act calls `FUN_141c47cc0(&out,&ct,0x28,&DAT_143a155f0,0)`, no TLS guard | `0x1400c29c0` |
| XOR-40 / XOR-8 decryptors | 8-byte key, 24-bit length; `d4f30/d4f70(&out,&buf,hash,0)`; `d4f70`↔397-B near-exact | `0x1400fbf70` |
| `{id,hash,alias}` record | two TLS guards + `c2d50(&dst,&src)`; 326 rows; third = alias hash; ids `0x1`–`0x18b` | `0x1400fbeb0` |
| Builder | guards + `c2d70`/decrypt + `d4fb0` + row `{+0x20 root, +0x28 ptr, +0x30 0, +0x98 1, +0x9c 0}`; 369/365-B rootless store no root | `0x1400fbf70` |
| Wrapper | same row writes as a builder but `+0x98 = 0`; 231/459-B also store root 0 | `0x14015f9a0` |
| Sorted registry | min-to-slot-0 pre-swap + insertion sort of 2×56-B records keyed at `+8`; 280 instances; middle call is the ordinary pre-step; pass 26 d4f30-heavy, mostly rootless/output-rooted | `0x1400ff280` |
| Stack canary | `_DAT_143ac5f40 ^ stack` → `FUN_1426c3d40`; builders/sorted/atexit only | `0x1400fbf70` |
| Nested-atexit | guards + per-object global slot + `atexit(&LAB_142f0…)` + `c7880(&slot)` (1–2 arg); 261 instances, atexit labels to `0x142f16960`; slots can sit in the ciphertext page; `0x143c3ba40` (p24–25) and `0x14412cd58` (p26) shared | `0x1401003f0` |
| Two-buffer builder | helper `(size,&buf,0,hash)` decrypt before the inline decrypt; ≥60 helpers; **helper hashes can equal reg/record hashes** (`0x6760479e`, `0xa7f15a16`); new helpers `FUN_1410eaf40/141108960/140f7ade0` | `0x14010c120` |
| Registration schema | 18 args; zero hash reuse; a10–a14 + a17 rotate per block; **arg18 = out − 0xa0**; pass 26: flags 0 ×278 / 1 ×3 / 2 ×3 / 3 ×1 / 0x80000000 ×1, align 8 ×275 / 0x10 ×7 / 4 ×3 / 1 ×1, **266/256/260-B rows carry a runtime-global a16** | `0x1400fbcb0` |
| No-output registration | 242/246/252/257-B; arg17 = arg18 = 0; ×40 in pass 26 incl. size-3/align-1 (Corrections 15); **consumed: sorted `FUN_1404a82b0` copies `&DAT_144121c50`** | `0x140341b30` |
| Token → category | nonzero arg9; one token per type default; pass 26: 73 uses / 69 distinct, `0x53b89a1dc661b5dd` ×3 consecutive, one no-output 252-B token row | `0x140126f90` |
| Size-tagged allocator | one-arg pre-step, argument = registered size; symbol is per-TU (16 symbols, Corrections 13) — key on the shape; `FUN_141901810(0)` allocates 0 | `0x140123f10` |
| Root regime | pass 26: **dynamic (registration outputs) dominates** — `&DAT_144127550` ×17, `&DAT_1441156d0` ×12, `&DAT_144127a50` ×9, `&DAT_144122f60` ×4, `&DAT_144121ff0/144120940/14412eca0`; static `0x143cf/d…` minority | `0x1402133b0` |
| Decrypt-hash reuse | builder sea reuses name hashes; one hash can be reg + record + helper hash (`0x6760479e`, `0xa7f15a16`, `0x15be7741`, `0xb48f1d22`); pass 26 d4f30 ×97/84, d4f70 ×17/15 | `0x1401e26f0` |
| No-arg pre-step family | `FUN_1421c51f0…FUN_1421c7780` (≥40 names) precede most builders/sorted-inserts; pass 26 adds `FUN_1410eadc0/141367b90/141367c50/14140e210/1421c5370/5eb0/63b0/69e0/6b60/6e60/76c0` | `0x1402cff50` |
| Per-block furniture | one `(a10..a14, a17)` sextet per block, always a fresh output page; blocks 1–57 regs (pass 26), records interleave every 4–28 regs; far families `(&LAB_1413bb260…)` and `FUN_14191f4b0…FUN_14193bf50` | `0x1402ea070` |
| Settings/variable registrar | 209–399-B `int` fns: 1–3 XOR-8 decrypts (new page `0x1439a8ba0+`) → `FUN_141c58170(&desc,0,&DAT_144140740\|758,&name,&default)` ×83 → ~0x50-B descriptor (6 initializers, float/int defaults) → `_onexit(&LAB_142f16xxx)` monotonic to `0x142f172b0`; no canary/guard | `0x1404b94e0` |

## Open threads (cheapest next query each; check/update every pass)

1. **Registrar body** `func_0x1421cd360` — not in the dump; schema derived from 7,952 call sites.
2. **Decrypt a name buffer** — cheapest now the settings page: payload `0x1439a8ba4`, key `0x1439a8ba0`, len `_DAT_1439a8ba0` (row `FUN_1404bf450`); fallback `0x14397fcb4` (pass 25).
3. **`FUN_141c58170` body** — FUN_-named, body exists in unread corpus (~chunk `15xx`); settle register-vs-store and what `&DAT_144140740`/`&DAT_144140758` hold.
4. **Settings-family consumer** — who reads descriptors `0x144130570`–`0x14413b7a0` and the six initializers `&PTR_FUN_142f7d350/142f83a40/142f8be60/142f83a70/143280838/143280868`? Walk forward from `0x1404bfd20` (zone continues into `0230`).
5. **`{id,hash}` consumer** — 326 rows, ids `0x1`–`0x18b`, rows to `0x144135f98`; walk forward from `0x1404bfd20` for the next `c2d50` or id switch.
6. **Flags 1/2/3/0x80000000 reader** — dump flags-0x80000000 output `0x144122660` (`FUN_1404a5fa0`) beside a flags-0 row; the flags-2 no-output row `FUN_14049e230` IS consumed (`FUN_14049f180` roots on it).
7. **266/256-B runtime-global a16** — dump `_DAT_14410ff88`, `_DAT_144111038`, `_DAT_144111198` (5 words each): what do they hold that constant `FUN_14131dXXX` pointers did not?
8. **Sorted-table consumers** — dump a finished table `0x144124a60` (`FUN_1404b0720`); grep forward chunks for `c2d70` sources at sorted outputs.
9. **Atexit/onexit label region** — dump `0x142f172b0` (highest onexit label) and shared c7880 slot `0x14412cd58` (written by `FUN_1404af790` + `FUN_1404b0ee0`).
10. **`0x143280xxx` initializer band** — dump `0x143280560`–`0x143280870` (stub + settings users).
11. **Uninspected gaps** — `0x1404b9547`–`0x1404babc0` (~5.5 KB headerless inside the settings zone): padding or data? Plus older gaps (largest `0x1401a4e02`–`0x1401abad0`).
12. **CompilerIDFilter** — payloads are regs `FUN_1403023f0/2900/2a00/24f0`; nobody *reads* the shells (last pass 21); dump `0x143e09560`–`0x143e095f8`.

CLOSED (machine): fd9670 recount; provenance complete; `0x1411b8070` unread corpus; thread 43
(`0x3fd91271` = `FUN_140290c50`); `--update`/`--init` ledger 5; shutdown "move" ledger 6; third
field = alias ledger 10; CompilerIDFilter payloads = regs; `0x39091531` ledger 11; **no-output
consumption (partial, pass 26)**.

## Next pass

Resume at **`chunk_0230.txt`** (pass 26 ends mid-family at `FUN_1404bfd20`, a 209-B settings `_onexit` stub — the `other x91` zone is OPEN and continues). `state.json.next_chunk = 230` and this resume point agree. The pass **length comes from the task message** (protocol default 8): this file names only the resume chunk, never an end chunk or a guessed length. Run `python scripts/pass_measure.py <start> <end>`, quote stdout verbatim in `ranges/<first>-<last>.md`, run `--update`, then refresh this file. Watch for:
(a) the settings/variable family continuing: how many more int functions, the label run past `0x142f172b0`, new initializers past `&PTR_FUN_143280868`, and any reader of the descriptors `0x144130570`–`0x14413b7a0` (thread 4);
(b) where the family ends and what follows — first registry/settings consumer, or another reg block;
(c) `{id,hash}` rows past id `0x18b` and new alias third fields;
(d) ciphertext past `0x1439a9b2c`, outputs past `0x144132d50`, descriptors past `0x14413b7a0`;
(e) sorted builders (31 in pass 26) and whether any sorts more than 2 records;
(f) flags/align outliers (0x80000000, align 1) and the `FUN_141c58170` 5-arg shape outside the zone;
(g) the headerless gap `0x1404b9547`–`0x1404babc0` once the family's extent is clear.
Do not re-run an already-counted range through `--update` (ledger 5); the ciphertext band has no script line (ledger 7); do not hand-edit the two stale `matched:false` flags (ledger 11).

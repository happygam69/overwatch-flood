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
| `state.json` | machine ledger: next_chunk, per-pass entries, cumulative totals, all 7,666 registration hashes, all 266 `{id,hash}` rows with match flags |
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
| **total** | **222, contiguous** | `0x140001000`–`0x140495d90` | **15,308** | **3,978,286** | machine-verified (`state.json`) |
| pending | `0222`–`2227` | `0x140495e90`→ | — | — | resume at `chunk_0222` |

Machine-verified cumulative (`state.json` after pass 25): files 15,308 (12.78 % of functions),
Σ `size=` 3,978,286 (9.28 % of `.text`); classes reg 7,666 / wrapper 1,918 / builder 1,672 /
sorted 249 / atexit 254 / record 266 / other 3,283; registrations 7,666, all hashes distinct;
`d4f30` 1,091, `d4f70` 1,333, `d4fb0` 4,342, `c2d70` 4,093, `c2d50` 266, `c7880` 254,
`atexit` 259; records 266, **264/266 matched** (two stale flags = Corrections 11); other unchanged
since pass 11. Pass 25 ran the 8-chunk protocol default after ten override passes.

## Corrections ledger (machine-derived; supersedes prose in older records)

1. **`{id,hash}` records match 75/75, not 74/75.** Pass 15's "unmatched" hash `0x3fd91271` (id `0x35`)
   is the registration hash of `FUN_140290c50` (chunk `0114`). Thread 43 CLOSED. Pass 16 adds 23 rows; pass 17 adds 45.
2. **Sorted-insert builders: 249 cumulative** after pass 25 (115→130→150 through pass 17; none in pass 25); use `state.json`.
3. **Nested-atexit builders: 254 cumulative**; shapes 558/574/542/526; initializer families grow per pass.
4. **Provenance caveat:** passes 1–15 records state counts without a quoting script (their ad-hoc
   scripts were not kept). All 24 passes' `files`/Σ `size=` are reproduced by `scripts/pass_measure.py`.
5. **`--update` is forward-only; `--init` wipes the pass list.** `--update` over an already-counted range
   double-counts and rewinds `next_chunk`; repair is `--init` (recomputes totals, empties `passes`) — that
   is why `state.json` lists only passes 16–24.
6. **There is no shutdown table and no "move".** Shutdown rows are per-object global slots scattered
   by the linker (`0x1438e…`, `0x143ce7…`, `0x143e5e/5f/6a/6e/77/7c…`, plus pass 17's
   `0x143e94720`, `0x143e92cc0`, `0x143ec5860/6248/3ab20`). The code addresses each absolutely.
7. **`pass_measure.py` prints no `ciphertext band:` line** — its `CTXT` regex needs `DAT_1438` + 6
   hex digits; the band is now `0x1438f…`/`0x14390…`. Ciphertext extremes in records are read from
   the text, with both addresses cited.
8. **`pass_measure.py` `zones:` filter** prints only class `reg`/`record` runs and runs with
   `cnt>=3`; 1–2-function builder/wrapper runs are absent from the skeleton (they exist in the text).
9. **`record-hash = registration-hash` is a rule; the two historical exceptions are resolved (11).**
   Ids `0x3e`/`0xcb` bind `0x39091531`, absent through pass 18 but registered in pass 19. Do not
   repeat "98/98" as a law, and do not treat the two stale `state.json` flags as exceptions.
10. **The 178-B third field is an alias registration hash, not a flag.** Pass 17 measured three
    independent pairs (`0xaa`→`0x5a5653e7` = `FUN_14031c180`, `0x11`→`0x67b43929` = `FUN_14031b240`,
    `0x8c`→`0x7f0ab0b0` = `FUN_14031e620`), each aliasing a second registration in the same block;
    pass 16's `id 0x182` self-repeat is the degenerate case. Row layout = `{id, hash, alias}`.
11. **Corrections 9 is now closed by direct evidence.** `FUN_14036bb60` (chunk `0156`) registers
    `0x39091531` (`&DAT_143f803a0`, size `0x30`), the hash of record ids `0x3e`/`0xcb`. The two
    `state.json` rows stay `matched:false` (the matcher never revisits old rows); treat them as stale.
12. **Roots alternate; "static-root era over" is retired.** Pass 23 roots 16 rows on `&DAT_143d013b0`
    and others on `&DAT_143d03a40/bb0/4cf0`, `&DAT_143d99c80`, `&DAT_143cfa130` while 48 root on
    `&DAT_143fca7f0`. Root regime is per-block, not a timeline.
13. **Allocator symbol ≠ allocator.** The one-arg pre-step is per-TU (`140f80f80`, `140f94650`,
    `140f94580`, `1411393a0`, `141814130`, `1417e3f10`, `141805b40`); key structure on the shape.
14. **The sorted-insert middle call is the ordinary pre-step slot** (`FUN_141114540…780` early in
    pass 23, `FUN_1421c7780`/`6920`/`7600` later). Not a second decrypt stage.

## What the code is — cumulative synthesis (25 passes; evidence unless marked [inference])

`.text` is catalogued in entry-address order. After 222 chunks the cursor is at `0x140495d90`
(12.78 % of functions, 9.28 % of `.text`). Names printed `func_0x…` have **no decompiled body
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
4. **Typed registry machine** `0x1400fbcb0`–`0x140495d90` (passes 2-tail–25) — the substance of the
   read, described next. No gameplay, network, asset or UI code; the only named subsystem is
   CompilerIDFilter.

**The registry machine — eight cooperating constructs/variants:**

- **Name buffers.** Every registration/builder carries an XOR-8 ciphertext: 8-byte key at `+0`,
  24-bit length at `+8`, done-flag `+0xb`, payload `+0xc`; `buf[i] ^= key[i & 7]`. Band
  `0x1438b8e50`–`0x14397fcb4` (pass 25 max; `0x143970f0c` printable pre-XOR). Plaintext never decoded.
- **Registration** — `func_0x1421cd360(out, ciphertext, hash32, 0, size, align, flags, 0, token,
  a10…a14, 0, 0, a16, a17, base)`: **7,666 instances, 7,666 distinct hash32 — zero reuse**
  (machine-checked). `size` 4–0x3bc0 overall, **8 minimum seen** (10 rows, pass 25); `align` 8
  default, 1/4/0x10 outliers; `flags` 0 default, 1/2/3/4/5/6/7/8/10/0xb/0x51 known (pass 25:
  0 ×266, 4 ×8, 2 ×2 — all ten on 257/267-B rows); 263/267-B rows carry 64-bit tokens (pass 25:
  **44 uses / 37 distinct**, 263-B ×38 + 267-B ×6); `arg8 = 8` limited to pass 19's 256/260-B rows.
  Passes 24–25 measured `base = out − 0xa0` in 174/174 + 276/276 rows (`0x1440c1cd0` vs
  `0x1440c1d70`, `0x1440f6fc0` vs `0x1440f6f20`) [inference: header slot, no reader seen].
  `a16` per-shape. [inference: a generated type registry — name, size, alignment, category,
  method/data pointers.]
- **No-output registration** — 242/246/252/257-B (246-B first `0x1403b32e0`, first overall
  `0x140341b30`, pass 18), pervasive since pass 19 (pass 23: 242-B ×16; **pass 25: 242-B ×8**, all
  in `0x1404908d0`–`0x140495380`): args 10–18 =
  `FUN_140548d00, 0x140f7b210, FUN_140548f80, FUN_14053a070, FUN_140548d00, 0, 0, 0, 0` —
  **arg17 = arg18 = 0**, no label and no output slot; still counted as `reg`.
  [inference: names/metadata registered without an instantiable object row.]
- **Builder** — 373/377/381/389/397/451/459/471/475/480/524/574-B: allocator/pre-step → inline XOR-8
  decrypt → `d4f30/d4f70(&out,&buf,hash,0)` → `d4fb0` → store class root, instance ptr, flag.
  Row = `{+0x20 root, +0x28 instance, +0x30 0, +0x98 flag(1), +0x9c 0}`; the registered row IS the
  object header and the registered `size` is only the payload (re-measured pass 17 by arithmetic:
  `FUN_1402fba60` row `0x143ea6c00`). 459-B and 451-B store **no root** (`+0x20 = 0`).
  **Pass 23 adds a 472-B two-buffer form** (×6): `FUN_140f81de0(size,&ct,0,0x9cadf2ec)` then the
  inline decrypt, two distinct helper hashes (`0x274b8350`, `0x4d2db658`); pass 24 adds
  `0x64adb587` and reuses `0x11b47c68` also seen as a plain `d4f30` hash.
- **Copy wrapper** — 241-B / 231-B rootless / 244-B: no decrypt; `c2d70(&dst,&src)` + `d4fb0`;
  `src = row slot − 0x20`. Same five fields but flag **0** at `+0x98`; 231-B also stores root 0.
  244-B stores `&PTR_s_CompilerIDFilter_*` + flag 1 into registration rows (×7) — the registry's
  named link into the CompilerIDFilter chain.
- **Sorted-insert builder** — 249 instances (507/508/511/512/515/523/524/527/531-B); every one sorts
  exactly 2 56-B records keyed by the `uint` at `+8` (min-to-slot-0 pre-swap, then insertion sort);
  two decrypts (2 distinct hashes per instance; shared opens `0xb48f1d22` ×2, `0x9b7a63ea` ×5 —
  pass 23 — and closes `0xf3733689`/`0x79252765`, `0x2ac48ffa`, `0x5aea0a51` ×3) + `d4fb0` + count = 2.
  The call between the two decrypts is the ordinary pre-step slot, not a second stage (pass 23).
  Pass 24 adds a rootless form (`FUN_14045bcb0`, root 0); **none in pass 25** (cumulative 249).
  [inference: tiny 2-entry lookup tables.]
- **`{id,hash}` record** — 169/178-B; **266 instances**; 264/266 flags matched, the last two resolved
  by Corrections 11. Ids span `0x2`–`0x189`+; pass 21 adds alias `0x7236f6e3` (id `0x1b`); pass 23
  adds id `0x166` → `0x5fda5eee`, registered 9 rows earlier at `0x1404504c0` (in-pass binding).
  Many-to-one is normal: `0x58b3d0d0` has **17 ids**; `0x38733fcc`/`0xa3645d25` two each;
  pass 20 adds `0xd3a5ca91` ×3. The 178-B third field is the **alias registration hash**
  (Corrections 10): pass 20 adds ids `0x124`→`0xc811573a`, `0xd4`→`0x43c60168`. Source rows
  `0x143e4ac90`–`0x143ed6f90`, `0x143f198d8`–`0x143fe0b00`, `0x1440c1390`. None added pass 25.
- **Nested-atexit builder** — 254 instances (526/542/558/574-B): writes a row into a **per-object
  global slot** (scattered, Corrections 6; pass 23 adds `0x14407d8f0/918/920`, `0x144091a48/70/78`,
  `0x1440a5838`, `0x14396c6e8/c710`, `0x1439735a0/5c8`), initializer pointers from the 26 families
  through pass 22 plus pass 23's `&PTR_FUN_14314bae8`/`14314b5b0`/`143149258` re-use; some slots hold
  two or three pointers (`&PTR_LAB_14314bb98`). Calls `atexit(&LAB_142f0…))` (labels now
  `0x142f08c40`–`0x142f15800`) and `c7880(&slot)`; field order varies and two rows write the slot into
  the ciphertext page. Pass 24 used slot `0x143c3ba40`/`&PTR_FUN_143149258`; pass 25 adds three rows —
  `FUN_1404744d0` **reuses that same slot** (label `0x142f157d0` = pass 24's +0x10) and
  `FUN_1404819a0`/`FUN_140481bd0` write ciphertext-page slots `0x14397a4d0`–`0x14397a528`
  (`&PTR_FUN_14314b5b0`) with c7880 slots `0x1440e4180/98`. [inference: static-object destructor/shutdown.]

Also present: **15 CompilerIDFilter shells** storing one of 15 `&PTR_s_CompilerIDFilter_*` labels plus
payloads `&DAT_143eb63c0/67e0/6aa0/6940` — **pass 17 proved those payloads are registration outputs**
(`FUN_1403023f0/2900/2a00/24f0`), so the chain roots are freshly registered types; the 244-B wrappers
tie the registry to this chain. Guard furniture: MSVC magic-static TLS guards + stack cookies;
**every builder/sorted-insert/atexit carries a canary, no registration or wrapper does**.
[inference: the sea registers part of the shader/compiler-filter machinery.]

**Passes 17–19 structural change (evidence).** One `(a10..a14, a17)` sextet and a fresh output page per
block (pass 17 `0x1413c14xx`→`0x14145dxx`, pass 18 `0x14146bdxx`→`0x14151b8xx`, pass 19
`0x141520190`→`0x14165b070`); 263/267-B rows carry a block-local sextet + 64-bit token, 256/260-B
have `arg8=8`, 270-B revives `a16=FUN_14131d9c0`. [inference: per-translation-unit method tables.]

**Passes 23–25 structural deltas (evidence).** Pass 23: 77–123-reg blocks, sextets
`FUN_1417e20b0`→`FUN_141862c20`, roots alternating static/dynamic, per-TU allocator symbols +
no-arg `FUN_1421c51f0…7780`. Pass 24: 174 regs all flags 0 / align 8, seven 263-B tokens,
sextets `FUN_141867190`→`FUN_141879930`, `base = out − 0xa0` 174/174 [inference: header slot].
**Pass 25 (276 regs, 453 files):** flags **4 ×8 / 2 ×2 return** — ten flags rows = 257-B
(`FUN_140481890`, `0x140492820/2930/2a40`, no token) + six **267-B rows = token + flags 4/2,
sizes `0x100`–`0x2c0`** (`FUN_1404922d0`…`FUN_140492d50`); **builders/wrappers root on
registration outputs** (`&DAT_1440e2830`/`0x1440e26d0` behind `0x140482010`–`0x140482990`,
`&DAT_1440f6fc0`/`0x1440f6620` behind `0x140495480`–`0x140495d90`) [inference: child-of links];
242-B no-output rows return ×8 (`0x1404908d0`–`0x140495380`); **zero sorted-insert builders and
zero `{id,hash}` records** (first zero-sorted ledgered pass); 373-B builders gain no-arg
pre-steps `FUN_1418c3e60`/`FUN_1418c3f20`; new one-arg allocator `FUN_14114d8a0`; token
`0x32c4241b02aad1d5` ×7 in one block; new shared 253-B family `(&LAB_1418aeec0, FUN_1418b28d0,
&LAB_1418b6140, &LAB_1418ad320)`; atexit labels to `0x142f15800`, slot `0x143c3ba40` reused
from pass 24. [inference: tokens per-category; flags per-variant.]

**Where the data lives:**

| band | content |
|---|---|
| `0x1438b8e50`–`0x14397fcb4` | XOR-8 name/payload ciphertext (+ 15 `PTR_s_CompilerIDFilter_*` labels; `0x143970f0c` is printable pre-XOR — thread 1; pass-25 atexit slots `0x14397a4d0`–`0x14397a528` live inside this band); pass 25 reached `0x14397fcb4` |
| `0x143e99d90`–`0x1440f8a10` + earlier `0x143d/0x143e…` | registration outputs / instance slots; fresh page per block-pair (pass 25 reached `0x1440f8a10`, scratch rows to `0x1440fd7c0`) |
| `0x143e4ac90`–`0x143ed6f90` + `0x143f198d8`–`0x143fe0b00` | `{id,hash,alias}` source rows, interleaved with output bands |
| `0x1438e…`, `0x143ce7…`, `0x143e5e/…`, `0x143e92/94…`, `0x143ec5/6…`, `0x143f1…`–`0x143f3…`, `0x143c3ab20`, `0x143c4c730`, `0x143e2bc10`, `0x143fc13f0`, `0x143fc1a90`, `0x143c3d0f8`, `0x143950a88/ae8/ba8`, `0x143953668/6c8`, `0x143fea2d0`, `0x143ff9810`, `0x1440459b0/9d8`, `0x14404d0b0`, `0x14405a3e0/408/410`, `0x14405c2c0/298`, `0x14405c5e8/5c0`, `0x14405c768/740`, `0x144068c00/c28/c30` | nested-atexit/shutdown slots (**per-object, scattered** — Corrections 6) |
| `0x143d01930`, `0x143d01a90`, `0x143d03780`, `0x143d04970`, `0x143d93520`, `0x143cfa130`, `0x1441e1bb0`, `0x143defd00`, `0x143f8e3d0`, `0x143ce2090`, `0x143f94670`, `0x143cfc6a0`, `0x143eb67e0`, `0x143e135e0`, `0x143e138a0`, `0x143fcaed0`, `0x143fca7f0`, `0x1440073e0`, `0x144005360`, `0x1440547f0`, `0x144058990`, `0x14405e0c0` | far class roots / atexit payloads (**0x143f94670 is the closed shared root of 73+62 wrappers**; 0x1441e22d0 reused ×25 in pass 19; pass 23 roots `0x143fca7f0` ×48, `0x143fcaed0` ×25, `&DAT_143d013b0` ×16, `&DAT_1441e1bb0` ×9) |
| `0x143cf0000`–`0x143d05000` + far `0x143f8xxxx`–`0x143f94xxx`, `0x143eb6xxx`, `0x143ecee70`, `0x143ee0cd0` | class roots / vtable-type descriptors (roots alternate — Corrections 12) |
| `0x14386a1e0`–`0x14386c788` (pass-1 tail) | 39 shared static-descriptor block pointers (`PTR_DAT_14386a…`, 3–307 users each) |

**What it is for (reading conclusion).** Everything in `0x14003ffe0`–`0x140495d90` is startup-time
type/object registration, not gameplay: encrypted names are registered with size/alignment/category/method
tables; builders instantiate them, wrappers clone rows, 2-entry sorted tables and `{id,hash,alias}` rows
expose types to an id-based consumer ahead in `.text`; the registry writes the CompilerIDFilter chain.
No consumer, no name plaintext, no gameplay logic read yet. Confidence: counts/shapes/bands/correlations
measured; "type registry / shutdown slot / lookup table" labels are shape-based inference.

**Known limits.** (a) Registrar + decryptors `func_0x…` — no body in the dump. (b) No name buffer decrypted
(cheapest now `0x14397fcb4`, key `0x14397fca8`, len `_DAT_14397fcb0`, row `FUN_140494630`; older
`0x143970f0c` printable pre-XOR). (c) `0x142f0…` atexit labels not in the dump (highest `0x142f15800`).
(d) Twelve+ uninspected gaps (largest `0x1401a4e02`–`0x1401abad0` 27,854 B, `0x140229be7`–`0x14022dcc0`
16,601 B; pass 25: `0x140482990`–`0x140483570` 3,040 B); 0x100–0x220 B steps look like padding.
(e) `0x39091531` registered (`FUN_14036bb60`, Corrections 11).

## Cross-cutting conventions (one line each; per-pass deltas in the records)

| convention | rule | first seen |
|---|---|---|
| TLS init guard | `*(TLS+0x50) < epoch` → `FUN_1426c3bcc(&epoch)` → `_Init_thread_footer` | `0x140001000` |
| 181-B descriptor | `{+0x20=1\|2, +0x40=ctor, +0x48=vtable/FUN, +0x50=third, +0x58=payload, +0x60=shared}` ×2,451 | `0x14003ffe0` |
| Static-descriptor block marker | shared `PTR_DAT_14386a…` + tag `1\|2` + ctor/label/payload bands; 57 tag-1 descriptors `0x1400bded0`–`0x1400c1a20` | `0x140093150` |
| XOR-40 plain helper | 134-B act calls `FUN_141c47cc0(&out,&ct,0x28,&DAT_143a155f0,0)`, no TLS guard | `0x1400c29c0` |
| XOR-40 / XOR-8 decryptors | 8-byte key, 24-bit length; `d4f30/d4f70(&out,&buf,hash,0)`; `d4f70`↔397-B near-exact | `0x1400fbf70` |
| `{id,hash,alias}` record | two TLS guards + `c2d50(&dst,&src)`; 266 rows, 264/266 matched (Corrections 11); third = alias hash | `0x1400fbeb0` |
| Builder | guards + `c2d70`/decrypt + `d4fb0` + row `{+0x20 root, +0x28 ptr, +0x30 0, +0x98 1, +0x9c 0}` | `0x1400fbf70` |
| Wrapper | same row writes as a builder but `+0x98 = 0`; 231/459-B also store root 0 | `0x14015f9a0` |
| Sorted registry | min-to-slot-0 pre-swap + insertion sort of 2×56-B records keyed at `+8`; 249 instances (one rootless); the middle call is the ordinary pre-step | `0x1400ff280` |
| Stack canary | `_DAT_143ac5f40 ^ stack` → `FUN_1426c3d40`; builders/sorted/atexit only | `0x1400fbf70` |
| Nested-atexit | guards + per-object global slot + `atexit(&LAB_142f0…)` + `c7880(&slot)`; 254 instances, labels to `0x142f15800`, some two/three-pointer slots, two slot/​ciphertext pages shared, slot `0x143c3ba40` reused across passes 24–25 | `0x1401003f0` |
| Two-buffer builder | helper `(size,&buf,0,hash)` decrypt before the inline decrypt; ≥60 helpers, own hash each; 472-B form first at `0x140441030` | `0x14010c120` |
| Registration schema | 18 args; zero hash reuse; a10–a14 + a17 rotate per block; **arg18 = out − 0xa0** (passes 24–25: 174/174 + 276/276); pass 25 flags 0 ×266 / 4 ×8 / 2 ×2, align 8 ×276, tokens 44 uses; `&DAT_14100e120`/`&DAT_141006710` recur as args 13–14 | `0x1400fbcb0` |
| No-output registration | 242/246/252/257-B; arg17 = arg18 = 0, no label/output slot; pervasive passes 19–23, absent pass 24, back ×8 in pass 25 (242-B only, `0x1404908d0`–`0x140495380`) | `0x140341b30` |
| Token → category | nonzero arg9; one token per type default; pass 25: 44/276 rows, 37 distinct, `0x32c4241b02aad1d5` ×7 shared by one block, 267-B rows always token+flags | `0x140126f90` |
| Size-tagged allocator | one-arg pre-step, argument = registered size; symbol is per-TU (`140f80f80`/`140f94650`/`1411393a0`/`141814130`/`1417e3f10`/`141805b40`/`14184a810`/`14114d8a0`) — key on the shape, not the symbol | `0x140123f10` |
| Root regime | alternates between dynamic bands and the static `0x143cf…`–`0x143d9…` band (pass 25: `&DAT_143fcaed0` ×46, `&DAT_143d013b0` ×43, `&DAT_143cfa130` ×38, new `0x143fc9060`/`0x143d02c80`/`0x143d02de0`/`0x143f8e270`); **new: roots can be registration outputs** (`0x1440f6fc0` ×6, `0x1440e2830` ×5) | `0x1402133b0` |
| Decrypt-hash reuse | builder sea reuses name hashes, one hash can be reg + record + helper hash (`0x73bb2f3a`, `0x7c3457dc`, `0x3a9b5e90`); pass 25: 5 `d4f30` / 82 `d4f70`, `0x66d09c06` ×12, `0xb16a0b` ×9, `0x37ab13d3` ×8 | `0x1401e26f0` |
| No-arg pre-step family | `FUN_1421c51f0…FUN_1421c7780` (≥28 names) precede most builders/sorted-inserts; pass 25 adds `FUN_1418c3e60`/`FUN_1418c3f20` (373-B) and reuses `FUN_1421c7780` | `0x1402cff50` |
| Per-block furniture | one `(a10..a14, a17)` sextet per block (pass 25: 2–74 regs, families to `FUN_1418b28d0`/`FUN_1418b1a70`), always a fresh output page; blocks can be 1–123 regs, each followed by its record(s) | `0x1402ea070` |

## Open threads (cheapest next query each; check/update every pass)

1. **Registrar body** `func_0x1421cd360` — not in the dump; schema derived from 7,666 call sites.
2. **Decrypt one name buffer** — cheapest `0x14397fcb4`, key `0x14397fca8`, len `_DAT_14397fcb0` (row `FUN_140494630`); older printable pre-XOR `0x143970f0c`, key `0x143970f00`, row `0x140438c90`.
3. **`{id,hash}` consumer** — 266 rows, ids `0x2`–`0x189`+, rows to `0x1440c1390`; none added pass 25; walk forward from `0x140495d90` into `0222` for the next `c2d50` or id switch.
4. **`0x39091531`** — CLOSED: registration `FUN_14036bb60`; only the two ledger flags are stale.
5. **No-output registration** (242/246/252/257-B, arg17=arg18=0) — back ×8 in pass 25; still no reader.
6. **`0x58b3d0d0` 17-id class** — registration `FUN_140170530` (chunk `0044`, output `&DAT_143ce5100`); did a chunk-`0044` builder fill its `+0x20/+0x28`?
7. **CompilerIDFilter** — payloads are regs `FUN_1403023f0/2900/2a00/24f0`; nobody *reads* the shells (last pass 21); dump `0x143e09560`–`0x143e095f8`.
8. **Atexit handlers** `LAB_142f08c40`–`LAB_142f15800` — outside `.text`; dump `0x142f15800`, slot region `0x143c3ba40`–`0x143c3ba80` (reused passes 24+25), c7880 slots `0x1440e4180/98`.
9. **Sextet globals/labels** — pass 25 families `(&LAB_1418aeec0, FUN_1418b28d0, &LAB_1418b6140, &LAB_1418ad320)` (plain) and `(&DAT_1418ae5f0, FUN_1418b1a70, &DAT_1418b5dc0, &DAT_1418ad020)` (267-B); plus pass 24's `&LAB_140aa6750`/`&SUB_14064feb0`; dump these.
10. **Allocator/pre-step bodies** — decompile `FUN_140f80f80`, `FUN_14114d8a0` (one-arg, new), `FUN_1418c3e60`/`FUN_1418c3f20` (no-arg, new) to confirm alloc-vs-construct.
11. **Static root band** — dump `0x143d013b0`, `0x143d030a0`, `0x143fc9060`, `0x143d02c80`, `0x143d02de0`, `0x143f8e270` (5 words each): vtable, output, or counter?
12. **Initializer families / token rows** — dump `&PTR_FUN_143149258`/`14314b5b0`/`14314bae8`, slots `0x144091a48`/`0x14407d8f0`; decompile token row `FUN_1404642b0`.
13. **Registration base −0xa0** — dump `0x1440f6f20` beside output `0x1440f6fc0` (`FUN_1404908d0`), plus pass 24's pair `0x1440c1cd0`/`0x1440c1d70`; identifies the 160-byte header.
14. **Unlisted gaps / outliers** — 0x100–0x220 B steps look like padding; pass 25's largest gaps `0x140482990`–`0x140483570` (3,040 B) and `0x14048ff00`–`0x1404908d0` (2,512 B).
15. **Flags 4/2 reader** — all ten flags rows are 257/267-B (pass 25); dump flags-2 output `0x1440f7c50` (`FUN_1404924f0`) beside a flags-0 row to find the flag slot and its consumer.
16. **Dynamic roots / shared token** — dump `0x1440f6fc0` + rooter `FUN_140495480` (child rows); explain the 7-row token class `0x32c4241b02aad1d5` (`0x140474ea0`–`0x140477310`).

CLOSED (machine): fd9670 recount; provenance complete; `0x1411b8070` unread corpus; **thread 43**
(`0x3fd91271` = `FUN_140290c50`); sorted/atexit counts see ledger; `--update`/`--init` ledger 5; shutdown "move" ledger 6; third field = alias ledger 10; CompilerIDFilter payloads = regs; `0x39091531` ledger 11.

## Next pass

Resume at **`chunk_0222.txt`** (first entry `0x140495e90`; pass 25 ends cleanly at `FUN_140495d90`).
`state.json.next_chunk = 222` and this resume point agree. The pass **length comes from the task
message** (protocol default 8): this file names only the resume chunk, never an end chunk or a guessed
length. Run `python scripts/pass_measure.py <start> <end>` over the assigned range, quote stdout verbatim
in `ranges/<first>-<last>.md`, run `--update`, then refresh this file. Watch for:
(a) flags-4/2 rows and the 267-B token+flags shape continuing past `0x140495d90`, and any reader of the flag slot (thread 15);
(b) more dynamic roots on registration outputs and what child rows add beyond `c2d70`'s copy (thread 16);
(c) 242-B no-output rows beyond pass 25's 8, and any reader of them;
(d) `{id,hash}` rows returning (records 0 in pass 25): ids past `0x166`, aliases past `0x7236f6e3`;
(e) atexit labels past `0x142f15800` and further slot reuse (`0x143c3ba40` shared by passes 24–25);
(f) ciphertext past `0x14397fcb4`, outputs past `0x1440f8a10`, scratch rows past `0x1440fd7c0`;
(g) sorted-insert builders returning (none in pass 25), and the new pre-steps
    `FUN_1418c3e60`/`FUN_1418c3f20`/`FUN_14114d8a0` shapes.
Do not re-run an already-counted range through `--update` (ledger 5); the ciphertext band has no script line (ledger 7);
do not hand-edit the two stale `matched:false` flags (ledger 11).

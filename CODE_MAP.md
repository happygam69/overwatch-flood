# CODE_MAP — cumulative map of the systematic `.text` read

**Read in full before every pass; update after every pass. Hard budget: ≤300 lines.**
Per-pass narrative lives ONLY in `ranges/<first>-<last>.md`; cumulative numbers come from
`state.json` (via `scripts/pass_measure.py`) — never hand-add. Long-form archive:
`CODE_MAP_ARCHIVE.md`.

## Files

| file | role |
|---|---|
| `chunks/chunk_NNNN.txt` | corpus, address order; the one-line `Removing unreachable block` warnings were stripped in place 2026-11-21 (668,998 lines / 42,145,998 B; per-chunk counts in `index.json`, pre-strip index `index.pre_strip.json`). Every code line is present. |
| `index.json` | per-chunk bytes / first / last — source of truth for coverage |
| `state.json` | machine ledger: next_chunk, per-pass entries, cumulative totals, all 7,952 registration hashes, all 326 `{id,hash}` rows with match flags |
| `scripts/pass_measure.py` | the canonical per-pass measurement; stdout quoted verbatim in records; matches any function header name (1,204 Ghidra-named functions in chunks ≥235 are not `FUN_`-named) |
| `census.py` / `cluster.py` | ad-hoc per-chunk census / family clustering (skeleton detector) |
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
| 27 | `0230`–`0238` | `0x1404bfe00`–`0x14054ea50` | 1,259 | 200,071 | `ranges/0x1404bfe00-0x14054ea50.md` |
| **total** | **239, contiguous** | `0x140001000`–`0x14054ea50` | **17,124** | **4,327,343** | machine-verified (`state.json`) |
| pending | `0239`–`2227` | `0x14054eb60`→ | — | — | resume at `chunk_0239` |

Machine-verified cumulative (`state.json` after pass 27): files 17,124 (14.30 % of functions),
Σ `size=` 4,327,343 (10.10 % of `.text`); classes reg 7,956 / wrapper 1,954 / builder 1,717 /
sorted 280 / atexit 261 / record 326 / other 4,630; registrations 7,956 ciphertext rows all
distinct (+4 plaintext rows, one hash ×2 — Corrections 16); `d4f30` 1,188 / `d4f70` 1,350 /
`d4fb0` 4,492 / `c2d70` 4,212 / `c2d50` 326 / `c7880` 261 / `atexit` 312; records 326 (all
pass-26 rows matched). Pass 27 is the structural pivot: registry out, plaintext in.

## Corrections ledger (machine-derived; supersedes prose in older records)

1. **`{id,hash}` records match 75/75, not 74/75.** Pass 15's "unmatched" hash `0x3fd91271` (id `0x35`) is the registration hash of `FUN_140290c50` (chunk `0114`). Thread 43 CLOSED. Pass 16 adds 23 rows; pass 17 adds 45.
2. **Sorted-insert builders: 280 cumulative** after pass 26 (249→+31, first since pass 23; machine-reconciled per chunk 0/4/3/9/1/8/4/2); use `state.json`.
3. **Nested-atexit builders: 261 cumulative**; shapes 542/558-B this pass; initializer families grow per pass.
4. **Provenance caveat:** passes 1–15 records state counts without a quoting script (their ad-hoc scripts were not kept). All 27 passes' `files`/Σ `size=` are reproduced by `scripts/pass_measure.py`.
5. **`--update` is forward-only; `--init` wipes the pass list.** `--update` over an already-counted range double-counts and rewinds `next_chunk`; repair is `--init` — why `state.json` lists only passes 16–26.
6. **There is no shutdown table and no "move".** Shutdown rows are per-object global slots scattered by
   the linker (`0x1438e…`, `0x143ce7…`, `0x143e5e/6…`, `0x143c3ab20/ba40`, `0x143e92/94…`, pass 26:
   `0x144101c90`, `0x144123ab0–af0`, `0x144126320–378`, `0x14412cd58/da0`, `0x14412e078–0b0`,
   `0x144136068–0a8`, ciphertext-page `0x14398bc98–d58`). The code addresses each absolutely.
7. **`pass_measure.py` prints no `ciphertext band:` line** — its `CTXT` regex needs `DAT_1438` + 6 hex
   digits; the band is now `0x1439a…`/`0x1439b…`. Ciphertext extremes in records are read from the
   text, both addresses cited (pass 27 low page `0x143848d40`; pass 26 payload `0x1439a9b2c`).
8. **`pass_measure.py` `zones:` filter** prints only class `reg`/`record` runs and runs with `cnt>=3`;
   1–2-function builder/wrapper runs are absent from the skeleton (they exist in the text).
9. **`record-hash = registration-hash` is a rule; the two historical exceptions are resolved by
   direct evidence.** `FUN_14036bb60` (chunk `0156`) registers `0x39091531` (`&DAT_143f803a0`,
   size `0x30`), the hash of record ids `0x3e`/`xcb`. The two `state.json` rows stay
   `matched:false` (the matcher never revisits old rows); treat them as stale.
10. **The 178-B third field is an alias registration hash, not a flag.** Pass 17 measured three pairs; pass 26 adds `0x129`→`0xab64f377` aliasing `0x93c5fe63` = `FUN_1404b3f50` (253-B, size 8). Row layout = `{id, hash, alias}`; most third fields are 0.
11. **Corrections 9 is closed by direct evidence** — see item 9 (`FUN_14036bb60` registers
    `0x39091531`); keep the two stale `state.json` flags untouched.
12. **Roots alternate; "static-root era over" is retired.** Pass 26 roots sit almost entirely on registration outputs (`&DAT_144127550` ×17, `&DAT_1441156d0` ×12, `&DAT_144127a50` ×9 …); static `0x143cf/d…` roots are now the minority (×3/×2/×2). Regime is per-block, not a timeline.
13. **Allocator symbol ≠ allocator.** Per-TU one-arg symbols (pass 26: `141367110`, `1412b5440`,
    `1418e82e0`, `1413676c0`, `141901b40/170/180`, `140f7b550`, `140f7ade0`, `14190df80`,
    `14191bd90`, `1419254a0`, `14192a730`; older `140f80f80`, `14114d8a0`); key on the shape.
14. **The sorted-insert middle call is the ordinary pre-step slot.** Not a second decrypt stage.
15. **Minimum registered size is 3, not 8** (pass 26: `FUN_1404aad50`, size 3, align 1); span 3–0x3bc0.
16. **Zero hash reuse is conditional, not absolute.** Pass 27's 4 plaintext registrar calls
    (`"teStructuredData"` `0x8df63eb2` ×2 with flags 0/2, `"MirrorData"`, `"TrackedData"`)
    trip the script's zero-reuse check legitimately: the property is "one hash per
    ciphertext-named row". Do not "repair" this in `state.json`.
17. **The static `0x143cf…/0x143d…` band is RTTI type_info, not "class roots".** Pass 27's
    272 catch descriptors all store one at +0x18; Corrections 12's root wording still holds
    for builder roots; the band's *content* label is superseded.

## What the code is — cumulative synthesis (27 passes; evidence unless marked [inference])

`.text` is catalogued in entry-address order. After 239 chunks the cursor is at `0x14054ea50`
(14.30 % of functions, 10.10 % of `.text`). Names printed `func_0x…` have **no decompiled body
in this dump** — registrar `func_0x1421cd360`, decryptors `d4f30`/`d4f70`, writer `c2d50`,
helpers `c2d70`/`c7880`/`SUB_140551380`, pointers `0x140fd9670`/`0x140f7b210`; pass 27 adds
settings helpers (`func_0x141c4aea0/141bb6770/141bb8e80/141bb7bf0`, `FUN_1421d8650`,
`func_0x1421d6a10`), catch-ctor `func_0x14213e3d0`, registry builders `func_0x141c578e0/
141cd5d40/141c5ff40`, metric writer `func_0x141d23660`, bitfield getter `func_0x14224ebe0`,
masked-pointer decoders `func_0x140543xxx/14054xxx`. Higher addresses = later, unread corpus.

**Five layers, in address order:**

1. **Library preamble** `0x140001000`–`0x140039fc0`. ISA-L/igzip-shaped DEFLATE inflate (12 fns);
   `nvapi_QueryInterface` bootstrap (lazy per-id caches, Wine probe); 53 NVAPI entry wrappers;
   `Initialize`/`Unload`.
2. **NVIDIA driver-loading shim** `0x14003a230`–`0x14003d330`. Replacement `LoadLibrary` for
   `nv*.dll` (D3DKMT, SetupAPI, service paths, Khronos keys); source of all 45 string literals.
3. **CRT/C++ static-init sea** `0x14003ffe0`–`0x1400fa760`. Five generator templates: the 181-B
   MSVC magic-static descriptor (**2,451**: `{+0x20 tag 1|2, +0x40 ctor, +0x48 vtable/FUN,
   +0x50 third, +0x58 payload, +0x60 shared PTR}` under a TLS guard), 209-B locale/facet statics
   (354), 58-B event thunks (284), 134-B XOR-40 + cipher registrations (61), 37-B `_onexit`
   stubs; pass-1 tail: 864 descriptors + 39 shared `PTR_DAT_14386a…` markers.
   [inference: per-record class/vtable descriptors; consumer ahead.]
4. **Typed registry machine** `0x1400fbcb0`–`0x14053ef50` (passes 2-tail–27) — the substance of
   the read through chunk 0235. No gameplay/network/asset code; named subsystem families:
   CompilerIDFilter (shader-compiler), physics/serialization schemas (`dm*`/`bc*`), telemetry
   (`circuitbreaker.*`, `gameruleset.gameoptions.*`). Pass 26 added the settings/variable
   family (first new construct since the registry began); pass 27 ends the machine.
5. **Runtime bootstrap + obfuscated dispatchers** `0x14053f6b0`–`0x14054ea50+` (pass 27, zone
   OPEN into chunk `0239`). PE `entry` trampoline `0x140540fd0`; module resolve + GetProcAddress;
   **signature scanner** `FUN_140541200` (VirtualProtect + memcmp patterns ending `0x90`/`0xcc`)
   → patch record at `0x143b79640`; **anti-tamper** (`"0x811C9DC5"` (FNV-1a basis) et al. → int3;
   CPUID FPU gate; Steam getters; first **settings consumers** (`FUN_141c295b0(name,100|20000,
   config)`). Under it a **masked-pointer layer**: pointers stored rotate-XOR encoded
   (`& 0x7ffffffffff8`, keys from `_DAT_143b79598+0x29…0x198`), decode helpers (`func_0x000140543xxx`,
   `FUN_140542320` ×19), GC `FUN_1405465f0`, and 16–47 KB obfuscated dispatchers (`halt_baddata`,
   `rdtsc`, POPCOUNT parity, LOCK copies; hottest `FUN_14054cf10` ×102, `FUN_14054ce70` ×131,
   `FUN_14054cd50` ×43). [inference: pointer-hiding + anti-tamper wrapper around the job/entity system.]

**The registry machine — nine cooperating constructs/variants:**

- **Name buffers.** Every registration/builder/settings row carries an XOR-8 ciphertext: key at
  `+0`, 24-bit length `+8`, done-flag `+0xb`, payload `+0xc`; `buf[i] ^= key[i & 7]`. Bands
  `0x1438b8e50`–`0x1439a9b2c` + pass-27 pages (`0x1439b0000+`, `0x143a155xx+`, `0x143b0c…`,
  low `0x143848d40+`). Plaintext never decoded.
- **Registration** — `func_0x1421cd360(out, ciphertext, hash32, 0, size, align, flags, 0, token,
  a10…a14, 0, 0, a16, a17, base)`: **7,952 ciphertext instances, all hash32 distinct** (pass 27
  adds 4 plaintext rows — `"teStructuredData"` `0x8df63eb2` ×2 flags 0/2, `"MirrorData"`
  `0x54d6a5f9`, `"TrackedData"` `0xf3318c83`; Corrections 16). `size` 3–`0x3bc0`, `align` 8
  default; `flags` 0 default, 1/2/3/4/5/6/7/8/10/0xb/0x51/0x80000000 known; 263/266/267-B rows
  carry 64-bit tokens (one token can repeat across consecutive rows); 266/256-B rows set a16
  from a runtime global (`_DAT_14410ff88…`); `base = out − 0xa0` verified every pass
  [inference: header slot].
- **No-output registration** — 242/246/252/257-B (first `0x140341b30`); args 10–18 =
  `FUN_140548d00, 0x140f7b210, FUN_140548f80, FUN_14053a070, FUN_140548d00, 0,0,0,0` —
  **arg17 = arg18 = 0**. Consumed: sorted `FUN_1404a82b0` copies no-output row
  `&DAT_144121c50` [inference: metadata rows; tables eat them].
- **Builder** — 365–574-B: allocator/pre-step → XOR-8 decrypt → `d4f30/d4f70(&out,&buf,hash,0)`
  → `d4fb0` → row `{+0x20 root, +0x28 instance, +0x30 0, +0x98 flag(1), +0x9c 0}` (registered
  row IS the object header); 369/365-B rootless forms store no root; two-buffer helpers
  `(size,&ct,0,hash)` ≥60, hashes can equal reg/record hashes (`0x6760479e`, `0xa7f15a16`,
  `0x15be7741`); per-TU allocators — key on shape (Corrections 13).
- **Copy wrapper** — 241/231/244-B: no decrypt; `c2d70(&dst,&src)` + `d4fb0`; `src = slot −
  0x20`; flag **0** at `+0x98`; 244-B stores `&PTR_s_CompilerIDFilter_*` + flag 1 (×7).
- **Sorted-insert builder** — **280 instances**; sorts exactly 2 56-B records keyed at `+8`
  (min-to-slot-0 pre-swap + insertion sort) + `d4fb0` + count = 2; pass 26/27 era: d4f30-heavy,
  rootless or output-rooted [inference: tiny 2-entry lookup tables consuming registry rows].
- **`{id,hash}` record** — 169/178-B; **326 instances**; pass 26 ×60 all matched, every hash
  registered earlier in the same pass. Ids span `0x1`–`0x18b`; many-to-one normal (`0x58b3d0d0`
  has 30 ids); 178-B third field = **alias registration hash** (Corrections 10).
- **Nested-atexit builder** — **261 instances** (526/542/558-B): row into a per-object global
  slot (scattered, Corrections 6), initializer pointers from 26+ families, `atexit(&LAB_142f0…)`
  + `c7880(&slot)`; slots can sit in the ciphertext page; some shared by two builders
  (`0x143c3ba40`, `0x14412cd58`) [inference: static-object shutdown].
- **Settings/variable registrar (pass 26+; the `other` zone)** — 209–399-B `int` fns: 1–3 XOR-8
  name decrypts, then **`FUN_141c58170(&desc, 0, &config, &name, &default)`** (configs
  `&DAT_144140740/758/144143410/1441d0150/14414fb48/1442a35e0`), a ~0x50-B descriptor (6+
  initializers, IEEE-754/int defaults), then `_onexit(&LAB_142f16xxx)` — one label per
  function, monotonic `0x142f16b90`→`0x142f2bff0` by pass 27; descriptors land
  `0x144130570`–`0x14413b7a0`. Pass 27 adds 308-B two-decrypt rows, float-limit descriptors
  (±FLT_MAX), singleton companions (122-B `FUN_14049f980`; 32–92-B stubs). No canary/guard.
  [inference: settings/console-variable registration; read back by `FUN_141c295b0` from
  `0x140541450` onward.]

Also present: **15 CompilerIDFilter shells** (`&PTR_s_CompilerIDFilter_*`; payloads are
registration outputs — pass 17). Guard furniture: TLS guards + stack cookies; **every
builder/sorted/atexit carries a canary, no registration, wrapper, or settings function does**.

**Passes 23–27 structural deltas (evidence).** Pass 23: 77–123-reg blocks, sextets `FUN_1417e20b0`→`FUN_141862c20`, per-TU allocator symbols + no-arg `FUN_1421c51f0…7780`. Pass 24: 174 regs all flags 0 / align 8, `base = out − 0xa0` 174/174. Pass 25: flags 4/2 return, builders root on registration outputs, 267-B = token+flags. **Pass 26 (286 regs, 557 files):** records ×60 and sorted ×31 return; no-output ×40; dynamic roots dominate; new sizes 266/256/260-B with runtime-global a16; flags 1/2/3/0x80000000; tokens 73/69; d4f30/d4f70 flip; **the settings/variable family appears** (`other` 92). **Pass 27 (1,259 files, other=1255):** the registry machine ends (`cd360` ×4 plaintext, records 0); **272 catch descriptors** (181-B: `func_0x00014213e3d0` + handler + `&SUB_140551380` + type_info); **282+ triplet stubs** (`func_0x000141c712f0` ×3 over far page `0x1439b0000–0x1439fa330`); **87 "Unknown" error rows** (`FUN_141b6c210`); **id→handler component registry** (`func_0x000141c5ff40` + `func_0x000141cd5d40`, ids 1–0x19, sizes 0x40–0x14e0); **dispatch-slot rows + readiness bitfields** (`func_0x00014224ebe0`; word[0]/[4] bits cleared 0x1→0x80000000, word[0xc] bits set 0x2000→…); **plaintext physics schemas** (`dmWorld` 0x194, `dmManifold` 0x100, `bcMtx44`…, rows at `0x1442a1920–0x1442a1bd8`); **runtime bootstrap + obfuscated dispatchers** from `0x14053f6b0`; `_onexit` labels to `0x142f2bff0`. [inference: the registry was data for the runtime that follows; the id-based consumer sits ahead at higher addresses.]

**Where the data lives** (full scattered slot list in Corrections 6):

| band | content |
|---|---|
| `0x143848d40`–`0x1438496xx` + `0x14384a0xx`–`0x14384a3xx` | XOR-8 ciphertext for the runtime bootstrap / obfuscated code (pass 27; **below** the old band start — key tables `0x143848d78`, `0x1438493c8`, `0x143849010…`, `0x14384a0f0…`, `0x1438496b0`) |
| `0x1438b8e50`–`0x1439a9b2c` | XOR-8 name/payload ciphertext (registry + settings; + 15 `PTR_s_CompilerIDFilter_*` labels; printable pre-XOR `0x143970f0c`, `s_5L7rL_F_14397b58c`, `s_Pjbl_ii_14397ffb4`; shutdown slots `0x14397a4d0`–`0x14397a528`, `0x14398bc98`–`0x14398bd58`; settings flag pair `0x143985430/438`) |
| `0x1439b0000`–`0x1439fa330` | triplet-stub object page (pass 27: `func_0x000141c712f0` ×3 + flag per 66-B stub) |
| `0x143a155xx`–`0x143aa36xx` + `0x143b0c…`–`0x143b77…` | XOR-40 key tables (`PTR_DAT_143a15870/16270/164f0`, `DAT_143a155f0`), settings names, locale/ciphertext `0x143a1ba20`, catch keys `PTR_DAT_143aa1dc8/1e78`, further key+payload pairs (pass 27) |
| `0x143cf0000`–`0x143d05000` + far `0x143d4c/d7/d9/da…`, `0x143f8…`–`0x143f94…` | **RTTI type_info descriptors** (Corrections 17; consumed by the 272 catch descriptors) |
| `0x143e99d90`–`0x14413b7a0` + earlier `0x143d/0x143e…` | registration outputs / instance slots; settings descriptors to `0x14413b7a0`; config globals `0x144140740/758/144143410/1441d0150/14414fb48` |
| `0x1441e18f0`–`0x1441e2230` | plaintext reg outputs (`teStructuredData` ×2, `MirrorData`, `TrackedData`); registry-list head `_DAT_1441e1c70` (239/253-B pushes, hashes `0x20b3d5a9 0x8fa75a30 0xa49ce182 0x91c74719 0x5d31669 0x3b9327d2`); dispatch-slot columns `0x1441e46a0–0x1441e67c8` (+ far `0x1441e9xxx–0x1441efxxx`) + readiness bitfield (`func_0x00014224ebe0`; word[0]/[4] cleared, word[0xc] set) |
| `0x1442a1920`–`0x1442a1bd8` | plaintext struct-schema rows (`dmWorld`, `dmManifold`, `bcMtx44`, …) with field tables `0x1442a0xxx–0x1442a1fxx`; record pools `0x1442e37xx–0x1442e5xxx`, `0x1442f0xxx–0x1442f14d2`, 0x1000-record 64 KiB pools `0x1442a3782`/`0x1442c3782` (patterns `0x101/0x3000000/0x7000000`, `0x4040404/0x5050505/0xf0f0f0f`) |
| `0x143280560`–`0x143280868`, `0x1432860a0`, `0x14328b728–b9f0`, `0x1432b9xxx`, `0x1433607xx–143361160`, `0x1433a0a80–0c40`, `0x1433a1xxx–0x1433a3xxx`, `0x14331b–14331cxxx` | settings/stub/list initializer label bands (pass 27 additions) |
| `0x14386a1e0`–`0x14386c788` (pass-1 tail) | 39 shared static-descriptor block pointers; shutdown slots scattered — Corrections 6 |
| `0x143b79598` (+0x29…+0x198), `0x143b79640/0x143b796a8`, `0x143b7a470`, `0x144180fa0` (row 0xe0), `0x144188200` | runtime config / key-table block, patch record, settings configs, per-thread rows |

**What it is for (reading conclusion).** Everything in `0x14003ffe0`–`0x14053ef50` is
startup-time registration, not gameplay: encrypted names registered with size/alignment/category
tables, builders instantiating them, wrappers cloning rows, 2-entry sorted tables and
`{id,hash,alias}` rows exposing types to an id-based consumer, settings/variable registrars,
catch-descriptor pairs wiring C++ RTTI — and, pass 27, the plaintext faces: physics schemas
(`dmWorld`, `dmManifold`, `bcMtx44`…), telemetry (`circuitbreaker.*`,
`gameruleset.gameoptions.*`), locale tables (`enUS`…`thTH`), component id→handler pairs, asset
path `c:\Prometheus\CompiledAssets`. From `0x14053f6b0` the runtime begins: module/export
resolution, signature scanning into patch records, anti-tamper int3 checks, CPUID gating,
Steam getters, first settings readers, and a masked-pointer/obfuscation layer under 16–47 KB
dispatchers (job/entity system). Confidence: counts/shapes/bands measured; construct labels are
shape-based inference; obfuscated dispatchers are read structurally.

**Known limits.** (a) Registrar + decryptors `func_0x…` — no body in the dump. (b) No name
buffer decrypted (cheapest: XOR-8 pages `0x1439a8ba0` and `0x14384a0…`; older printable
`0x143970f0c`). (c) `0x142f0…`–`0x142f2b…` atexit/onexit labels not in the dump (highest
`0x142f2bff0`). (d) Uninspected gaps (largest `0x1401a4e02`–`0x1401abad0` 27,854 B; 0x100–0x220
B steps look like padding). (e) Obfuscated dispatcher bodies (`FUN_140541450/14a0/1640/1b50`,
`FUN_14054ade0/cf10/e0c0/ea50`) resist decompilation — read structurally only.

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
| Sorted registry | min-to-slot-0 pre-swap + insertion sort of 2×56-B records keyed at `+8`; 280 instances; middle call is the ordinary pre-step; pass 26 d4f30-heavy, mostly rootless/output-rooted | `0x1400ff280` |
| Stack canary | `_DAT_143ac5f40 ^ stack` → `FUN_1426c3d40`; builders/sorted/atexit only | `0x1400fbf70` |
| Nested-atexit | guards + per-object global slot + `atexit(&LAB_142f0…)` + `c7880(&slot)` (1–2 arg); 261 instances, atexit labels to `0x142f16960`; slots can sit in the ciphertext page; `0x143c3ba40` (p24–25) and `0x14412cd58` (p26) shared | `0x1401003f0` |
| Registration schema | 18 args; zero hash reuse; a10–a14 + a17 rotate per block; **arg18 = out − 0xa0**; pass 26: flags 0 ×278 / 1 ×3 / 2 ×3 / 3 ×1 / 0x80000000 ×1, align 8 ×275 / 0x10 ×7 / 4 ×3 / 1 ×1, **266/256/260-B rows carry a runtime-global a16** | `0x1400fbcb0` |
| No-output registration | 242/246/252/257-B; arg17 = arg18 = 0; consumed by sorted `FUN_1404a82b0` (`&DAT_144121c50`) | `0x140341b30` |
| Token → category | nonzero arg9; one token per type default; repeats only across consecutive rows | `0x140126f90` |
| Size-tagged allocator | one-arg pre-step, argument = registered size; symbol is per-TU (16 symbols, Corrections 13) — key on the shape; `FUN_141901810(0)` allocates 0 | `0x140123f10` |
| Root regime | dynamic (registration outputs) dominates since pass 26; static `0x143cf/d…` minority | `0x1402133b0` |
| Decrypt-hash reuse | one hash can be reg + record + helper hash (`0x6760479e`, `0xa7f15a16`, `0x15be7741`, `0xb48f1d22`) | `0x1401e26f0` |
| No-arg pre-step family | `FUN_1421c51f0…FUN_1421c7780` (+ pass-26 additions `FUN_1410eadc0/141367b90/14140e210…`) precede most builders/sorted-inserts | `0x1402cff50` |
| Per-block furniture | one `(a10..a14, a17)` sextet per block, always a fresh output page; blocks 1–57 regs; far families `(&LAB_1413bb260…)`, `FUN_14191f4b0…` | `0x1402ea070` |
| Settings/variable registrar | 209–399-B `int` fns: 1–3 XOR-8 decrypts (new page `0x1439a8ba0+`) → `FUN_141c58170(&desc,0,&DAT_144140740\|758,&name,&default)` ×83 → ~0x50-B descriptor (6 initializers, float/int defaults) → `_onexit(&LAB_142f16xxx)` monotonic to `0x142f172b0`; no canary/guard | `0x1404b94e0` |
| Catch descriptor (181-B) | TLS guard + `func_0x00014213e3d0(&row,&desc)` + `{+0 handler FUN_1421…, +8 &LAB_14216…, +0x10 &SUB_140551380, +0x18 type_info @0x143cf/d…, +0x28 PTR_DAT_143aa1dc8\|1e78}`; 272 in pass 27 | `0x1404f8720` |
| Triplet stub (66-B) | `func_0x000141c712f0(&DAT_1439b…)` ×3 + `_DAT_…=0` + `_onexit(FUN_142f1xxxx)`; ~282/chunk; also `func_0x000141bb8e80` variant | `0x1404c88f0` |
| "Unknown" error row | 56/59-B `FUN_141b6c210(&DAT,"Unknown",&DAT,FUN_141exxxxx,0,0|&DAT)`; ×87 | `0x1404c2620` |
| Component registry (id→handler) | 58-B `func_0x000141c5ff40(&DAT,{u16 id,code* handler,u64})` ids 1–0x19 + 40/47-B `func_0x000141cd5d40(id,size,init,dtor1,dtor2)` sizes 0x40–0x14e0 | `0x1404f6cf0` |
| Dispatch-slot row + readiness bitfield | 129–286-B fns write 8 fn-pointers per row (`0x1441e46a0…` columns) then clear/set one bit via `func_0x00014224ebe0()` (word[0]/[4] cleared 0x1→0x80000000, word[0xc] set 0x2000→); consumed by popcount dispatchers | `0x14050d450` |
| Registry list push (239/253-B) | two TLS guards: `{hash32,&PTR_FUN_1433axxxx,(+&PTR_LAB_1433axxxx),atexit(&LAB_142f2axxx)}` then LIFO push to head `_DAT_1441e1c70` | `0x14050a3d0` |
| Struct schema (plaintext) | TLS guard → field table `{&name,off,size}` → `{&name,&fields,size,flag,&LAB_142c…|FUN_142cf2f60}` at `0x1442a1920+`; names plaintext (`dmWorld`, `bcMtx44`, …) | `0x14051d1d0` |
| Metric registration | 48-B `func_0x000141d23660(&DAT,type,"name","tag,k=v;…")`; names plaintext (`circuitbreaker.*`, `gameruleset.gameoptions.*`, `resmgr.show_state`) | `0x1404ed950` |
| Masked pointer | stored values rot-XOR encoded, `& 0x7ffffffffff8`; decode via per-TU helpers (`func_0x000140543xxx`, `FUN_140542320`), keys `_DAT_143b79598+n`; GC `FUN_1405465f0` (`0xa6c156b0120b4011` chain) | `0x14053f9a0` |
| Obfuscated dispatcher | 16–47 KB bodies: overlapping instructions, `halt_baddata`, `rdtsc`, POPCOUNT parity, LOCK copies, vtable+0x20/+0xa8 calls (arg 5); hottest `FUN_14054cf10` ×102, `FUN_14054ce70` ×131, `FUN_14054cd50` ×43 | `0x140541450` |
| Signature scan / patch record | `FUN_140541200`: VirtualProtect (`*_DAT_142f2d5a0`) + memcmp 9→1-B patterns (`0x142f7d2a8…`), bytes `0x90`/`0xcc`; `FUN_140541000` writes 0x58-B record to `0x143b79640` | `0x140541000` |

## Open threads (cheapest next query each; check/update every pass)

1. **Registrar body** `func_0x1421cd360` — not in the dump; schema known from 7,956 call sites
   incl. 4 plaintext rows (name = arg2).
2. **Decrypt a settings name** — XOR-8 pages `0x1439a8ba0` and `0x14384a0…`/`0x143848d…`
   (8-byte key, in-place XOR); names the settings the runtime reads via `FUN_141c295b0`.
3. **`FUN_141c58170` / `FUN_141c295b0` / `func_0x00014224ebe0` bodies** — FUN_-named, in
   unread corpus (~chunk `15xx`); settle settings set/get and the readiness-bitfield layout.
4. **Runtime config block** — dump `0x143b79598–0x143b796a8` (masked-pointer keys, patch
   record, module handle); who writes `*_DAT_143b79570` (`entry` target)? Which module is
   signature-scanned (`0x143b79640` vs encrypted names in page `0x143848d…`)? Dump one 0xad0
   job-node (`FUN_140545240` move-ctor gives the field map).
5. **Registry consumer ahead** — walk forward from `0x14054eb60` (chunk `0239`) for readers of
   the catch descriptors, dispatch rows, schema rows and list head `0x1441e1c70`.
6. **Firsts** — `"c:\\Prometheus\\CompiledAssets"` reader (grep forward for `14414e161`);
   Steam-getter callers; locale-table consumers (`0x1441881b0`, `0x1442a0118`).
7. **Uninspected gaps** — `0x1401a4e02`–`0x1401abad0` (27,854 B) unchanged; pass-26's
   settings-zone gap `0x1404b9547`–`0x1404babc0` (padding likely).
8. **CompilerIDFilter** — unchanged (last touched pass 21); payloads are regs.

CLOSED (machine): fd9670 recount; provenance complete; `0x1411b8070` unread corpus; thread 43
(`0x3fd91271` = `FUN_140290c50`); `--update`/`--init` ledger 5; shutdown "move" ledger 6; third
field = alias ledger 10; CompilerIDFilter payloads = regs; `0x39091531` ledger 11; **no-output
consumption (partial, pass 26)**; **zero-reuse conditioned (ledger 16)**; **static band =
type_info (ledger 17)**.

## Next pass

Resume at **`chunk_0239.txt`** (pass 27 ends mid-zone at `FUN_14054ea50`, a 56-B obfuscated
dispatcher — the `0x14053f6b0` runtime/obfuscated zone is OPEN). `state.json.next_chunk = 239`
agrees. The pass **length comes from `python scripts/pass_next.py`**; this file names only the
resume chunk. Run `pass_measure.py <start> <end>`, quote stdout verbatim in the record, run
`--update`, refresh this file. Watch for: (a) how far the obfuscated-dispatcher zone runs and
caller counts above ×131; (b) the first plaintext *reader* of the registry outputs (catch
descriptors, dispatch rows `0x1441e46a0+`, schemas `0x1442a1920+`, list head `0x1441e1c70`);
(c) ciphertext past `0x143b77…` and links to low page `0x143848d…`; (d) a second plaintext
`cd360` cluster or the XOR-8 name rows returning; (e) who writes `*_DAT_143b79570` and fills
the `0x143b79598` config block; (f) firsts: `c:\Prometheus\CompiledAssets` reader, Steam-getter
callers, locale-table consumers. Do not re-run a counted range through `--update` (ledger 5);
no ciphertext script line (ledger 7); leave the stale flags (ledgers 11/16) alone.

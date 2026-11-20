# Kickoff prompt for one read pass

Operator: paste everything under the line to the agent, as-is — nothing to edit.
The agent derives the chunk range itself from the ledger. (To force a different
range — e.g. an 11-chunk pass — append one line naming it.)

---

You are doing **one pass** of the systematic decompiled-`.text` read of
`Overwatch_clean.exe`. Work from `E:/overwatch-research/work/flood/`.

Work out what to read, in this order:
1. `PROTOCOL.md` — the process, in full.
2. `CODE_MAP.md` — the cumulative map, in full. The coverage table's last row names
   the most recent record; the "Next pass" section says where the read resumes.
3. `state.json` — the machine ledger. Your pass is chunks `next_chunk` ..
   `next_chunk + 7` (a protocol pass is 8 chunks). Cross-check that against
   CODE_MAP's "Next pass" section — if the two disagree, stop and report the
   discrepancy instead of guessing.
4. The most recent record in `ranges/` (last coverage-table row). Note the
   Corrections ledger in `CODE_MAP.md` supersedes any counts it quotes.

Then:
- Run `python scripts/pass_measure.py <first> <last>` and use its output as your
  measurement index (classes, zone skeleton, registration/decrypt/record censuses).
  Do not retype or hand-derive its numbers; anything it cannot classify, read raw.
- Read all 8 chunks completely, in order. Expect the previous pass's open construct
  to continue at the boundary (the record and CODE_MAP say which).
- Write the pass record to `ranges/<first>-<last>.md` (named by the `.text` range the
  script prints). Quote the script stdout verbatim in the headline-numbers section.
  Label evidence vs inference; give every zone boundary an address. Record unresolved
  things as open threads with the cheapest next query.
- Run `python scripts/pass_measure.py <first> <last> --update` to merge the pass into
  `state.json`.
- Update `CODE_MAP.md`: add the coverage row, refresh synthesis/conventions **only if
  something structural changed**, update open threads and rewrite the "Next pass"
  section (with the new resume chunk) for whoever follows. Cumulative numbers come
  from `state.json` — never hand-add. Keep the file under 300 lines.

Stop rules: if the context ceiling approaches mid-pass, stop at a chunk boundary, write
the read-state table (read vs pending chunks), and stop — do not start a chunk you
cannot finish. Ask for the reported context-usage number instead of guessing.

Deliverables: the new `ranges/` record, updated `CODE_MAP.md`, updated `state.json`.
When done, report the covered `.text` range, the chunk numbers, and the pass's key
findings.

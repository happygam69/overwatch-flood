"""Cheap census over flood chunks: python census.py START END"""
import re
import sys
import json
import collections

HDR = re.compile(r'^// ([0-9a-f]{16})_(\S+)\s+\(\d+ B\)')
META = re.compile(
    r'^// ([0-9a-f]+) \S+ size=(\d+) callers=(\d+) callees=(\d+) '
    r'section=(\S+) thunk=(true|false) sig=(.*)$')


def main(start, end):
    for n in range(start, end + 1):
        path = 'chunks/chunk_%04d.txt' % n
        text = open(path, encoding='utf-8', errors='replace').read()
        lines = text.splitlines()
        funcs = 0
        size_sum = 0
        callers = 0
        callees = 0
        thunks = 0
        sigs = collections.Counter()
        first = last = None
        callee_targets = collections.Counter()
        constructs = collections.Counter()
        strs = 0
        for ln in lines:
            m = HDR.match(ln)
            if m:
                funcs += 1
                first = first or m.group(1)
                last = m.group(1)
                continue
            m = META.match(ln)
            if m:
                size_sum += int(m.group(2))
                callers += int(m.group(3))
                callees += int(m.group(4))
                if m.group(6) == 'true':
                    thunks += 1
                sigs[m.group(7).strip()] += 1
                continue
            for t in re.findall(r'FUN_[0-9a-f]{9,16}', ln):
                callee_targets[t] += 1
            for kw in ('switchD', 'while (', 'do {', 'if (', 'goto ', 'WARNING',
                       'Indirect', 'unaff_', 'in_stack_', 'DAT_', 'uRam', 's_',
                       '__security_check', 'thunk_FUN', 'SUB', 'SUBPRIVATE'):
                c = ln.count(kw)
                if c:
                    constructs[kw] += c
            strs += len(re.findall(r'"', ln))
        top = callee_targets.most_common(6)
        print('== chunk %04d  %s -> %s' % (n, first, last))
        print('   funcs=%d textbytes=%d avg=%d callers=%d callees=%d thunks=%d distinct_callees=%d'
              % (funcs, size_sum, size_sum // max(funcs, 1), callers, callees, thunks,
                 len(callee_targets)))
        print('   sigs=%s' % dict(sigs.most_common(6)))
        print('   top_callees=%s' % ', '.join('%s x%d' % (k, v) for k, v in top))
        print('   constructs=%s' % dict(constructs.most_common(12)))


if __name__ == '__main__':
    main(int(sys.argv[1]), int(sys.argv[2]))

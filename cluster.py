"""Group functions in flood chunks by normalized body. python cluster.py START END"""
import re
import sys
import collections
import hashlib

HDR = re.compile(r'^// ([0-9a-f]{16})_(\S+)\s+\((\d+) B\)')
ADDR = re.compile(r'0x0001[0-9a-f]{9,}|00000001[0-9a-f]{10}|140[0-9a-f]{8,9}|143[0-9a-f]{8}')
FUNN = re.compile(r'FUN_1[0-9a-f]{8}')


def norm(body):
    b = ADDR.sub('<A>', body)
    b = FUNN.sub('<F>', b)
    return b


def main(start, end):
    fams = collections.defaultdict(list)  # hash -> [(addr, bytes, body)]
    for n in range(start, end + 1):
        text = open('chunks/chunk_%04d.txt' % n, encoding='utf-8', errors='replace').read()
        parts = re.split(r'(?m)^(?=// [0-9a-f]{16}_)', text)
        for p in parts:
            m = HDR.match(p)
            if not m:
                continue
            body = '\n'.join(p.splitlines()[1:])
            h = hashlib.md5(norm(body).encode()).hexdigest()[:10]
            fams[h].append((m.group(1), int(m.group(3)), body))
    order = sorted(fams.items(), key=lambda kv: -len(kv[1]))
    print('distinct families: %d  functions: %d' % (len(fams), sum(len(v) for v in fams.values())))
    for h, members in order[:25]:
        a0, b0, body = members[0]
        print('\n### family %s x%d  e.g. 0x%s (%d B)' % (h, len(members), a0, b0))
        print('\n'.join(body.splitlines()[:26]))


if __name__ == '__main__':
    main(int(sys.argv[1]), int(sys.argv[2]))

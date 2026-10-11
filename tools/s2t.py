"""Baseline: Simplified Chinese lang file -> Traditional (Taiwan phrases) via OpenCC s2twp.
Usage: py s2t.py <simplified.txt> <out.txt>
Tags (<color=..>, {0}, <sprite ..>) and keys are untouched by OpenCC (ASCII)."""
import sys
from opencc import OpenCC
cc = OpenCC('s2twp')
src, dst = sys.argv[1:3]
out = []
for i, line in enumerate(open(src, encoding='utf-8-sig', newline='').read().split('\r\n')):
    if i == 0:
        out.append('d=Traditional Chinese'); continue
    k, sep, v = line.partition('=')
    out.append(k + sep + cc.convert(v) if sep and not line.startswith('//') else line)
open(dst, 'w', encoding='utf-8', newline='').write('\r\n'.join(out))

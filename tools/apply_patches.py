"""Apply patches/*.txt (line|new zh value) onto 'Traditional Chinese.txt' by line number.
Aborts a patch line if tags/placeholders differ from English. Usage: py apply_patches.py [files...]"""
import sys, re, glob
D = r'E:\SteamLibrary\steamapps\common\Car Mechanic Simulator 2026 Demo\Car Mechanic Simulator 2026 Demo_Data\StreamingAssets\Localizations\English.txt'
en = open(D, encoding='utf-8-sig').read().splitlines()
F = 'Traditional Chinese.txt'
zh = open(F, encoding='utf-8', newline='').read().split('\r\n')
tag = lambda s: sorted(re.findall(r'<[^>]+>|\{\d*\}|\\n|%[sd]|\|', s))
n = bad = 0
for p in (sys.argv[1:] or sorted(glob.glob('patches/*.txt'))):
    for ln in open(p, encoding='utf-8'):
        ln = ln.rstrip('\r\n')
        if not ln.strip(): continue
        i, _, v = ln.partition('|')
        i = int(i) - 1
        k, _, e = en[i].partition('=')
        if tag(e) != tag(v):
            bad += 1; print('TAGMISMATCH', i+1, e, '|', v); continue
        zh[i] = k + '=' + v; n += 1
open(F, 'w', encoding='utf-8', newline='').write('\r\n'.join(zh))
print('applied', n, 'bad', bad)

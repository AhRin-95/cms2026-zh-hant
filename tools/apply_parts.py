"""Translate '!'-keyed part names using tools/parts_dict.txt (EN=>ZH root phrases, longest prefix wins).
Text after the root (A/B, model codes, '(...)') is kept verbatim. Unmatched lines are left alone."""
import re, collections
D = r'E:\SteamLibrary\steamapps\common\Car Mechanic Simulator 2026 Demo\Car Mechanic Simulator 2026 Demo_Data\StreamingAssets\Localizations\English.txt'
en = open(D, encoding='utf-8-sig').read().splitlines()
F = 'Traditional Chinese.txt'
zh = open(F, encoding='utf-8', newline='').read().split('\r\n')
d = sorted((l.rstrip('\n').split('=>') for l in open('tools/parts_dict.txt', encoding='utf-8') if '=>' in l),
           key=lambda p: -len(p[0]))
hit = 0
unmatched = []
for i, l in enumerate(en):
    if not l.startswith('!') or '=' not in l:
        continue
    k, _, e = l.partition('=')
    if e.startswith('^'):
        continue
    for a, b in d:
        if e.startswith(a) and (len(e) == len(a) or e[len(a)] in ' (-'):
            rest = e[len(a):].strip()
            zh[i] = k + '=' + b + (' ' + rest if rest else '')
            hit += 1
            break
    else:
        unmatched.append((i + 1, e))
open(F, 'w', encoding='utf-8', newline='').write('\r\n'.join(zh))
print('hit', hit, 'miss', len(unmatched))
c = collections.Counter(re.sub(r'\s*\([^)]*\)\s*$', '', e) for _, e in unmatched)
print(len(c))
for k, v in list(c.items())[:80]:
    print(v, k)

"""Sanity: line count, tag/'|' parity vs English, leftover simplified-ish terms."""
import re
D = r'E:\SteamLibrary\steamapps\common\Car Mechanic Simulator 2026 Demo\Car Mechanic Simulator 2026 Demo_Data\StreamingAssets\Localizations\English.txt'
en = open(D, encoding='utf-8-sig').read().splitlines()
zh = open('Traditional Chinese.txt', encoding='utf-8').read().splitlines()
tag = lambda s: sorted(re.findall(r'<[^>]+>|\{\d*\}|\n|%[sd]|\|', s))
print('lines', len(en), len(zh))
for i, (a, b) in enumerate(zip(en, zh)):
    if '=' in a and not a.startswith('//'):
        if a.partition('=')[0] != b.partition('=')[0]: print('KEY', i+1)
        elif tag(a.partition('=')[2]) != tag(b.partition('=')[2]): print('TAG', i+1, a.partition('=')[2][:70], '=>', b.partition('=')[2][:70])

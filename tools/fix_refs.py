"""'^key suffix' values = reference to another key's text + suffix. Suffix is mostly a car/seat MODEL NAME
(proper noun) -> keep English. Translate only descriptive words. Rewrites lines whose English value starts with '^'."""
import re
D = r'E:\SteamLibrary\steamapps\common\Car Mechanic Simulator 2026 Demo\Car Mechanic Simulator 2026 Demo_Data\StreamingAssets\Localizations\English.txt'
en = open(D, encoding='utf-8-sig').read().splitlines()
F = 'Traditional Chinese.txt'
zh = open(F, encoding='utf-8', newline='').read().split('\r\n')
WORD = [(r'\bLeather\b', '皮革'), (r'\bFabric\b', '布面'), (r'\bWall\b', '胎壁'),
        (r'\bCarbon Ceramic\b', '碳陶瓷'), (r'\bDrilled and slotted\b', '打孔劃線'),
        (r'\bDrilled\b', '打孔'), (r'\bSlotted\b', '劃線'), (r'\bCustom\b', '客製'),
        (r'\bStage (\d)\b', r'第 \1 階')]
n = 0
for i, l in enumerate(en):
    if '=' not in l or l.startswith('//'):
        continue
    k, _, e = l.partition('=')
    if not e.startswith('^'):
        continue
    m = re.match(r'(\^\S+)(\s*)(.*)$', e)
    ref, sp, suf = m.groups()
    for a, b in WORD:
        suf = re.sub(a, b, suf)
    if 7939 <= i + 1 <= 8082:  # seat names: Front/Rear = front/rear seat
        suf = re.sub(r'\bFront\b', '前座', suf)
        suf = re.sub(r'\bRear\b', '後座', suf)
    new = ref + sp + suf
    if zh[i] != k + '=' + new:
        zh[i] = k + '=' + new
        n += 1
open(F, 'w', encoding='utf-8', newline='').write('\r\n'.join(zh))
print('changed', n)

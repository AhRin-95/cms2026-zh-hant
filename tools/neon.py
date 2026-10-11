"""Neon tube names -> patches/015.txt"""
import re
D = r'E:\SteamLibrary\steamapps\common\Car Mechanic Simulator 2026 Demo\Car Mechanic Simulator 2026 Demo_Data\StreamingAssets\Localizations\English.txt'
en = open(D, encoding='utf-8-sig').read().splitlines()
col = {'White': '白色', 'Red': '紅色', 'Blue': '藍色', 'Green': '綠色', 'Orange': '橘色', 'Purple': '紫色', 'Teal': '青色'}
pos = {'floor-side': '地面側邊', 'floor': '地面', 'standing': '立式', 'wall-side': '牆面側邊', 'wall': '牆面'}
out = []
for n in range(11116, 11179):
    e = en[n - 1].partition('=')[2]
    m = re.match(r'Neon tube (Short|Long) \((\w+), ([\w-]+)\)$', e)
    if m:
        out.append(f"{n}|霓虹燈管 {'短' if m[1] == 'Short' else '長'}（{col[m[2]]}，{pos[m[3]]}）")
open('patches/015.txt', 'w', encoding='utf-8').write('\n'.join(out))
print(len(out))

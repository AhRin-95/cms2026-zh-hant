"""Print line|key|EN|ZH for lines a..b (1-based). Usage: py pair.py a b"""
import sys
D = r'E:\SteamLibrary\steamapps\common\Car Mechanic Simulator 2026 Demo\Car Mechanic Simulator 2026 Demo_Data\StreamingAssets\Localizations\English.txt'
en = open(D, encoding='utf-8-sig').read().splitlines()
zh = open('Traditional Chinese.txt', encoding='utf-8').read().splitlines()
a, b = int(sys.argv[1]), int(sys.argv[2])
for i in range(a-1, min(b, len(en))):
    if '=' in en[i] and not en[i].startswith('//'):
        k, _, e = en[i].partition('=')
        print(f'{i+1}|{k}|{e}|{zh[i].partition("=")[2]}')

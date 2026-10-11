"""Post-pass: Taiwan automotive terms. Usage: py apply_glossary.py <file.txt>  (in place)
Only touches text after the first '=' of each line."""
import sys
g = [l.rstrip('\n').split('\t') for l in open(__file__.replace('apply_glossary.py', 'glossary.tsv'), encoding='utf-8') if '\t' in l]
p = sys.argv[1]
out = []
for line in open(p, encoding='utf-8', newline='').read().split('\r\n'):
    k, s, v = line.partition('=')
    if s and not line.startswith('//'):
        for a, b in g: v = v.replace(a, b)
    out.append(k + s + v)
open(p, 'w', encoding='utf-8', newline='').write('\r\n'.join(out))

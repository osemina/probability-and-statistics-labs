"""usage: python mkpart.py DOC.json partN  -> writes partN_req.json (text + tables appended after the last body paragraph)"""
import json, sys, importlib
from docbuild import build, u16
from placeholders import table_requests, RAW
d = json.load(open(sys.argv[1], encoding='utf8'))['content']
body = d['tabs'][0]['documentTab']['body']['content']
at = body[-1]['startIndex'] - 1
mod = importlib.import_module(sys.argv[2])
R, t, end = build(mod.BLOCKS, at, first_page_break=False)
phs = []
for key in list(mod.TABLES) + list(getattr(mod, 'FIGURES', {})):
    i = t.find(f'[[{key}]]')
    if i >= 0:
        phs.append((at + 1 + u16(t[:i]), key))
for s, key in sorted(phs, reverse=True):
    if key.startswith('F'):
        name, w, h = mod.FIGURES[key]
        R.append({'deleteContentRange': {'range': {'startIndex': s, 'endIndex': s + u16(f'[[{key}]]')}}})
        R.append({'insertInlineImage': {'location': {'index': s}, 'uri': RAW.format(commit=sys.argv[3], name=name),
                                        'objectSize': {'width': {'magnitude': w, 'unit': 'PT'}, 'height': {'magnitude': h, 'unit': 'PT'}}}})
        continue
    sp = mod.TABLES[key]
    R.append({'deleteContentRange': {'range': {'startIndex': s, 'endIndex': s + u16(f'[[{key}]]') + 1}}})
    R += table_requests(s - 1, sp['rows'], sp['widths'], sp.get('center', ()), sp.get('boldcol0', False))
chunks, cur = [], []
for r in R:
    cur.append(r)
    if len(json.dumps(cur, separators=(',', ':'))) > 20000:
        chunks.append(cur[:-1]); cur = [r]
chunks.append(cur)
for k, c in enumerate(chunks):
    json.dump(c, open(f'{sys.argv[2]}_req{k}.json', 'w', encoding='utf8'), separators=(',', ':'))
print('chunks', len(chunks))
print(at, len(R), d['revisionId'])

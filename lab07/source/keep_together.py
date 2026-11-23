"""keepWithNext for: MC questions (7.N.) and their options except the last, lettered task items except the last,
and paragraphs that end with ':' (they introduce a list or a formula)."""
import json, re, sys
d = json.load(open(sys.argv[1], encoding='utf8'))['content']
body = d['tabs'][0]['documentTab']['body']['content']
items = []
for el in body:
    p = el.get('paragraph')
    if p:
        t = ''.join(e.get('textRun', {}).get('content', '') for e in p['elements']).rstrip('\n')
        items.append((el['startIndex'], el['endIndex'], t))
    else:
        items.append((None, None, None))
R = []
for i, (s, e, t) in enumerate(items):
    if s is None or s < 419:
        continue
    nxt = items[i + 1][2] if i + 1 < len(items) else None
    keep = False
    if re.match(r'^7\.\d+\. ', t) and nxt and re.match(r'^a\)\t', nxt):
        keep = True
    elif re.match(r'^[a-g]\)\t', t) and nxt and re.match(r'^[b-h]\)\t', nxt):
        keep = True
    elif t.endswith(':') and nxt:
        keep = True
    if keep:
        R.append({"updateParagraphStyle": {"range": {"startIndex": s, "endIndex": e}, "paragraphStyle": {"keepWithNext": True}, "fields": "keepWithNext"}})
print(d['revisionId'])
print(len(R))
json.dump(R, open('keep_req.json', 'w'), separators=(',', ':'))

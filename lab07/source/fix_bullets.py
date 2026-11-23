"""Remove inherited list bullets from paragraphs that should not be list items.
usage: python fix_bullets.py DOC.json START_HEADING_TEXT keep_text_prefix1 [keep2 ...]"""
import json, sys
doc = json.load(open(sys.argv[1], encoding='utf8'))['content']
start_txt, keep = sys.argv[2], sys.argv[3:]
body = doc['tabs'][0]['documentTab']['body']['content']
R, on = [], False
for el in body:
    p = el.get('paragraph')
    if not p:
        continue
    t = ''.join(e.get('textRun', {}).get('content', '') for e in p['elements'])
    if t.startswith(start_txt):
        on = True
    if on and p.get('bullet') and not any(t.startswith(k) for k in keep):
        s, e = el['startIndex'], el['endIndex']
        R.append({"deleteParagraphBullets": {"range": {"startIndex": s, "endIndex": e}}})
        R.append({"updateParagraphStyle": {"range": {"startIndex": s, "endIndex": e},
                  "paragraphStyle": {"indentStart": {"magnitude": 0, "unit": "PT"}, "indentFirstLine": {"magnitude": 0, "unit": "PT"}},
                  "fields": "indentStart,indentFirstLine"}})
# merge adjacent ranges
M = []
for r in R:
    k = list(r)[0]
    rg = r[k]['range']
    if M and list(M[-1])[0] == k and M[-1][k]['range']['endIndex'] == rg['startIndex'] and (k != 'updateParagraphStyle' or True):
        pass
    M.append(r)
print(doc['revisionId'])
print(json.dumps(R, separators=(',', ':')))

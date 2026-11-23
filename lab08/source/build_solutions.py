"""usage: python build_solutions.py DOC.json -> sol_calls.json (one request list per task, last task first, then Test Yourself)"""
import json, sys
import docbuild, sol
from docbuild import u16, col, GREEN
d = json.load(open(sys.argv[1], encoding='utf8'))['content']
body = d['tabs'][0]['documentTab']['body']['content']
paras = []
for el in body:
    if 'paragraph' in el:
        t = ''.join(e.get('textRun', {}).get('content', '') for e in el['paragraph']['elements'])
        paras.append((el['startIndex'], el['endIndex'], t.rstrip('\n')))


def find(prefix):
    for i, (s, e, t) in enumerate(paras):
        if t.startswith(prefix):
            return i
    raise KeyError(prefix)


stops = {k: f'Task {k + 1}.' for k in range(1, 10)}
stops[6] = 'Extra Practice'
stops[10] = 'Test Yourself'
calls = {}
TY = []
for q, letter in sol.MC_ANS.items():
    qi = find(f'8.{q}. ')
    for j in range(qi + 1, qi + 6):
        s, e, t = paras[j]
        if t.startswith(letter + ')\t'):
            TY.append({"updateTextStyle": {"range": {"startIndex": s + 3, "endIndex": e - 1}, "textStyle": {"bold": True, "foregroundColor": col(GREEN)}, "fields": "bold,foregroundColor"}})
            break
    else:
        raise SystemExit(f'no option for {q}')
ins = []
for q, txt in list(sol.FILL.items()) + [(k, f' Answer: {v}.') for k, v in sol.TF_ANS.items()]:
    s, e, t = paras[find(f'8.{q}. ')]
    ins.append((e - 1, txt))
for pos, txt in sorted(ins, reverse=True):
    TY.append({"insertText": {"location": {"index": pos}, "text": txt}})
    TY.append({"updateTextStyle": {"range": {"startIndex": pos + 1, "endIndex": pos + u16(txt)}, "textStyle": {"bold": True, "foregroundColor": col(GREEN)}, "fields": "bold,foregroundColor"}})
calls['ty'] = TY
for k in range(10, 0, -1):
    end_i = find(stops[k]) - 1
    s, e, t = paras[end_i]
    R, _, _ = docbuild.build(sol.S[k], e - 1, first_page_break=False)
    calls[f't{k}'] = R
for k, v in calls.items():
    json.dump(v, open(f'sol_{k}.json', 'w', encoding='utf8'), separators=(',', ':'))
    print(k, len(v), len(json.dumps(v, separators=(',', ':'))))
print(d['revisionId'])

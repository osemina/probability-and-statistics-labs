import sys, fitz, os
src, out = sys.argv[1], sys.argv[2]
os.makedirs(out, exist_ok=True)
d = fitz.open(src)
print(len(d), 'pages')
pages = range(len(d)) if len(sys.argv) < 4 else [int(x) for x in sys.argv[3].split(',')]
for i in pages:
    d[i].get_pixmap(dpi=int(os.environ.get('DPI', 60))).save(f'{out}/p{i+1:02d}.png')

import os, json, shutil
HERE = os.path.dirname(os.path.abspath(__file__))
FONTSRC = os.path.join(HERE, '..', 'tpl', 'word', 'fonts')

HEAD = """<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=1640, height=740" />
    <script src="https://cdn.jsdelivr.net/npm/gsap@3.14.2/dist/gsap.min.js"></script>
    <style>
      @font-face { font-family: "Montserrat"; font-weight: 700; src: url("assets/Montserrat-700.ttf"); }
      @font-face { font-family: "Open Sans"; font-weight: 400; src: url("assets/OpenSans-400.ttf"); }
      @font-face { font-family: "Open Sans"; font-weight: 600; src: url("assets/OpenSans-600.ttf"); }
      * { margin: 0; padding: 0; box-sizing: border-box; }
      html, body { width: 1640px; height: 740px; overflow: hidden; background: #ffffff; }
      #root { position: relative; width: 1640px; height: 740px; font-family: "Open Sans", sans-serif; color: #202020; }
      .abs { position: absolute; }
      .lbl { font: 700 26px "Montserrat"; white-space: nowrap; }
      .step { font: 700 22px "Montserrat"; color: #003e67; white-space: nowrap; }
      .sub { font: 400 21px "Open Sans"; color: #5f6368; white-space: nowrap; }
      .rt { font: 600 24px "Open Sans"; color: #202020; }
      .note { font: 400 23px "Open Sans"; color: #5f6368; line-height: 1.45; }
      .eq { font: 600 30px "Open Sans"; color: #003e67; white-space: nowrap; }
      .card { border-radius: 22px; background: #f3f3f0; }
      %CSS%
    </style>
  </head>
  <body>
    <div id="root" data-composition-id="main" data-start="0" data-duration="%DUR%" data-width="1640" data-height="740">
      <div id="scene" class="clip abs" data-start="0" data-duration="%DUR%" style="left:0;top:0;width:1640px;height:740px">
%BODY%
      </div>
    </div>
    <script>
      const tl = gsap.timeline({ paused: true });
%JS%
      tl.to({}, { duration: 0.01 }, %END%);
      window.__timelines = window.__timelines || {};
      window.__timelines["main"] = tl;
      tl.seek(0);
    </script>
  </body>
</html>
"""


def write(name, dur, body, js, css=''):
    d = os.path.join(HERE, name)
    os.makedirs(os.path.join(d, 'assets'), exist_ok=True)
    for src, dst in [('Montserrat-bold.ttf', 'Montserrat-700.ttf'), ('OpenSans-regular.ttf', 'OpenSans-400.ttf'),
                     ('OpenSans-bold.ttf', 'OpenSans-600.ttf')]:
        shutil.copy(os.path.join(FONTSRC, src), os.path.join(d, 'assets', dst))
    html = (HEAD.replace('%CSS%', css).replace('%DUR%', str(dur)).replace('%BODY%', body)
            .replace('%JS%', js).replace('%END%', str(dur - 0.01)))
    open(os.path.join(d, 'index.html'), 'w', encoding='utf8').write(html)
    json.dump({"$schema": "https://hyperframes.heygen.com/schema/hyperframes.json",
               "registry": "https://raw.githubusercontent.com/heygen-com/hyperframes/main/registry",
               "paths": {"blocks": "compositions", "components": "compositions/components", "assets": "assets"},
               "media": {"autoProxy": True}}, open(os.path.join(d, 'hyperframes.json'), 'w'), indent=2)
    json.dump({"name": name, "private": True, "type": "module",
               "scripts": {"check": "npx --yes hyperframes@0.8.133 check", "render": "npx --yes hyperframes@0.8.133 render"}},
              open(os.path.join(d, 'package.json'), 'w'), indent=2)

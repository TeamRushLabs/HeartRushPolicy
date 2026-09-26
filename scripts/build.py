from pathlib import Path
from html import escape
import json
ROOT = Path(__file__).resolve().parent.parent
BASE = 'https://teamrushlabs.github.io/HeartRushPolicy/'
data = json.loads((ROOT / 'data/privacy.json').read_text())
policies = data['policies']
css = '''*{box-sizing:border-box}body{margin:0;background:#f6f8fc;color:#17243a;font:17px/1.75 system-ui,-apple-system,sans-serif;word-break:keep-all;overflow-wrap:anywhere}header,main,footer{max-width:820px;margin:auto;padding:28px 24px}header{display:flex;justify-content:space-between;gap:20px;align-items:center}header a{font-weight:750;text-decoration:none;color:#245bca}main{background:white;border:1px solid #dde5f0;border-radius:20px;margin:0 auto 24px;padding:36px}h1{font-size:clamp(27px,5vw,40px);line-height:1.3;margin:12px 0}h2{font-size:21px;line-height:1.5;margin:30px 0 8px}p{margin:8px 0 16px}.muted,footer{color:#53647d;font-size:14px}.brand{color:#245bca;font-weight:700;letter-spacing:.04em}a{color:#245bca;text-underline-offset:3px}a:focus-visible,summary:focus-visible{outline:3px solid #245bca;outline-offset:4px}details{max-width:820px;margin:0 auto 24px;padding:16px 24px}summary{cursor:pointer}.languages{display:flex;flex-wrap:wrap;gap:12px;padding-top:16px}.languages a{padding:4px 8px;border:1px solid #dde5f0;border-radius:6px}footer{padding-top:0}@media(max-width:600px){header{padding:20px}main{margin:0 12px 20px;padding:24px 20px;border-radius:16px}}'''
(ROOT/'styles.css').write_text(css+'\n')
nav=' · '.join(f'<a href="{BASE}privacy/{lc}/" lang="{lc}">{label}</a>' for lc,label in [('ko-KR','한국어'),('en-US','English')])
langs='<div class="languages">'+''.join(f'<a href="{BASE}privacy/{escape(lc)}/" lang="{escape(lc)}">{escape(lc)}</a>' for lc in sorted(policies))+'</div>'
def render(lc,canonical):
 p=policies[lc]; rtl=' dir="rtl"' if lc.split('-')[0] in ('ar','iw','he','fa','ur') else ''
 sections=''.join(f'<section><h2>{escape(s["title"])}</h2><p>{escape(s["body"])}</p></section>' for s in p['sections'])
 return f'''<!doctype html>
<html lang="{escape(lc)}"{rtl}><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="description" content="Drawly · RushLabs — {escape(p['title'])}"><title>Drawly · {escape(p['title'])} | RushLabs</title><link rel="canonical" href="{canonical}"><link rel="stylesheet" href="{BASE}styles.css"></head>
<body><header><a href="{BASE}">Drawly · RushLabs</a><nav aria-label="Language">{nav}</nav></header><main><p class="brand">DRAWLY / RUSHLABS</p><h1>{escape(p['title'])}</h1><p class="muted">{escape(p['updated'])}</p><p>{escape(p['intro'])}</p>{sections}<p><a href="mailto:june1012june@gmail.com">june1012june@gmail.com</a></p></main><details><summary>Languages / 언어 ({len(policies)})</summary>{langs}</details><footer>RushLabs · Drawly (formerly HeartRush)<br>© 2026 RushLabs</footer></body></html>\n'''
for lc in policies:
 dest=ROOT/'privacy'/lc;dest.mkdir(parents=True,exist_ok=True);(dest/'index.html').write_text(render(lc,BASE+'privacy/'+lc+'/'))
(ROOT/'index.html').write_text(render('en-US',BASE))
(ROOT/'privacy/index.html').write_text(render('en-US',BASE+'privacy/'))
(ROOT/'.nojekyll').write_text('')
print(f'Built {len(policies)} localized static policies, root and privacy landing pages.')

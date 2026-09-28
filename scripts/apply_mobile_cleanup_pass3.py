from pathlib import Path
import re

root = Path(__file__).resolve().parents[1]

common_style = r'''
<style id="vip-mobile-pass-3">
/* Mobile cleanup pass 3: baseline dots + calmer first viewport */
.vip-dot{
  display:inline-block !important;
  font-size:.27em !important;
  line-height:1 !important;
  vertical-align:baseline !important;
  transform:none !important;
  position:relative;
  top:.08em;
  margin:0 .025em !important;
  letter-spacing:0 !important;
}
</style>
'''

home_style = r'''
<style id="vip-home-mobile-pass-3">
@media (max-width:820px){
  .fp-hero{
    min-height:0 !important;
    padding:68px 0 0 !important;
    align-items:flex-start !important;
  }
  .fp-hero-content{
    display:block !important;
    width:calc(100% - 24px) !important;
    min-height:0 !important;
    padding-top:0 !important;
    gap:0 !important;
  }
  .fp-hero-left{
    max-width:100% !important;
    min-height:calc(100svh - 68px) !important;
    display:flex !important;
    flex-direction:column !important;
    justify-content:center !important;
    padding:20px 0 28px !important;
  }
  .fp-hero-quiz{
    width:100% !important;
    max-width:100% !important;
    margin:0 0 30px !important;
    scroll-margin-top:76px !important;
  }
}

@media (max-width:480px){
  .fp-hero{padding-top:64px !important}
  .fp-hero-content{width:calc(100% - 20px) !important}
  .fp-hero-left{
    min-height:calc(100svh - 64px) !important;
    padding:18px 0 26px !important;
  }
  .fp-hero-quiz{margin-bottom:24px !important}
}
</style>
'''

def replace_style(html: str, style_id: str, replacement: str) -> str:
    pattern = re.compile(rf'<style id=["\']{re.escape(style_id)}["\']>.*?</style>\s*', re.S)
    html = pattern.sub('', html)
    marker = '</body>'
    if marker in html:
        return html.replace(marker, replacement + '\n' + marker, 1)
    return html + replacement

for path in root.rglob('*.html'):
    html = path.read_text(encoding='utf-8')
    html = replace_style(html, 'vip-mobile-pass-3', common_style)
    if path == root / 'index.html':
        html = replace_style(html, 'vip-home-mobile-pass-3', home_style)
    path.write_text(html, encoding='utf-8')

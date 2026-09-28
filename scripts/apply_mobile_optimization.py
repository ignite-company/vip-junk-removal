from pathlib import Path

root = Path(__file__).resolve().parents[1]

home_css = r'''

/* =========================================================
   MOBILE OPTIMIZATION PASS 2
   Compact first load, thumb-friendly controls, safer iPhone spacing
========================================================= */
.vip-dot{
  display:inline-block;
  font-size:.36em;
  line-height:1;
  transform:translateY(-.46em);
  margin:0 .015em;
  letter-spacing:0;
}

@media (max-width:820px){
  html{scroll-padding-top:72px}
  #vip-pro{padding-bottom:72px}
  .fp-shell{width:calc(100% - 24px)}

  .fp-header{
    position:fixed;
    background:rgba(37,16,63,.97);
    border-bottom:1px solid rgba(212,175,55,.45);
    backdrop-filter:blur(10px);
    -webkit-backdrop-filter:blur(10px);
  }
  .fp-header-inner{
    width:calc(100% - 20px);
    min-height:68px;
    gap:12px;
  }
  .fp-logo-wrap{width:112px;flex:0 0 112px}
  .fp-wordmark{line-height:.78}
  .fp-wordmark strong{font-size:30px;letter-spacing:-.045em}
  .fp-wordmark small{margin-top:5px;font-size:7px;letter-spacing:.22em}
  .fp-mobile-btn{
    width:42px;
    height:42px;
    padding:9px;
    border-radius:8px;
    background:rgba(255,255,255,.04);
  }
  .fp-mobile-btn span{margin:4px 0}
  .fp-mobile-menu{
    position:fixed;
    top:68px;
    max-height:calc(100dvh - 68px);
    overflow-y:auto;
    overscroll-behavior:contain;
    padding:8px 12px calc(18px + env(safe-area-inset-bottom));
  }
  .fp-mobile-menu a,
  .fp-mobile-submenu-toggle{
    min-height:46px;
    padding:0 10px;
    display:flex;
    align-items:center;
    font-size:12px;
  }
  .fp-mobile-submenu a{min-height:42px;padding:0 10px;font-size:11.5px}

  .fp-hero{
    min-height:0;
    padding:76px 0 30px;
    align-items:flex-start;
  }
  .fp-hero-photo{background-position:60% center;transform:scale(1.01)}
  .fp-hero-shade{
    background:linear-gradient(180deg,rgba(22,8,35,.76) 0%,rgba(37,16,63,.91) 48%,rgba(22,8,35,.97) 100%);
  }
  .fp-hero-content{
    width:calc(100% - 24px);
    min-height:0;
    gap:20px;
    padding-top:6px;
  }
  .fp-hero-left{max-width:100%;padding:0}
  .fp-hero-kicker{max-width:100%;margin-bottom:7px;font-size:10px;line-height:1.3;letter-spacing:.02em}
  .fp-hero h1{
    margin-bottom:12px;
    font-size:clamp(42px,12.5vw,58px);
    line-height:.92;
    letter-spacing:-.018em;
  }
  .fp-hero-desc{
    max-width:34rem;
    margin-bottom:16px;
    font-size:14px;
    line-height:1.48;
    font-weight:600;
  }
  .fp-hero-actions{gap:8px;margin-bottom:0}
  .fp-hero-actions a{
    min-height:50px;
    padding:0 16px;
    border-radius:7px;
    font-size:12.5px;
  }

  .fp-hero-quiz{
    max-width:100%;
    margin-top:0;
    padding:5px;
    border-radius:9px;
    background:rgba(22,8,35,.78);
    box-shadow:0 14px 34px rgba(0,0,0,.2);
    backdrop-filter:none;
    -webkit-backdrop-filter:none;
    scroll-margin-top:76px;
  }
  .fp-hero-quiz .fp-quiz-shell{border-width:3px;border-radius:7px}
  .fp-hero-quiz .fp-quiz-progress{padding:14px 13px 0}
  .fp-hero-quiz .fp-quiz-screen{padding:22px 13px 18px}
  .fp-hero-quiz .fp-quiz-screen > h3{font-size:clamp(30px,8.5vw,40px);line-height:1}
  .fp-hero-quiz .fp-quiz-description{font-size:13px;line-height:1.45}
  .fp-hero-quiz .fp-quiz-answer-grid{gap:8px;margin-top:16px}
  .fp-hero-quiz .fp-quiz-answer{min-height:70px;padding:9px 10px;border-radius:7px}
  .fp-hero-quiz .fp-quiz-answer-icon{width:40px;height:40px;font-size:17px}
  .fp-hero-quiz .fp-quiz-answer strong{font-size:12px;line-height:1.25}
  .fp-hero-quiz .fp-contact-field input{min-height:52px;font-size:16px}

  .fp-reviews{min-height:0}
  .fp-review-score{min-height:145px;padding:18px 14px}
  .fp-review-stars{font-size:27px}
  .fp-review-card{width:268px;flex-basis:268px;padding:20px 17px}

  .fp-about{padding:52px 0 46px}
  .fp-about-grid,.fp-local-grid,.fp-ba-grid{gap:28px}
  .fp-about-photo{height:315px;border-radius:8px}
  .fp-about-badge{width:92px;height:92px;right:8px;top:-14px;border-width:4px}
  .fp-about-badge strong{font-size:20px}
  .fp-about-copy h2{margin-bottom:16px;font-size:clamp(38px,10.8vw,50px);line-height:.98}
  .fp-about-copy p,.fp-about-bottom p{font-size:15px;line-height:1.58}
  .fp-about-bottom{margin-top:28px}

  .fp-popular{padding:50px 0}
  .fp-heading{margin-bottom:34px}
  .fp-heading h2{margin-bottom:10px;font-size:clamp(38px,10.8vw,52px);line-height:.98}
  .fp-heading p{font-size:15px;line-height:1.55}
  .fp-icon-grid{gap:8px}
  .fp-icon-service{min-height:132px;padding:10px 6px}
  .fp-line-icon{width:64px;height:64px;margin-bottom:10px}
  .fp-icon-service strong{font-size:12px;line-height:1.25}

  .fp-trust{padding:18px 0}
  .fp-trust-grid{gap:8px}
  .fp-trust-item{min-height:62px;padding:11px 10px}
  .fp-trust-copy{padding-left:11px}
  .fp-trust-copy strong{font-size:10.5px}
  .fp-trust-copy span{font-size:8.5px}

  .fp-help{padding:50px 0 54px}
  .fp-help-heading{margin-bottom:28px}
  .fp-help-heading p{font-size:10px;letter-spacing:.14em}
  .fp-help-heading h2{font-size:clamp(38px,10.8vw,52px)}
  .fp-help-grid{gap:10px}
  .fp-help-card{min-height:220px;border-width:2px}
  .fp-help-card-content{padding:16px 13px 14px}
  .fp-help-card h3{font-size:17px}
  .fp-help-card p{font-size:12px;line-height:1.4}

  .fp-local{padding:52px 0}
  .fp-mini-title{font-size:12px}
  .fp-local-copy h2{margin-bottom:16px;font-size:clamp(40px,11.5vw,54px);line-height:.95}
  .fp-local-copy > p{font-size:15px;line-height:1.58}
  .fp-local-checks{gap:10px;margin:20px 0 22px}
  .fp-local-checks div{font-size:13px}
  .fp-local-photo{height:320px;border-radius:8px;overflow:hidden}

  .fp-pricing{padding:50px 0}
  .fp-pricing-head > p{font-size:12px}
  .fp-pricing-head h2{margin-bottom:14px;font-size:clamp(48px,14vw,64px);line-height:.92}
  .fp-price-note{margin-bottom:20px;font-size:16px}
  .fp-pricing-buttons{gap:8px}
  .fp-pricing-buttons a,.fp-ba-actions a{min-height:50px;font-size:12.5px}

  .fp-price-factors{padding:52px 0 34px}
  .fp-price-heading{margin-bottom:34px}
  .fp-price-heading h2{margin-bottom:14px;font-size:clamp(38px,10.8vw,50px)}
  .fp-price-heading p{font-size:15px;line-height:1.55}
  .fp-factor-grid{gap:14px}
  .fp-factor{min-height:270px}
  .fp-factor h3{font-size:34px}
  .fp-factor-art{height:150px}

  .fp-before-after{padding:52px 0}
  .fp-ba-slider{height:300px;border-radius:8px}
  .fp-ba-content h2{margin-bottom:14px;font-size:clamp(40px,11.5vw,54px)}
  .fp-ba-content > p{font-size:15px;line-height:1.58}

  .fp-google-profile{padding:50px 0}
  .fp-google-profile-inner{gap:24px}
  .fp-google-profile-copy h2{font-size:clamp(40px,11.5vw,54px)}
  .fp-google-profile-copy > p:last-child{font-size:15px;line-height:1.58}
  .fp-google-profile-card{padding:22px 17px;border-radius:8px}

  .fp-final-cta{min-height:420px;padding:52px 0}
  .fp-final-inner > p{font-size:12px}
  .fp-final-inner h2{margin-bottom:20px;font-size:clamp(46px,13vw,62px);line-height:.92}

  .fp-footer{padding-top:46px;padding-bottom:90px}
  .fp-footer-grid{gap:26px 18px}
  .fp-footer-brand .fp-wordmark{width:auto;max-height:none}
  .fp-footer-brand .fp-wordmark strong{font-size:34px}
  .fp-footer-brand .fp-wordmark small{font-size:8px}

  .fp-mobile-bottom{
    padding:7px 9px calc(7px + env(safe-area-inset-bottom));
    box-shadow:0 -4px 18px rgba(0,0,0,.11);
  }
  .fp-mobile-bottom a{min-height:50px;border-radius:8px;font-size:12px}
}

@media (max-width:600px){
  .fp-help-grid{grid-template-columns:1fr}
  .fp-help-card{min-height:260px}
  .fp-footer-grid{grid-template-columns:1fr}
  .fp-footer-brand{grid-column:auto}
  .fp-trust-grid{grid-template-columns:1fr}
  .fp-trust-item:last-child{grid-column:auto;justify-content:flex-start}
}

@media (max-width:480px){
  .fp-shell{width:calc(100% - 20px)}
  .fp-header-inner{width:calc(100% - 18px);min-height:64px}
  .fp-logo-wrap{width:104px;flex-basis:104px}
  .fp-wordmark strong{font-size:28px}
  .fp-wordmark small{font-size:6.5px;letter-spacing:.20em}
  .fp-mobile-btn{width:40px;height:40px}
  .fp-mobile-menu{top:64px;max-height:calc(100dvh - 64px)}
  .fp-hero{padding:70px 0 24px}
  .fp-hero-content{width:calc(100% - 20px);gap:16px;padding-top:4px}
  .fp-hero-kicker{font-size:9.5px}
  .fp-hero h1{font-size:clamp(39px,12vw,52px);margin-bottom:10px}
  .fp-hero-desc{font-size:13.5px;line-height:1.45;margin-bottom:14px}
  .fp-hero-actions a{min-height:48px;font-size:12px}
  .fp-hero-quiz{padding:4px}
  .fp-hero-quiz .fp-quiz-progress{padding:12px 11px 0}
  .fp-hero-quiz .fp-quiz-screen{padding:19px 11px 16px}
  .fp-hero-quiz .fp-quiz-screen > h3{font-size:clamp(28px,8.2vw,36px)}
  .fp-hero-quiz .fp-quiz-answer-grid{grid-template-columns:1fr}
  .fp-hero-quiz .fp-quiz-answer{min-height:62px;grid-template-columns:38px minmax(0,1fr);padding:8px 10px}
  .fp-hero-quiz .fp-quiz-answer-icon{width:38px;height:38px}
  .fp-review-card{width:252px;flex-basis:252px}
  .fp-about-photo,.fp-local-photo{height:285px}
  .fp-ba-slider{height:270px}
}
'''

generic_css = r'''

/* Mobile optimization pass */
.vip-dot{display:inline-block;font-size:.36em;line-height:1;transform:translateY(-.46em);margin:0 .015em;letter-spacing:0}
@media(max-width:820px){
  html{scroll-padding-top:76px}
  .shell{width:calc(100% - 24px)}
  .header{min-height:70px;padding:0 12px;box-shadow:0 5px 18px rgba(0,0,0,.12)}
  .wordmark{line-height:.78}
  .wordmark strong{font-size:30px;letter-spacing:-.045em}
  .wordmark small{margin-top:5px;font-size:7px;letter-spacing:.22em}
  .mobile-btn{width:42px;height:40px;padding:9px;border-radius:8px}
  .mobile-menu{top:70px;max-height:calc(100dvh - 70px);overflow-y:auto;overscroll-behavior:contain;padding:10px 14px calc(18px + env(safe-area-inset-bottom))}
  .mobile-menu strong{padding:12px 0 5px;font-size:9px;letter-spacing:.08em}
  .mobile-menu a{min-height:42px;display:flex;align-items:center;padding:0;border-bottom:1px solid rgba(255,255,255,.08);font-size:11.5px}
  .hero{min-height:0}
  .hero-inner{padding:48px 0 44px}
  .eyebrow{margin-bottom:8px;font-size:10px}
  .hero h1{margin-bottom:14px;font-size:clamp(42px,12vw,58px);line-height:.92}
  .hero p{margin-bottom:20px;font-size:15px;line-height:1.55}
  .actions{gap:8px}
  .btn,.btn-outline{min-height:50px;padding:0 18px;border-radius:7px;font-size:12px}
  .trust{gap:8px 14px;margin-top:18px;font-size:10.5px}
  .section{padding:54px 0}
  .grid2,.faq{gap:28px}
  .section h2{margin-bottom:14px;font-size:clamp(38px,10.8vw,52px);line-height:.98}
  .body{font-size:15px;line-height:1.65}
  .photo{height:320px;border-radius:8px}
  .check-grid{gap:9px;margin:20px 0}
  .check{font-size:12.5px}
  .cards{gap:12px}
  .card{padding:22px 18px;border-radius:8px}
  .card h3{font-size:16px}
  .card p{font-size:12.5px;line-height:1.55}
  .area-links{gap:8px;margin-top:20px}
  .area-links a{padding:13px 12px;font-size:11.5px}
  .process{gap:10px;margin-top:22px}
  .step{padding:20px 16px}
  .step strong{font-size:30px}
  .faq details{padding:15px 0}
  .faq summary{font-size:13px;line-height:1.4}
  .faq details p{font-size:12.5px;line-height:1.6}
  .review-grid{gap:12px}
  .review{padding:22px 18px}
  .cta{min-height:360px;padding:48px 0}
  .cta h2{font-size:clamp(42px,12vw,58px)}
  .cta p{font-size:14px;line-height:1.55}
  .footer{padding:46px 0 24px}
  .footer-grid{gap:28px 18px}
}
@media(max-width:600px){
  .cards,.review-grid,.area-links,.process,.check-grid,.footer-grid{grid-template-columns:1fr}
  .actions{display:grid}
  .actions a{width:100%}
}
@media(max-width:480px){
  .shell{width:calc(100% - 20px)}
  .header{min-height:64px;padding:0 10px}
  .wordmark strong{font-size:28px}
  .wordmark small{font-size:6.5px;letter-spacing:.20em}
  .mobile-btn{width:40px;height:38px}
  .mobile-menu{top:64px;max-height:calc(100dvh - 64px)}
  .hero-inner{padding:40px 0 38px}
  .hero h1{font-size:clamp(38px,11.7vw,50px)}
  .hero p{font-size:14px;line-height:1.5}
  .section{padding:48px 0}
  .section h2{font-size:clamp(36px,10.5vw,48px)}
  .photo{height:285px}
  .cta{min-height:320px;padding:42px 0}
  .cta h2{font-size:clamp(38px,11vw,50px)}
}
'''

replacement = '<strong>V<span class="vip-dot">.</span>I<span class="vip-dot">.</span>P<span class="vip-dot">.</span></strong>'

count = 0
for p in root.rglob('*.html'):
    s = p.read_text(encoding='utf-8')
    s = s.replace('<strong>V.I.P.</strong>', replacement)

    if p.name == 'index.html' and p.parent == root:
        marker = '\n</style>\n\n<div id="vip-pro">'
        if 'MOBILE OPTIMIZATION PASS 2' not in s:
            if marker not in s:
                raise RuntimeError('Homepage style marker missing')
            s = s.replace(marker, home_css + marker, 1)
    else:
        if '/* Mobile optimization pass */' not in s:
            idx = s.find('</style><script type="application/ld+json">')
            if idx != -1:
                s = s[:idx] + generic_css + s[idx:]
            else:
                h = s.find('</head>')
                pos = s.rfind('</style>', 0, h)
                if pos != -1:
                    s = s[:pos] + generic_css + s[pos:]

    p.write_text(s, encoding='utf-8')
    count += 1

print(f'Patched {count} HTML files for VIP mobile optimization.')

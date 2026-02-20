import streamlit as st
import os

st.set_page_config(
    page_title="Somos Tu Crédito | Vehículos & Financiamiento",
    page_icon="🏅",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ── Datos de contacto ─────────────────────────────────────────────────────────
WA_NUMBER = "573134138598"
WA_URL    = f"https://wa.me/{WA_NUMBER}"
FB_URL    = "https://www.facebook.com/somostucredito"
IG_URL    = "https://www.instagram.com/somostucredito_/"
PHONE     = "+57 313 413 8598"

# ── Catálogo de vehículos ─────────────────────────────────────────────────────
CARS = [
    {
        "img":    "https://images.unsplash.com/photo-1583121274602-3e2820c69888?w=700&q=80",
        "badge":  "NUEVO", "badge_class": "",
        "name":   "SUV Familiar Premium",
        "specs":  "2024 · Automático · 4WD · 7 puestos",
        "price":  "$89.900.000",
        "msg":    "Hola, me interesa el SUV Familiar Premium",
    },
    {
        "img":    "https://images.unsplash.com/photo-1494976388531-d1058494cdd8?w=700&q=80",
        "badge":  "OFERTA", "badge_class": "oferta",
        "name":   "Sedán Ejecutivo",
        "specs":  "2023 · Automático · Full equipo · 48.000 km",
        "price":  "$54.500.000",
        "msg":    "Hola, me interesa el Sedán Ejecutivo",
    },
    {
        "img":    "https://images.unsplash.com/photo-1555215695-3004980ad54e?w=700&q=80",
        "badge":  "NUEVO", "badge_class": "",
        "name":   "Pick-Up 4×4 Diésel",
        "specs":  "2024 · Manual · 4×4 · Motor Diésel",
        "price":  "$112.000.000",
        "msg":    "Hola, me interesa la Pick-Up 4x4",
    },
    {
        "img":    "https://images.unsplash.com/photo-1618843479313-40f8afb4b4d8?w=700&q=80",
        "badge":  "SEMINUEVO", "badge_class": "",
        "name":   "Hatchback Urbano Híbrido",
        "specs":  "2022 · Automático · 32.000 km · Híbrido",
        "price":  "$47.000.000",
        "msg":    "Hola, me interesa el Hatchback Urbano",
    },
    {
        "img":    "https://images.unsplash.com/photo-1568605117036-5fe5e7bab0b7?w=700&q=80",
        "badge":  "NUEVO", "badge_class": "",
        "name":   "Coupé Deportivo Turbo",
        "specs":  "2024 · Automático · Turbo · Full LED",
        "price":  "$135.000.000",
        "msg":    "Hola, me interesa el Coupé Deportivo",
    },
    {
        "img":    "https://images.unsplash.com/photo-1533473359331-0135ef1b58bf?w=700&q=80",
        "badge":  "SEMINUEVO", "badge_class": "",
        "name":   "Minivan 8 Puestos",
        "specs":  "2022 · Automático · 8 puestos · A/C Triple",
        "price":  "$78.500.000",
        "msg":    "Hola, me interesa la Minivan 8 puestos",
    },
]

# ─────────────────────────────────────────────────────────────────────────────
# HELPER: inyecta HTML sin indentación (evita que Streamlit lo trate como código)
# ─────────────────────────────────────────────────────────────────────────────
def H(raw: str) -> None:
    # quita indentación de líneas para que Markdown no las convierta en <code>
    lines = [ln.strip() for ln in raw.strip().splitlines()]
    st.markdown("\n".join(lines), unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
# CSS — bloque único, sin f-string (sin riesgo de escape)
# ══════════════════════════════════════════════════════════════════════════════
CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@600;700;800&family=Outfit:wght@300;400;500;600&display=swap');
:root{
--gold:#C9A84C;--gold-lt:#E8D369;--gold-dk:#96780E;
--black:#0B0B0B;--dark:#141414;--dark2:#1E1E1E;
--white:#FFFFFF;--offwhite:#F9F7F2;--gray-lt:#F0EDE6;--gray-mid:#D8D0C0;
--text:#2C2A25;--muted:#7A7060;
--sh-gold:0 8px 32px rgba(201,168,76,0.28);
--sh-card:0 4px 28px rgba(11,11,11,0.09);
--sh-lg:0 20px 60px rgba(11,11,11,0.16);
--r:18px;--r-sm:10px;
}
html,body,.stApp{background:var(--offwhite)!important;font-family:'Outfit',sans-serif!important;color:var(--text)!important;}
#MainMenu,footer,header{visibility:hidden;}
.block-container{padding:0!important;max-width:100%!important;}
::-webkit-scrollbar{width:6px;}
::-webkit-scrollbar-track{background:var(--offwhite);}
::-webkit-scrollbar-thumb{background:var(--gold);border-radius:3px;}
@keyframes fadeDown{from{opacity:0;transform:translateY(-18px)}to{opacity:1;transform:translateY(0)}}
@keyframes fadeUp{from{opacity:0;transform:translateY(22px)}to{opacity:1;transform:translateY(0)}}
@keyframes scaleIn{from{opacity:0;transform:scale(0.94)}to{opacity:1;transform:scale(1)}}
@keyframes slideL{from{opacity:0;transform:translateX(30px)}to{opacity:1;transform:translateX(0)}}
@keyframes shimmer{0%{background-position:-200% center}100%{background-position:200% center}}
@keyframes goldPulse{0%,100%{box-shadow:0 0 0 0 rgba(201,168,76,0.4)}50%{box-shadow:0 0 0 14px rgba(201,168,76,0)}}
.stc-nav{background:var(--white);border-bottom:1px solid var(--gray-mid);padding:12px 52px;display:flex;align-items:center;justify-content:space-between;position:sticky;top:0;z-index:999;box-shadow:0 2px 16px rgba(0,0,0,0.06);animation:fadeDown .5s ease both;}
.stc-nav-brand{font-family:'Cormorant Garamond',serif;font-size:21px;font-weight:800;color:var(--black);text-decoration:none;}
.stc-nav-brand span{color:var(--gold-dk);}
.stc-nav-links{display:flex;gap:28px;}
.stc-nav-link{font-size:13px;font-weight:500;color:var(--text);text-decoration:none;position:relative;padding-bottom:2px;transition:color .2s;}
.stc-nav-link::after{content:'';position:absolute;bottom:0;left:0;width:0;height:2px;background:var(--gold);transition:width .28s ease;border-radius:2px;}
.stc-nav-link:hover{color:var(--gold-dk);}
.stc-nav-link:hover::after{width:100%;}
.stc-nav-right{display:flex;align-items:center;gap:10px;}
.stc-nav-social{display:flex;gap:8px;}
.stc-soc-icon{width:34px;height:34px;border-radius:8px;display:flex;align-items:center;justify-content:center;text-decoration:none;border:1px solid var(--gray-mid);background:var(--offwhite);font-size:16px;transition:transform .2s,background .2s;}
.stc-soc-icon:hover{transform:translateY(-2px);background:var(--gray-lt);}
.stc-wa-btn{background:linear-gradient(135deg,#25D366,#128C7E);color:white!important;font-size:12px;font-weight:700;padding:9px 18px;border-radius:var(--r-sm);text-decoration:none;display:inline-flex;align-items:center;gap:7px;transition:transform .2s,box-shadow .2s;box-shadow:0 4px 16px rgba(37,211,102,0.3);}
.stc-wa-btn:hover{transform:translateY(-2px);box-shadow:0 8px 24px rgba(37,211,102,0.45);}
.stc-hero{position:relative;min-height:91vh;overflow:hidden;display:flex;align-items:center;}
.stc-hero-bg{position:absolute;inset:0;background:linear-gradient(125deg,#0B0B0B 0%,#1a1200 40%,#0B0B0B 100%);}
.stc-hero-img{position:absolute;inset:0;background-image:url('https://images.unsplash.com/photo-1492144534655-ae79c964c9d7?w=1600&q=80');background-size:cover;background-position:center;opacity:.17;}
.stc-hero-ov{position:absolute;inset:0;background:linear-gradient(90deg,rgba(11,11,11,0.96) 42%,rgba(11,11,11,0.55) 70%,rgba(11,11,11,0.28) 100%);}
.stc-hero-stripe{position:absolute;bottom:0;left:0;right:0;height:5px;background:linear-gradient(90deg,var(--gold-dk),var(--gold),var(--gold-lt),var(--gold),var(--gold-dk));background-size:200% 100%;animation:shimmer 3s ease infinite;}
.stc-hero-car{position:absolute;right:0;top:0;bottom:0;width:47%;overflow:hidden;z-index:1;}
.stc-hero-car img{width:100%;height:100%;object-fit:cover;animation:slideL .9s .2s cubic-bezier(.22,1,.36,1) both;}
.stc-hero-car::before{content:'';position:absolute;inset:0;z-index:2;background:linear-gradient(90deg,var(--dark) 0%,transparent 30%,transparent 70%,rgba(11,11,11,.5) 100%);}
.stc-hero-cnt{position:relative;z-index:2;padding:80px 60px;max-width:620px;animation:fadeUp .7s .1s ease both;}
.stc-eyebrow-dark{display:inline-flex;align-items:center;gap:8px;background:rgba(201,168,76,.12);border:1px solid rgba(201,168,76,.3);color:var(--gold-lt);padding:6px 16px;border-radius:99px;font-size:11px;font-weight:600;letter-spacing:3px;text-transform:uppercase;margin-bottom:24px;}
.stc-hero-dot{width:7px;height:7px;background:var(--gold-lt);border-radius:50%;display:inline-block;animation:goldPulse 2s ease infinite;}
.stc-hero-title{font-family:'Cormorant Garamond',serif;font-size:clamp(42px,5.5vw,70px);font-weight:800;line-height:1.06;color:var(--white);margin:0 0 22px;}
.stc-hero-title .acc{color:var(--gold);}
.stc-hero-sub{font-size:16px;line-height:1.75;color:rgba(255,255,255,.57);margin-bottom:40px;max-width:500px;}
.stc-hero-btns{display:flex;gap:14px;flex-wrap:wrap;}
.stc-btn-gold{display:inline-flex;align-items:center;gap:10px;background:linear-gradient(135deg,var(--gold),var(--gold-lt));color:var(--black);font-weight:700;font-size:14px;padding:14px 30px;border-radius:var(--r-sm);text-decoration:none;box-shadow:var(--sh-gold);transition:transform .22s,box-shadow .22s;animation:goldPulse 2.5s ease infinite;}
.stc-btn-gold:hover{transform:translateY(-3px);box-shadow:0 14px 44px rgba(201,168,76,.55);}
.stc-btn-outline{display:inline-flex;align-items:center;gap:10px;background:transparent;color:var(--white);font-weight:600;font-size:14px;padding:14px 30px;border-radius:var(--r-sm);text-decoration:none;border:1.5px solid rgba(255,255,255,.28);transition:background .22s,border-color .22s,transform .22s;}
.stc-btn-outline:hover{background:rgba(255,255,255,.08);border-color:rgba(255,255,255,.65);transform:translateY(-2px);}
.stc-stats{display:flex;gap:40px;margin-top:52px;padding-top:38px;border-top:1px solid rgba(255,255,255,.1);}
.stc-stat-n{font-family:'Cormorant Garamond',serif;font-size:34px;font-weight:800;color:var(--gold-lt);}
.stc-stat-l{font-size:12px;color:rgba(255,255,255,.42);margin-top:2px;}
.stc-sec{padding:80px 60px;}
.stc-sec-white{background:var(--white);}
.stc-sec-cream{background:var(--offwhite);}
.stc-sec-dark{background:var(--dark);}
.stc-sec-black{background:var(--black);}
.stc-eyebrow{display:inline-flex;align-items:center;gap:8px;font-size:11px;font-weight:700;letter-spacing:3.5px;text-transform:uppercase;color:var(--gold-dk);margin-bottom:14px;}
.stc-eyebrow::before{content:'';display:inline-block;width:26px;height:2px;background:var(--gold);border-radius:2px;}
.stc-eyebrow-lt{color:var(--gold-lt);}
.stc-eyebrow-lt::before{background:var(--gold-lt);}
.stc-h2{font-family:'Cormorant Garamond',serif;font-size:clamp(30px,3.2vw,48px);font-weight:800;color:var(--black);line-height:1.12;margin:0 0 16px;}
.stc-h2-w{color:var(--white);}
.stc-sub{font-size:15px;color:var(--muted);line-height:1.75;max-width:540px;}
.stc-sub-w{color:rgba(255,255,255,.5);}
.stc-svc-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:22px;margin-top:48px;}
.stc-svc-card{background:var(--white);border:1px solid var(--gray-mid);border-radius:var(--r);padding:32px 28px;position:relative;overflow:hidden;box-shadow:var(--sh-card);transition:transform .28s cubic-bezier(.22,1,.36,1),box-shadow .28s,border-color .22s;animation:fadeUp .5s ease both;cursor:default;}
.stc-svc-card:hover{transform:translateY(-7px);box-shadow:var(--sh-lg);border-color:var(--gold);}
.stc-svc-card::after{content:'';position:absolute;top:0;left:0;right:0;height:3px;background:linear-gradient(90deg,var(--gold-dk),var(--gold-lt));transform:scaleX(0);transform-origin:left;transition:transform .35s cubic-bezier(.22,1,.36,1);}
.stc-svc-card:hover::after{transform:scaleX(1);}
.stc-svc-icon{width:56px;height:56px;border-radius:15px;margin-bottom:20px;background:linear-gradient(135deg,#fdf4d0,#f0e070);display:flex;align-items:center;justify-content:center;font-size:24px;transition:transform .3s ease;}
.stc-svc-card:hover .stc-svc-icon{transform:scale(1.1) rotate(-6deg);}
.stc-svc-name{font-family:'Cormorant Garamond',serif;font-size:19px;font-weight:800;color:var(--black);margin:0 0 10px;}
.stc-svc-desc{font-size:13.5px;color:var(--muted);line-height:1.65;}
.stc-car-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:24px;margin-top:52px;}
.stc-car-card{background:var(--white);border-radius:var(--r);overflow:hidden;box-shadow:var(--sh-card);border:1px solid var(--gray-mid);transition:transform .32s cubic-bezier(.22,1,.36,1),box-shadow .32s;animation:scaleIn .5s ease both;}
.stc-car-card:hover{transform:translateY(-10px) scale(1.01);box-shadow:var(--sh-lg);}
.stc-car-img{position:relative;height:200px;overflow:hidden;}
.stc-car-img img{width:100%;height:100%;object-fit:cover;transition:transform .5s cubic-bezier(.22,1,.36,1);display:block;}
.stc-car-card:hover .stc-car-img img{transform:scale(1.07);}
.stc-car-badge{position:absolute;top:14px;left:14px;background:var(--black);color:var(--gold-lt);font-size:10px;font-weight:700;letter-spacing:1.5px;text-transform:uppercase;padding:5px 12px;border-radius:8px;}
.stc-car-badge.oferta{background:linear-gradient(135deg,var(--gold-dk),var(--gold));color:var(--black);}
.stc-car-ov{position:absolute;inset:0;background:linear-gradient(to top,rgba(11,11,11,.55) 0%,transparent 50%);opacity:0;transition:opacity .3s;}
.stc-car-card:hover .stc-car-ov{opacity:1;}
.stc-car-body{padding:22px;}
.stc-car-name{font-family:'Cormorant Garamond',serif;font-size:19px;font-weight:800;color:var(--black);margin:0 0 5px;}
.stc-car-spec{font-size:12px;color:var(--muted);margin-bottom:12px;}
.stc-car-row{display:flex;align-items:center;justify-content:space-between;}
.stc-car-price{font-size:20px;font-weight:700;color:var(--gold-dk);font-family:'Cormorant Garamond',serif;}
.stc-car-link{display:inline-flex;align-items:center;gap:6px;background:var(--black);color:var(--gold-lt);font-size:12px;font-weight:700;padding:9px 16px;border-radius:9px;text-decoration:none;transition:background .2s,transform .18s,box-shadow .18s;}
.stc-car-link:hover{background:var(--dark2,#1E1E1E);transform:translateY(-2px);box-shadow:0 6px 20px rgba(0,0,0,.2);}
.stc-steps{display:grid;grid-template-columns:repeat(4,1fr);gap:0;margin-top:56px;position:relative;}
.stc-steps::before{content:'';position:absolute;top:32px;left:12%;right:12%;height:2px;background:linear-gradient(90deg,var(--gold-dk),var(--gold-lt),var(--gold-dk));background-size:200% 100%;animation:shimmer 3s ease infinite;z-index:0;}
.stc-step{text-align:center;padding:0 16px;position:relative;z-index:1;}
.stc-step-circle{width:64px;height:64px;border-radius:50%;margin:0 auto 22px;background:linear-gradient(135deg,var(--gold-dk),var(--gold-lt));display:flex;align-items:center;justify-content:center;font-size:26px;box-shadow:var(--sh-gold);transition:transform .25s ease;border:3px solid var(--dark);}
.stc-step:hover .stc-step-circle{transform:scale(1.12);}
.stc-step-num{font-family:'Cormorant Garamond',serif;font-size:13px;font-weight:800;color:var(--gold-lt);letter-spacing:1px;text-transform:uppercase;margin-bottom:8px;}
.stc-step-title{font-family:'Cormorant Garamond',serif;font-size:17px;font-weight:800;color:var(--white);margin:0 0 8px;}
.stc-step-desc{font-size:13px;color:rgba(255,255,255,.48);line-height:1.65;}
.stc-sim-wrap{background:var(--white);border-radius:22px;padding:44px 48px;box-shadow:var(--sh-lg);border:1px solid var(--gray-mid);animation:scaleIn .5s ease both;}
.stc-sim-res{background:linear-gradient(135deg,var(--black) 0%,#1E1E1E 100%);border-radius:var(--r);padding:30px 36px;margin-top:26px;border:1px solid rgba(201,168,76,.35);text-align:center;animation:scaleIn .4s ease both;position:relative;overflow:hidden;}
.stc-sim-res::before{content:'';position:absolute;inset:0;background:radial-gradient(ellipse at center,rgba(201,168,76,.1) 0%,transparent 65%);}
.stc-sim-label{font-size:11px;color:rgba(255,255,255,.4);letter-spacing:3px;text-transform:uppercase;margin-bottom:10px;}
.stc-sim-value{font-family:'Cormorant Garamond',serif;font-size:52px;font-weight:800;color:var(--gold);line-height:1;position:relative;}
.stc-sim-sub{font-size:12px;color:rgba(255,255,255,.35);margin-top:8px;}
.stc-sim-tag{display:inline-block;margin-top:14px;padding:5px 14px;border-radius:99px;font-size:12px;font-weight:600;}
.stc-sim-ok{background:rgba(37,211,102,.12);color:#25D366;border:1px solid rgba(37,211,102,.25);}
.stc-sim-warn{background:rgba(255,165,0,.12);color:#FFA500;border:1px solid rgba(255,165,0,.25);}
.stc-test-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:22px;margin-top:48px;}
.stc-test-card{background:var(--white);border:1px solid var(--gray-mid);border-radius:var(--r);padding:28px 24px;box-shadow:var(--sh-card);animation:fadeUp .5s ease both;transition:transform .25s,box-shadow .25s;}
.stc-test-card:hover{transform:translateY(-5px);box-shadow:var(--sh-lg);}
.stc-test-stars{color:var(--gold);font-size:16px;letter-spacing:2px;margin-bottom:14px;}
.stc-test-text{font-size:14px;color:var(--text);line-height:1.75;margin-bottom:18px;font-style:italic;opacity:.85;}
.stc-test-author{display:flex;align-items:center;gap:12px;}
.stc-test-av{width:42px;height:42px;border-radius:50%;flex-shrink:0;background:linear-gradient(135deg,var(--gold-dk),var(--gold-lt));display:flex;align-items:center;justify-content:center;font-family:'Cormorant Garamond',serif;font-size:17px;font-weight:800;color:var(--black);}
.stc-test-name{font-size:14px;font-weight:700;color:var(--black);}
.stc-test-city{font-size:12px;color:var(--muted);margin-top:2px;}
.stc-contact-grid{display:grid;grid-template-columns:1fr 1fr;gap:48px;margin-top:52px;align-items:start;}
.stc-contact-item{display:flex;align-items:center;gap:16px;padding:18px 22px;background:rgba(201,168,76,.06);border:1px solid rgba(201,168,76,.2);border-radius:var(--r-sm);margin-bottom:14px;transition:background .2s,transform .2s;text-decoration:none;}
.stc-contact-item:hover{background:rgba(201,168,76,.12);transform:translateX(4px);}
.stc-contact-icon{font-size:22px;width:42px;text-align:center;flex-shrink:0;}
.stc-contact-lbl{font-size:11px;color:rgba(255,255,255,.4);text-transform:uppercase;letter-spacing:1.5px;margin-bottom:3px;}
.stc-contact-val{font-size:15px;font-weight:600;color:var(--white);}
.stc-social-row{display:flex;gap:14px;margin-top:24px;}
.stc-soc-btn{flex:1;display:flex;align-items:center;justify-content:center;gap:10px;padding:13px;border-radius:var(--r-sm);font-size:13px;font-weight:700;text-decoration:none;transition:transform .2s,box-shadow .2s;}
.stc-soc-wa{background:#25D366;color:var(--white);box-shadow:0 4px 16px rgba(37,211,102,.35);}
.stc-soc-wa:hover{transform:translateY(-3px);box-shadow:0 10px 28px rgba(37,211,102,.5);}
.stc-soc-fb{background:#1877F2;color:var(--white);box-shadow:0 4px 16px rgba(24,119,242,.35);}
.stc-soc-fb:hover{transform:translateY(-3px);box-shadow:0 10px 28px rgba(24,119,242,.5);}
.stc-soc-ig{background:linear-gradient(135deg,#833ab4,#fd1d1d,#fcb045);color:var(--white);box-shadow:0 4px 16px rgba(131,58,180,.35);}
.stc-soc-ig:hover{transform:translateY(-3px);box-shadow:0 10px 28px rgba(131,58,180,.5);}
.stc-cta-box{background:rgba(201,168,76,.07);border:1px solid rgba(201,168,76,.25);border-radius:var(--r);padding:36px;}
.stc-cta-box-title{font-family:'Cormorant Garamond',serif;font-size:28px;font-weight:800;color:var(--white);margin-bottom:10px;line-height:1.2;}
.stc-cta-box-sub{font-size:14px;color:rgba(255,255,255,.5);margin-bottom:24px;line-height:1.65;}
.stc-cta-banner{background:linear-gradient(135deg,var(--black) 0%,#1a1200 50%,var(--dark) 100%);padding:88px 64px;text-align:center;position:relative;overflow:hidden;}
.stc-cta-banner::before{content:'';position:absolute;inset:0;background:radial-gradient(ellipse at center,rgba(201,168,76,.14) 0%,transparent 65%);}
.stc-cta-title{font-family:'Cormorant Garamond',serif;font-size:clamp(30px,4vw,54px);font-weight:800;color:var(--white);margin-bottom:14px;position:relative;z-index:1;}
.stc-cta-title span{color:var(--gold-lt);}
.stc-cta-sub{font-size:15px;color:rgba(255,255,255,.5);margin-bottom:38px;position:relative;z-index:1;}
.stc-cta-btns{display:flex;gap:14px;justify-content:center;flex-wrap:wrap;position:relative;z-index:1;}
.stc-footer{background:var(--black);padding:48px 60px 28px;border-top:1px solid rgba(201,168,76,.16);}
.stc-footer-grid{display:grid;grid-template-columns:2fr 1fr 1fr 1fr;gap:48px;margin-bottom:40px;}
.stc-footer-brand{font-family:'Cormorant Garamond',serif;font-size:20px;font-weight:800;color:var(--white);margin-bottom:8px;}
.stc-footer-brand span{color:var(--gold);}
.stc-footer-tagline{font-size:13px;color:rgba(255,255,255,.35);line-height:1.65;max-width:240px;margin-bottom:20px;}
.stc-footer-soc{display:flex;gap:10px;}
.stc-footer-soc-icon{width:34px;height:34px;border-radius:8px;display:flex;align-items:center;justify-content:center;font-size:15px;text-decoration:none;background:rgba(255,255,255,.07);border:1px solid rgba(255,255,255,.1);transition:background .2s,transform .18s;}
.stc-footer-soc-icon:hover{background:rgba(201,168,76,.2);transform:translateY(-2px);}
.stc-footer-col-title{font-size:12px;font-weight:700;color:var(--white);letter-spacing:1.5px;text-transform:uppercase;margin-bottom:16px;}
.stc-footer-link{display:block;font-size:13px;color:rgba(255,255,255,.45);text-decoration:none;margin-bottom:9px;transition:color .2s;}
.stc-footer-link:hover{color:var(--gold-lt);}
.stc-footer-bottom{border-top:1px solid rgba(255,255,255,.07);padding-top:22px;display:flex;justify-content:space-between;align-items:center;font-size:12px;color:rgba(255,255,255,.25);}
[data-testid="stNumberInput"] input{border-radius:var(--r-sm)!important;border:1.5px solid var(--gray-mid)!important;font-family:'Outfit',sans-serif!important;font-size:15px!important;padding:10px 14px!important;background:var(--offwhite)!important;transition:border-color .22s,box-shadow .22s!important;}
[data-testid="stNumberInput"] input:focus{border-color:var(--gold-dk)!important;box-shadow:0 0 0 4px rgba(201,168,76,.14)!important;outline:none!important;}
[data-testid="stNumberInput"] label,[data-testid="stSlider"] label{font-family:'Outfit',sans-serif!important;font-weight:600!important;font-size:13px!important;color:var(--text)!important;}
.stButton>button{background:linear-gradient(135deg,var(--gold-dk),var(--gold-lt))!important;color:var(--black)!important;font-family:'Outfit',sans-serif!important;font-weight:700!important;border:none!important;border-radius:var(--r-sm)!important;padding:13px 32px!important;font-size:14px!important;box-shadow:var(--sh-gold)!important;transition:transform .22s,box-shadow .22s!important;width:100%!important;}
.stButton>button:hover{transform:translateY(-3px)!important;box-shadow:0 14px 40px rgba(201,168,76,.52)!important;}
[data-testid="stAlert"]{border-radius:var(--r)!important;}
.stc-svc-grid>*:nth-child(1){animation-delay:.05s}.stc-svc-grid>*:nth-child(2){animation-delay:.12s}.stc-svc-grid>*:nth-child(3){animation-delay:.19s}.stc-svc-grid>*:nth-child(4){animation-delay:.26s}.stc-svc-grid>*:nth-child(5){animation-delay:.33s}.stc-svc-grid>*:nth-child(6){animation-delay:.4s}
.stc-car-grid>*:nth-child(1){animation-delay:.06s}.stc-car-grid>*:nth-child(2){animation-delay:.14s}.stc-car-grid>*:nth-child(3){animation-delay:.22s}.stc-car-grid>*:nth-child(4){animation-delay:.3s}.stc-car-grid>*:nth-child(5){animation-delay:.38s}.stc-car-grid>*:nth-child(6){animation-delay:.46s}
.stc-test-grid>*:nth-child(1){animation-delay:.05s}.stc-test-grid>*:nth-child(2){animation-delay:.15s}.stc-test-grid>*:nth-child(3){animation-delay:.25s}
</style>
"""
st.markdown(CSS, unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
# NAVBAR
# ══════════════════════════════════════════════════════════════════════════════
logo_html = ('<img src="assets/logo.webp" alt="Somos Tu Crédito" style="height:44px;width:auto;">'
             if os.path.exists("assets/logo.webp")
             else '<span class="stc-nav-brand">Somos Tu <span>Crédito</span></span>')

H(f'<nav class="stc-nav"><div>{logo_html}</div><div class="stc-nav-links"><a class="stc-nav-link" href="#servicios">Servicios</a><a class="stc-nav-link" href="#vehiculos">Vehículos</a><a class="stc-nav-link" href="#proceso">Proceso</a><a class="stc-nav-link" href="#simulador">Simulador</a><a class="stc-nav-link" href="#contacto">Contacto</a></div><div class="stc-nav-right"><div class="stc-nav-social"><a class="stc-soc-icon" href="{FB_URL}" target="_blank" title="Facebook">📘</a><a class="stc-soc-icon" href="{IG_URL}" target="_blank" title="Instagram">📸</a></div><a class="stc-wa-btn" href="{WA_URL}" target="_blank">💬 {PHONE}</a></div></nav>')

# ══════════════════════════════════════════════════════════════════════════════
# HERO
# ══════════════════════════════════════════════════════════════════════════════
H(f'''<section class="stc-hero"><div class="stc-hero-bg"></div><div class="stc-hero-img"></div><div class="stc-hero-ov"></div><div class="stc-hero-stripe"></div><div class="stc-hero-car"><img src="https://images.unsplash.com/photo-1544636331-e26879cd4d9b?w=1000&q=85" alt="Vehículo premium" loading="eager"></div><div class="stc-hero-cnt"><div class="stc-eyebrow-dark"><span class="stc-hero-dot"></span> Tocancipá &middot; Cundinamarca</div><h1 class="stc-hero-title">Tu vehículo ideal,<br><span class="acc">a tu alcance hoy</span></h1><p class="stc-hero-sub">Gestionamos tu crédito vehicular con más de 15 bancos aliados. Nuevos, usados, SUV, motos — te acompañamos en cada paso hasta la entrega.</p><div class="stc-hero-btns"><a class="stc-btn-gold" href="{WA_URL}" target="_blank">💬 Asesoría gratuita</a><a class="stc-btn-outline" href="#vehiculos">Ver vehículos →</a></div><div class="stc-stats"><div><div class="stc-stat-n">+2.500</div><div class="stc-stat-l">Clientes satisfechos</div></div><div><div class="stc-stat-n">15+</div><div class="stc-stat-l">Bancos aliados</div></div><div><div class="stc-stat-n">98%</div><div class="stc-stat-l">Tasa de aprobación</div></div></div></div></section>''')

# ══════════════════════════════════════════════════════════════════════════════
# SERVICIOS
# ══════════════════════════════════════════════════════════════════════════════
H('''<section class="stc-sec stc-sec-white" id="servicios"><div class="stc-eyebrow">Qué ofrecemos</div><h2 class="stc-h2">Todo lo que necesitas<br>en un solo lugar</h2><p class="stc-sub">Desde el primer contacto hasta la entrega de llaves — somos tu aliado en movilidad.</p><div class="stc-svc-grid"><div class="stc-svc-card"><div class="stc-svc-icon">🚗</div><h3 class="stc-svc-name">Vehículos Nuevos</h3><p class="stc-svc-desc">Accede a las mejores marcas del mercado con precios competitivos, garantía de fábrica y financiación aprobada.</p></div><div class="stc-svc-card"><div class="stc-svc-icon">🔄</div><h3 class="stc-svc-name">Vehículos Usados</h3><p class="stc-svc-desc">Selección curada de seminuevos revisados y certificados. Calidad garantizada a precios muy accesibles.</p></div><div class="stc-svc-card"><div class="stc-svc-icon">🏦</div><h3 class="stc-svc-name">Gestión de Crédito</h3><p class="stc-svc-desc">Negociamos por ti con más de 15 entidades financieras para asegurarte la mejor tasa y el mejor plazo.</p></div><div class="stc-svc-card"><div class="stc-svc-icon">📊</div><h3 class="stc-svc-name">Análisis de Perfil</h3><p class="stc-svc-desc">Evaluamos tu situación financiera sin costo y te orientamos hacia la mejor opción disponible.</p></div><div class="stc-svc-card"><div class="stc-svc-icon">🏍️</div><h3 class="stc-svc-name">Motos &amp; Más</h3><p class="stc-svc-desc">También financiamos motos, camperos y vehículos de carga. Sin importar qué ruedas buscas.</p></div><div class="stc-svc-card"><div class="stc-svc-icon">🛡️</div><h3 class="stc-svc-name">Postventa &amp; SOAT</h3><p class="stc-svc-desc">Asesoramos en seguros, SOAT, traspaso y trámites para que tu vehículo esté siempre al día.</p></div></div></section>''')

# ══════════════════════════════════════════════════════════════════════════════
# GALERÍA DE VEHÍCULOS
# ══════════════════════════════════════════════════════════════════════════════
cards_html = ""
for c in CARS:
    msg_enc = c["msg"].replace(" ", "%20")
    cards_html += (f'<div class="stc-car-card">'
                   f'<div class="stc-car-img">'
                   f'<img src="{c["img"]}" alt="{c["name"]}" loading="lazy">'
                   f'<div class="stc-car-ov"></div>'
                   f'<span class="stc-car-badge {c["badge_class"]}">{c["badge"]}</span>'
                   f'</div>'
                   f'<div class="stc-car-body">'
                   f'<p class="stc-car-name">{c["name"]}</p>'
                   f'<p class="stc-car-spec">{c["specs"]}</p>'
                   f'<div class="stc-car-row">'
                   f'<span class="stc-car-price">{c["price"]}</span>'
                   f'<a class="stc-car-link" href="{WA_URL}?text={msg_enc}" target="_blank">💬 Me interesa</a>'
                   f'</div></div></div>')

H(f'<section class="stc-sec stc-sec-cream" id="vehiculos"><div class="stc-eyebrow">Disponibles ahora</div><h2 class="stc-h2">Vehículos destacados</h2><p class="stc-sub">Encuentra el que se adapta a tu estilo de vida. Cada vehículo con financiación lista.</p><div class="stc-car-grid">{cards_html}</div></section>')

# ══════════════════════════════════════════════════════════════════════════════
# PROCESO
# ══════════════════════════════════════════════════════════════════════════════
H('''<section class="stc-sec stc-sec-dark" id="proceso"><div class="stc-eyebrow stc-eyebrow-lt">¿Cómo funciona?</div><h2 class="stc-h2 stc-h2-w">4 pasos para estrenar<br>tu vehículo</h2><div class="stc-steps"><div class="stc-step"><div class="stc-step-circle">💬</div><p class="stc-step-num">Paso 01</p><p class="stc-step-title">Contáctanos</p><p class="stc-step-desc">Escríbenos por WhatsApp o redes sociales. Respondemos en minutos.</p></div><div class="stc-step"><div class="stc-step-circle">📋</div><p class="stc-step-num">Paso 02</p><p class="stc-step-title">Analizamos tu perfil</p><p class="stc-step-desc">Evaluamos tu situación financiera sin costo para encontrar la mejor opción.</p></div><div class="stc-step"><div class="stc-step-circle">✅</div><p class="stc-step-num">Paso 03</p><p class="stc-step-title">Aprobación rápida</p><p class="stc-step-desc">Gestionamos tu crédito con todos nuestros bancos aliados simultáneamente.</p></div><div class="stc-step"><div class="stc-step-circle">🔑</div><p class="stc-step-num">Paso 04</p><p class="stc-step-title">¡Entrega de llaves!</p><p class="stc-step-desc">Recibe tu vehículo en tiempo récord. ¡Así de fácil y seguro!</p></div></div></section>''')

# ══════════════════════════════════════════════════════════════════════════════
# SIMULADOR — header
# ══════════════════════════════════════════════════════════════════════════════
H('''<section class="stc-sec stc-sec-cream" id="simulador"><div style="text-align:center;margin-bottom:48px"><div class="stc-eyebrow" style="justify-content:center;display:flex">Herramienta</div><h2 class="stc-h2" style="text-align:center">Simula tu cuota mensual</h2><p class="stc-sub" style="margin:0 auto;text-align:center">Calcula en segundos cuánto pagarías. Un asesor confirmará la oferta exacta.</p></div></section>''')

# Widgets Streamlit del simulador
_, col_s, _ = st.columns([1, 2.2, 1])
with col_s:
    st.markdown('<div class="stc-sim-wrap">', unsafe_allow_html=True)
    ingreso = st.number_input("💼  Ingreso mensual (COP)", min_value=0, step=100_000, format="%d", help="Salario o ingresos comprobables al mes")
    valor   = st.number_input("🚗  Valor del vehículo (COP)", min_value=0, step=1_000_000, format="%d", help="Precio del vehículo que te interesa")
    plazo   = st.select_slider("📅  Plazo del crédito", options=[12,24,36,48,60,72], value=48, format_func=lambda x: f"{x} meses")
    calcular = st.button("Calcular cuota estimada")

    if calcular and valor > 0:
        tasa = 0.015
        cuota = valor * (tasa * (1 + tasa)**plazo) / ((1 + tasa)**plazo - 1)
        if ingreso > 0 and cuota <= ingreso * 0.30:
            tag = '<span class="stc-sim-tag stc-sim-ok">✅ Perfil viable para este crédito</span>'
        elif ingreso > 0:
            tag = '<span class="stc-sim-tag stc-sim-warn">⚠️ Consulta con un asesor personalizado</span>'
        else:
            tag = ""
        H(f'<div class="stc-sim-res"><div class="stc-sim-label">Cuota mensual estimada</div><div class="stc-sim-value">${cuota:,.0f}</div><div class="stc-sim-sub">Plazo {plazo} meses &middot; Tasa ref. 1.5% M.V.</div>{tag}</div><p style="font-size:12px;color:#aaa;text-align:center;margin-top:16px">* Simulación orientativa. La tasa final depende del banco y perfil crediticio.</p>')
    elif calcular:
        st.warning("Por favor ingresa el valor del vehículo.")
    st.markdown('</div>', unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
# TESTIMONIOS
# ══════════════════════════════════════════════════════════════════════════════
H('''<section class="stc-sec stc-sec-white"><div class="stc-eyebrow">Clientes reales</div><h2 class="stc-h2">Lo que dicen quienes<br>ya estrenaron su vehículo</h2><div class="stc-test-grid"><div class="stc-test-card"><div class="stc-test-stars">&#9733;&#9733;&#9733;&#9733;&#9733;</div><p class="stc-test-text">"Pensé que con mis ingresos no calificaba. El equipo de Somos Tu Crédito encontró la solución y hoy manejo mi SUV nuevo. ¡Los recomiendo al 100%!"</p><div class="stc-test-author"><div class="stc-test-av">C</div><div><div class="stc-test-name">Carlos Mendoza</div><div class="stc-test-city">Bogotá, D.C.</div></div></div></div><div class="stc-test-card"><div class="stc-test-stars">&#9733;&#9733;&#9733;&#9733;&#9733;</div><p class="stc-test-text">"Proceso súper rápido, transparente y sin letra pequeña. Me aprobaron en menos de 3 días hábiles. Excelente atención de principio a fin."</p><div class="stc-test-author"><div class="stc-test-av">A</div><div><div class="stc-test-name">Andrea Vargas</div><div class="stc-test-city">Medellín, Ant.</div></div></div></div><div class="stc-test-card"><div class="stc-test-stars">&#9733;&#9733;&#9733;&#9733;&#9733;</div><p class="stc-test-text">"Llevé un historial crediticio complicado y aun así encontraron la manera. Profesionales, honestos y muy comprometidos con el cliente."</p><div class="stc-test-author"><div class="stc-test-av">R</div><div><div class="stc-test-name">Ricardo Torres</div><div class="stc-test-city">Cali, Valle</div></div></div></div></div></section>''')

# ══════════════════════════════════════════════════════════════════════════════
# CONTACTO
# ══════════════════════════════════════════════════════════════════════════════
H(f'''<section class="stc-sec stc-sec-black" id="contacto"><div class="stc-eyebrow stc-eyebrow-lt">Escríbenos</div><h2 class="stc-h2 stc-h2-w">Habla con un asesor ahora</h2><div class="stc-contact-grid"><div><a class="stc-contact-item" href="tel:+573134138598"><div class="stc-contact-icon">📞</div><div><div class="stc-contact-lbl">Teléfono corporativo</div><div class="stc-contact-val">{PHONE}</div></div></a><a class="stc-contact-item" href="{WA_URL}" target="_blank"><div class="stc-contact-icon">💬</div><div><div class="stc-contact-lbl">WhatsApp</div><div class="stc-contact-val">{PHONE}</div></div></a><a class="stc-contact-item" href="{FB_URL}" target="_blank"><div class="stc-contact-icon">📘</div><div><div class="stc-contact-lbl">Facebook</div><div class="stc-contact-val">Somos tu Crédito | Tocancipá</div></div></a><a class="stc-contact-item" href="{IG_URL}" target="_blank"><div class="stc-contact-icon">📸</div><div><div class="stc-contact-lbl">Instagram</div><div class="stc-contact-val">@somostucredito_</div></div></a><div class="stc-social-row"><a class="stc-soc-btn stc-soc-wa" href="{WA_URL}" target="_blank">💬 WhatsApp</a><a class="stc-soc-btn stc-soc-fb" href="{FB_URL}" target="_blank">📘 Facebook</a><a class="stc-soc-btn stc-soc-ig" href="{IG_URL}" target="_blank">📸 Instagram</a></div></div><div class="stc-cta-box"><p class="stc-cta-box-title">¿Listo para estrenar<br>tu vehículo?</p><p class="stc-cta-box-sub">Déjanos tus datos por WhatsApp y un asesor te contactará en menos de 15 minutos para guiarte en todo el proceso de financiamiento.</p><a class="stc-btn-gold" href="{WA_URL}?text=Hola%2C%20quiero%20información%20sobre%20crédito%20vehicular" target="_blank" style="display:inline-flex">💬 Iniciar asesoría gratis →</a><div style="margin-top:20px;padding-top:18px;border-top:1px solid rgba(201,168,76,0.2)"><p style="font-size:12px;color:rgba(255,255,255,0.3);margin:0">Sin costo de estudio &middot; Respuesta en 24 h &middot; Ubicados en Tocancipá, Cundinamarca</p></div></div></div></section>''')

# ══════════════════════════════════════════════════════════════════════════════
# CTA BANNER
# ══════════════════════════════════════════════════════════════════════════════
H(f'<section class="stc-cta-banner"><h2 class="stc-cta-title">¿Todavía pensándolo?<br><span>Tu vehículo te está esperando.</span></h2><p class="stc-cta-sub">Asesoría sin costo &middot; Sin codeudor en muchos casos &middot; Aprobación express</p><div class="stc-cta-btns"><a class="stc-btn-gold" href="{WA_URL}" target="_blank">💬 Escríbenos ahora — Gratis</a><a class="stc-btn-outline" href="tel:+573134138598">📞 {PHONE}</a></div></section>')

# ══════════════════════════════════════════════════════════════════════════════
# FOOTER
# ══════════════════════════════════════════════════════════════════════════════
H(f'<footer class="stc-footer"><div class="stc-footer-grid"><div><div class="stc-footer-brand">Somos Tu <span>Crédito</span></div><p class="stc-footer-tagline">Tu aliado en movilidad y financiamiento vehicular. Tocancipá, Cundinamarca.</p><div class="stc-footer-soc"><a class="stc-footer-soc-icon" href="{WA_URL}" target="_blank">💬</a><a class="stc-footer-soc-icon" href="{FB_URL}" target="_blank">📘</a><a class="stc-footer-soc-icon" href="{IG_URL}" target="_blank">📸</a><a class="stc-footer-soc-icon" href="tel:+573134138598">📞</a></div></div><div><p class="stc-footer-col-title">Servicios</p><a class="stc-footer-link" href="#vehiculos">Vehículos Nuevos</a><a class="stc-footer-link" href="#vehiculos">Vehículos Usados</a><a class="stc-footer-link" href="#servicios">Gestión de Crédito</a><a class="stc-footer-link" href="#servicios">Motos &amp; Más</a></div><div><p class="stc-footer-col-title">Empresa</p><a class="stc-footer-link" href="#proceso">¿Cómo funciona?</a><a class="stc-footer-link" href="#simulador">Simulador</a><a class="stc-footer-link" href="#contacto">Contacto</a></div><div><p class="stc-footer-col-title">Contacto</p><a class="stc-footer-link" href="tel:+573134138598">{PHONE}</a><a class="stc-footer-link" href="{WA_URL}" target="_blank">WhatsApp</a><a class="stc-footer-link" href="{FB_URL}" target="_blank">Somos tu Crédito | Tocancipá</a><a class="stc-footer-link" href="{IG_URL}" target="_blank">@somostucredito_</a></div></div><div class="stc-footer-bottom"><span>&copy; 2026 Somos Tu Crédito &middot; Tocancipá, Cundinamarca &middot; Colombia</span><span>Diseñado con ❤️ para Colombia</span></div></footer>')

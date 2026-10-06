#!/usr/bin/env python3
"""Build a portable, dependency-free bilingual GitHub Pages website."""
import html
import hashlib
import json
import os
from pathlib import Path
import shutil
from urllib.parse import quote
from content import PRIVACY, FAQ

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "site"
C = json.loads((ROOT / "config.json").read_text())
BASE = C["site_url"].rstrip("/")
EMAIL = C["support_email"]
REPO = C["repository"]
DATE = C["policy_date"]

ICONS = {
"arrow": '<path d="M5 12h14M13 6l6 6-6 6"/>',
"leaf": '<path d="M20 4c0 11-4 16-10 16a6 6 0 0 1-6-6C4 8 9 4 20 4Z"/><path d="m5 19 9-9"/>',
"steps": '<path d="M7 18v-4h5V9h5V4h4M3 18h4M12 9v5M17 4v5"/>',
"chart": '<path d="M4 4v16h16M7 14l4-4 4 2 5-7"/>',
"shield": '<path d="m12 3 8 3v6c0 5-8 9-8 9s-8-4-8-9V6l8-3Z"/><path d="m8 12 3 3 5-6"/>',
"mail": '<rect x="3" y="5" width="18" height="14" rx="3"/><path d="m3 7 9 6 9-6"/>',
"help": '<circle cx="12" cy="12" r="9"/><path d="M9 9a3 3 0 1 1 4 3c-1 .5-1 1-1 2M12 17h.01"/>',
"file": '<path d="M14 3H6a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V9l-6-6Z"/><path d="M14 3v6h6M8 13h8M8 17h5"/>',
"search": '<circle cx="10.5" cy="10.5" r="6.5"/><path d="m16 16 5 5"/>',
"copy": '<rect x="8" y="8" width="12" height="13" rx="2"/><path d="M16 8V5a2 2 0 0 0-2-2H5a2 2 0 0 0-2 2v9a2 2 0 0 0 2 2h3"/>',
"menu": '<path d="M5 8h14M5 16h14"/>',
"check": '<path d="m5 12 4 4L19 6"/>',
"heart": '<path d="M20 5a5 5 0 0 0-8 2 5 5 0 0 0-8-2c-4 4 1 10 8 15 7-5 12-11 8-15Z"/>'
}

def icon(name):
    return f'<svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{ICONS[name]}</svg>'

def e(value):
    return html.escape(str(value), quote=True)

def path(lang, page="home"):
    return ("en/" if lang == "en" else "") + ("" if page == "home" else page + "/")

def rel(current, target):
    result = os.path.relpath(target or ".", current or ".").replace(os.sep, "/")
    if target.endswith("/") or not target:
        return (result if result != "." else ".") + "/"
    return result

def asset(current, name):
    url = rel(current, "assets/" + name)
    if name.endswith((".css", ".js")) or name in {"mark.svg", "touch-icon.png", "favicon-32.png", "social-card.jpg"}:
        url += "?v=" + hashlib.sha256((ROOT / "assets" / name).read_bytes()).hexdigest()[:10]
    return url

def t(lang, zh, en):
    return en if lang == "en" else zh

def link(current, lang, page):
    return rel(current, path(lang, page))

def btn(label, url, variant=""):
    return f'<a class="btn {variant}" href="{e(url)}">{label}{icon("arrow")}</a>'

def mail_url(subject, body=None):
    url = "mailto:" + EMAIL + "?subject=" + quote(subject)
    if body:
        url += "&body=" + quote(body)
    return url

def brand(current, lang):
    name = t(lang, "轻一点", "Lighter")
    return f'<a class="brand" href="{link(current,lang,"home")}" aria-label="{t(lang,"轻一点首页","Lighter home")}"><img src="{asset(current,"mark.svg")}" width="42" height="42" alt=""><span translate="no"><span class="brand-name">{name}</span><span class="brand-caption">{t(lang,"LIGHTER · 轻一点","SMALL STEPS.")}</span></span></a>'

def header(current, lang, page):
    other = "en" if lang == "zh" else "zh"
    nav = "".join(f'<a href="{link(current,lang,key)}"'+(' aria-current="page"' if key == page else '')+f'>{t(lang,zh,en)}</a>' for key,zh,en in [("home","认识轻一点","The app"),("support","技术支持","Support"),("privacy","隐私政策","Privacy")])
    cta = C.get("app_store_url") or (link(current,lang,"home") + "#availability")
    return f'''<a class="skip" href="#main">{t(lang,"跳转到主要内容","Skip to content")}</a>
<header class="header" id="top"><div class="wrap nav">{brand(current,lang)}
<nav class="nav-links" id="primary-navigation" data-nav aria-label="{t(lang,"主导航","Main navigation")}">{nav}</nav>
<div class="nav-end"><a class="locale" href="{rel(current,path(other,page))}" lang="{t(lang,"en","zh-Hans")}" hreflang="{t(lang,"en","zh-Hans")}" aria-label="{t(lang,"Switch to English","切换为简体中文")}">{t(lang,"EN ↗","中文 ↗")}</a><a class="nav-cta" href="{e(cta)}">{t(lang,"下载 App" if C.get("app_store_url") else "即将上线","Get the app" if C.get("app_store_url") else "Coming soon")}<span class="arrow" aria-hidden="true">↗</span></a><button class="menu-toggle" type="button" data-menu aria-controls="primary-navigation" aria-expanded="false" aria-label="{t(lang,"打开导航","Open navigation")}">{icon("menu")}</button></div></div></header>'''

def footer(current, lang):
    return f'''<footer class="footer"><div class="wrap"><div class="footer-main"><div>{brand(current,lang)}<p class="footer-desc">{t(lang,"把改变，放回舒服的日常。","Make room for a gentler everyday.")}</p></div><div class="footer-links"><div><strong>{t(lang,"了解轻一点","EXPLORE")}</strong><a href="{link(current,lang,"home")}#inside">{t(lang,"产品功能","Inside the app")}</a><a href="{link(current,lang,"home")}#availability">{t(lang,"发布状态","Availability")}</a><a href="{link(current,lang,"support")}">{t(lang,"技术支持","Support")}</a></div><div><strong>{t(lang,"信任与联系","TRUST & CONTACT")}</strong><a href="{link(current,lang,"privacy")}">{t(lang,"隐私政策","Privacy policy")}</a><a href="mailto:{EMAIL}">{t(lang,"联系开发者","Email the developer")}</a><a href="{REPO}" rel="noopener noreferrer">GitHub ↗</a></div></div></div><div class="footer-bottom"><p>{t(lang,"面向成年人提供一般习惯支持与记录，不替代专业医疗建议，不保证减重效果。","General habit support and records for adults. Does not replace professional medical advice or guarantee weight-loss results.")}</p><span translate="no">© 2026 {t(lang,"轻一点","Lighter")} · Made with care.</span></div></div></footer>'''

def document(lang, page, body, title, description, current=None, index=True):
    current = current if current is not None else path(lang, page)
    canonical = BASE + "/" + path(lang, page)
    alternates = "".join(f'<link rel="alternate" hreflang="{code}" href="{BASE}/{path(locale,page)}">' for code,locale in [("zh-Hans","zh"),("en","en"),("x-default","zh")])
    return f'''<!doctype html>
<html lang="{t(lang,"zh-Hans","en")}" class="no-js"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{e(title)}</title><meta name="description" content="{e(description)}"><meta name="theme-color" content="#fbfaf7"><meta name="color-scheme" content="light">
<meta name="referrer" content="strict-origin-when-cross-origin"><meta http-equiv="Content-Security-Policy" content="default-src 'self'; script-src 'self'; style-src 'self'; img-src 'self' data:; connect-src 'none'; font-src 'self'; object-src 'none'; base-uri 'self'; form-action 'none'; frame-src 'none'; upgrade-insecure-requests">
<meta name="robots" content="{'index,follow' if index else 'noindex,follow'}"><link rel="canonical" href="{canonical}">{alternates}
<meta property="og:type" content="website"><meta property="og:title" content="{e(title)}"><meta property="og:description" content="{e(description)}"><meta property="og:url" content="{canonical}"><meta property="og:image" content="{BASE}/{asset("", "social-card.jpg")}"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630"><meta property="og:locale" content="{t(lang,"zh_CN","en_US")}"><meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="{asset(current,"favicon-32.png")}" type="image/png" sizes="32x32"><link rel="icon" href="{asset(current,"mark.svg")}" type="image/svg+xml"><link rel="apple-touch-icon" href="{asset(current,"touch-icon.png")}"><link rel="stylesheet" href="{asset(current,"style.css")}"><script defer src="{asset(current,"site.js")}"></script>
</head><body>{header(current,lang,page)}{body}{footer(current,lang)}</body></html>'''

def home(lang):
    current = path(lang)
    get = lambda name: asset(current,name)
    support = link(current,lang,"support")
    privacy = link(current,lang,"privacy")
    views = [
      ("diet","饮食","Meals","每一餐，从容一点。","Make room for a good meal.","用简单的文字和选项记下一餐，保留真实感受。常吃餐食可以快速填写，让记录更顺手。","Capture a meal with simple words and choices, keeping your real experience. Reuse familiar meals for easier entries."),
      ("record","今天","Today","从一件做得到的小事开始。","Start with one achievable step.","一次关注一个主要行动。记录完成、部分完成或遇到的困难，再根据实际情况继续、调整或暂停。","Focus on one main action. Record completion, partial progress or difficulty, then continue, adjust or pause based on what happened."),
      ("activity","运动","Activity","按自己的节奏，记录活动。","Move and record at your own pace.","记录自主活动的日期、时长和主观感受。演示进度与真实活动分开保存，回顾时更清楚。","Log the date, duration and perceived effort of your own activities. Demonstration progress is stored separately from real activity."),
      ("progress","进展","Progress","看见过程，也保留不确定。","See the journey, with room for uncertainty.","保留原始测量、单位与真实记录。资料充分时再展示趋势，通过周复盘回看哪些行动更适合自己。","Keep original measurements, units and real entries. Show trends when records are sufficient, and review which actions fit your life.")
    ]
    switcher=""
    for key,zh,en,headzh,headen,desczh,descen in views:
        alt=t(lang,f"轻一点开发版本的{zh}页面，使用示例资料",f"Lighter development build: {en} screen, with example data")
        switcher += f'<a href="?view={key}#inside" data-view="{key}" data-image="{get(key+".webp")}" data-alt="{e(alt)}" data-heading="{e(t(lang,headzh,headen))}" data-description="{e(t(lang,desczh,descen))}" aria-current="{str(key=="diet").lower()}">{t(lang,zh,en)}</a>'
    hero_title=t(lang,'让改变，<br><em>轻一点。</em>','A little change.<br><em>A lighter day.</em>')
    hero_alt=t(lang,"轻一点饮食页：简单记一餐、主食蛋白质蔬菜示意及餐食记录","Lighter meals screen: simple meal entry, food categories and meal records. Chinese development interface.")
    body=f'''<main id="main">
<section class="wrap hero" aria-labelledby="hero-title"><div class="hero-copy"><span class="pill"><span class="status-dot" aria-hidden="true"></span>{t(lang,"iOS · 正在准备发布","iOS · Preparing for release")}</span><p class="eyebrow">Small steps. Lighter days.</p><h1 id="hero-title">{hero_title}</h1><p class="hero-description">{t(lang,"从好好吃一餐、动一动、记下今天开始。<br>轻一点，陪你把小小的改变，<br>慢慢放进自己的日常。","A good meal. A little movement. A moment to reflect.<br>Lighter helps you make small changes<br>that fit into your everyday life.")}</p><div class="button-row">{btn(t(lang,"认识轻一点","Meet Lighter"),"#inside")}<a class="text-link" href="{support}">{t(lang,"需要帮助","Find support")}<span aria-hidden="true">↗</span></a></div><p class="hero-note">{t(lang,"无需账号 · 本机记录 · 尊重你的节奏","No account · On-device records · Your own pace")}</p></div><div class="hero-art"><div class="orb" aria-hidden="true"></div><div class="orbit" aria-hidden="true"></div><div class="orb-dot" aria-hidden="true"></div><div class="phone hero-phone"><img src="{get("diet.webp")}" width="660" height="1435" alt="{hero_alt}" fetchpriority="high"></div><div class="float-card float-top"><span class="float-icon">{icon("check")}</span><span><strong>{t(lang,"一小步，也值得记录","Small steps count")}</strong><small>{t(lang,"把注意力放回今天","Make room for today")}</small></span></div><div class="float-card float-bottom"><span class="float-icon purple">{icon("shield")}</span><span><strong>{t(lang,"你的记录，由你控制","Your records. Your choice.")}</strong><small>{t(lang,"仅本机存储 · 可导出与删除","On-device · Export & delete")}</small></span></div><p class="hero-art-label">{t(lang,"开发版本真实界面 · 示例资料","Actual development interface · Example data")}</p></div></section>
<div class="wrap principles"><div class="principle"><span class="small-number">01 /</span>{t(lang,"吃好一点","Eat with ease")}</div><div class="principle"><span class="small-number">02 /</span>{t(lang,"按自己的节奏动一动","Move at your pace")}</div><div class="principle"><span class="small-number">03 /</span>{t(lang,"看见每一次小小的进展","Notice the small steps")}</div></div>
<section class="wrap section reveal" aria-labelledby="everyday-title"><p class="eyebrow">Designed for everyday life</p><div class="section-heading"><h2 id="everyday-title">{t(lang,"把注意力，<br>放在做得到的小事上。","A little less pressure.<br>A little more possibility.")}</h2><p>{t(lang,"不用把每一天都过成一道考题。<br>从一个适合自己的行动开始，用简单记录回看过程，再决定下一步。","Every day does not need to feel like a test. Start with an action that fits your life, record what happened, and decide on the next step.")}</p></div><div class="feature-grid"><article class="feature-card"><div class="feature-icon">{icon("leaf")}</div><h3>{t(lang,"吃饭，先从从容开始。","Make meals feel simpler.")}</h3><p>{t(lang,"简单记下一餐和自己的感受。少一点填写负担，多一点对日常的留意。","Log a meal and how it felt. Less effort filling things in, more attention to everyday life.")}</p><div class="food-row" aria-hidden="true"><img src="{get("rice.webp")}" width="360" height="360" alt="" loading="lazy"><img src="{get("protein.webp")}" width="360" height="360" alt="" loading="lazy"><img src="{get("vegetables.webp")}" width="360" height="360" alt="" loading="lazy"></div></article><article class="feature-card"><div class="feature-icon">{icon("steps")}</div><h3>{t(lang,"一步步，也是一种节奏。","Find a pace that fits.")}</h3><p>{t(lang,"关注一个主要行动，留下真实完成情况。需要时可以调整，也可以暂停。","Focus on one main action and record what you actually did. Adjust or pause when needed.")}</p><div class="step-trace" aria-hidden="true"><span></span><i></i><span></span><i></i><span></span><i></i><span></span><i></i><span></span><i></i><span></span></div></article><article class="feature-card"><div class="feature-icon">{icon("chart")}</div><h3>{t(lang,"看见过程，不急着下结论。","Reflect, without rushing.")}</h3><p>{t(lang,"保留原始记录，按真实资料回看。数据不足时，明确告诉你还不能判断。","Keep original entries and reflect on real records. When data is insufficient, the app says so.")}</p><svg class="trend-svg" viewBox="0 0 280 90" fill="none" aria-hidden="true"><path d="M5 70H275M5 40H275M5 10H275" stroke="#ded8cb" stroke-dasharray="3 6"/><path d="m8 61 43-9 45 10 42-24 43 7 46-20 45 8" stroke="#703ce3" stroke-width="2.5" stroke-linecap="round"/><circle cx="272" cy="33" r="5" fill="#d4e979" stroke="#703ce3" stroke-width="2"/></svg></article></div><p class="feature-note">{t(lang,"食物与曲线为功能示意，不代表个人餐单、测量结果或效果承诺。","Food and chart illustrations are examples, not personal meal plans, measurements or promised results.")}</p></section>
<section class="product-section" id="inside" aria-labelledby="inside-title"><div class="wrap product"><div class="product-visual"><div class="phone"><img data-product-image src="{get("diet.webp")}" width="660" height="1435" alt="{hero_alt}" loading="lazy"></div></div><div class="product-copy"><p class="eyebrow">A small companion, every day</p><h2 id="inside-title">{t(lang,"四个日常入口，<br>陪你慢慢来。","Four everyday spaces.<br>One gentle companion.")}</h2><nav class="view-switcher" aria-label="{t(lang,"查看 App 界面","Explore app screens")}">{switcher}</nav><div class="view-detail" aria-live="polite" aria-atomic="true"><h3 data-product-heading>{t(lang,views[0][3],views[0][4])}</h3><p data-product-description>{t(lang,views[0][5],views[0][6])}</p></div><p class="view-caption">{t(lang,"开发版本真实界面，包含示例或测试资料。","Actual development screens with example or test data. Screens shown in Chinese.")}</p><a class="text-link" href="{support}">{t(lang,"查看使用帮助","Read the usage guide")}{icon("arrow")}</a><div class="product-meta"><span>iOS 18.0+</span><span>iPhone & iPad</span><span>{t(lang,"本机优先","On-device first")}</span></div><noscript><p class="notice">{t(lang,"关闭 JavaScript 时展示饮食页；其他功能说明可在技术支持页查看。","With JavaScript disabled, the meals screen remains visible. Find other feature details on the support page.")}</p></noscript></div></div></section>
<section class="wrap privacy-band reveal" aria-labelledby="privacy-title"><div class="privacy-emblem" aria-hidden="true"><div class="emblem-disc">{icon("shield")}</div><span class="emblem-dot"></span></div><div><p class="eyebrow">Personal stays personal</p><h2 id="privacy-title">{t(lang,"私人的记录，<br>留在你手里。","Personal records.<br>In your hands.")}</h2><p>{t(lang,"你的饮食、活动与体重记录保存在设备本机。<br>无需创建账号，你可以自行导出、编辑或删除。<br>当前 App 不上传健康记录，也没有广告或第三方分析。","Your meal, activity and weight records stay on your device. No account is needed, and you can export, edit or delete your records. The current app does not upload health records or include ads or third-party analytics.")}</p><div class="privacy-chips"><span>{t(lang,"无需账号","No account")}</span><span>{t(lang,"本机存储","On-device storage")}</span><span>{t(lang,"导出与删除","Export & delete")}</span></div><a class="text-link" href="{privacy}">{t(lang,"阅读完整隐私政策","Read the full privacy policy")}{icon("arrow")}</a></div></section>
<section class="wrap launch" id="availability" aria-labelledby="launch-title"><div><p class="eyebrow">Good things take a little care</p><h2 id="launch-title">{t(lang,"轻一点，正在认真准备。","A little care before we launch.")}</h2><p>{t(lang,"当前为开发验证版本，尚未在 App Store 发布。我们正在完善体验，并继续专业内容审核与真机验收。正式上线后，这里会提供下载入口。","The current app is a development build and is not on the App Store yet. We are refining the experience, with professional content review and device acceptance still in progress. A download link will appear here when the app is released.")}</p></div><div class="launch-actions">{btn(t(lang,"联系开发者","Contact the developer"),mail_url(t(lang,"轻一点 · 产品咨询","Lighter product inquiry")),"light")}<small>{EMAIL}</small><small>{t(lang,"不收集订阅名单，你可以随时回来查看。","No mailing list. You can check back whenever you like.")}</small></div></section>
</main>'''
    return document(lang,"home",body,t(lang,"轻一点 Lighter — 让改变，轻一点。","Lighter — Small steps. Lighter days."),t(lang,"轻一点是一款面向成年人的本机习惯支持与记录 App。简单记餐、记录活动、回看进展，让改变融入日常。正在准备发布。","Lighter is an on-device habit and records app for adults. Log meals, record activity and reflect on progress at your own pace. Preparing for release."))

def page_hero(lang,page,eyebrow,title,lead,symbol,meta=""):
    current=path(lang,page)
    return f'''<section class="page-hero"><div class="wrap"><nav class="breadcrumb" aria-label="{t(lang,"面包屑导航","Breadcrumb")}"><a href="{link(current,lang,"home")}">{t(lang,"首页","Home")}</a><span aria-hidden="true">/</span><span>{title}</span></nav><div class="page-heading-row"><div><p class="eyebrow">{eyebrow}</p><h1>{title}</h1><p class="page-lead">{lead}</p>{meta}</div><div class="page-symbol" aria-hidden="true">{icon(symbol)}</div></div></div></section>'''

def privacy(lang):
    current=path(lang,"privacy")
    title=t(lang,"隐私政策","Privacy policy")
    date_label=t(lang,"2026 年 10 月 5 日","October 5, 2026")
    meta=f'<div class="page-meta"><span>{t(lang,"更新 / 生效","Updated / effective")}: <time datetime="{DATE}">{date_label}</time></span><span>{t(lang,"适用版本","App version")} {C["app_version"]}</span><span>{t(lang,"网站与技术支持","Website & support")}</span></div>'
    hero=page_hero(lang,"privacy","Your records. Your choice.",title,t(lang,"隐私应该说清楚。这里说明轻一点如何在本机处理记录，以及官网和技术支持各自涉及的信息。","Privacy should be clear. Here is how Lighter handles records on your device, and what happens when you visit the website or contact support."),"shield",meta)
    toc=f'<aside class="toc"><p class="toc-title">{t(lang,"本页目录","ON THIS PAGE")}</p>'
    sections=""
    values={"email":EMAIL,"repo":REPO,"repo_owner":"https://github.com/weizhichao1027-collab","support":link(current,lang,"support")}
    for number,(key,heading,copy) in enumerate(PRIVACY[lang],1):
        toc+=f'<a href="#{key}">{number:02d} · {heading}</a>'
        sections+=f'<section class="policy-section" id="{key}"><h2><span class="section-no">{number:02d}</span>{heading}</h2>{copy.format(**values)}</section>'
    toc+=f'<button type="button" class="copy-button" data-print>{icon("file")}{t(lang,"打印 / 保存 PDF","Print / save PDF")}</button></aside>'
    points=t(lang,["健康记录只在设备本机处理","App 不设账号、不上传健康记录","无广告与第三方分析 SDK","可以自行导出与删除"],["Health records processed on your device","No app account or health-record uploads","No ads or third-party analytics SDKs","Your choice to export and delete"])
    summary=f'<div class="summary-panel"><h2>{t(lang,"先看这四件事","Four things to know")}</h2><ul>'+"".join(f'<li>{point}</li>' for point in points)+f'</ul><p>{t(lang,"以上概括适用于当前 App。本网站的 GitHub 托管日志、支持通信及你主动导出的副本另有说明，请阅读下文。","These points describe the current app. GitHub hosting logs, support correspondence and copies you export are explained separately below.")}</p></div>'
    contact=f'<div class="contact-inline"><div><h3>{t(lang,"还有隐私方面的疑问？","Questions about privacy?")}</h3><p>{t(lang,"可以直接联系开发者，无需提供完整健康记录。","Contact the developer without sending complete health records.")}</p></div><a class="text-link" href="{mail_url("Lighter privacy request")}">{EMAIL} ↗</a></div>'
    body=f'<main id="main">{hero}<div class="wrap policy-layout">{toc}<article class="policy-body">{summary}{sections}{contact}<a class="back-top" href="#top">↑ {t(lang,"回到顶部","Back to top")}</a></article></div></main>'
    return document(lang,"privacy",body,t(lang,"隐私政策 — 轻一点 Lighter","Privacy policy — Lighter"),t(lang,"轻一点隐私政策：本机记录、系统权限、保存与删除、导出、网站托管和技术支持信息。","Lighter privacy policy: local records, permissions, retention, deletion, exports, website hosting and support information."))

def support(lang):
    current=path(lang,"support")
    privacy_link=link(current,lang,"privacy")
    title=t(lang,"我们在这里，帮你轻松一点。","A little help, when you need it.")
    hero=page_hero(lang,"support","A little help goes a long way",t(lang,"技术支持","Support"),title,"help")
    cards=""
    for heading,copy,ic,label,url in [
      (t(lang,"先找到一个答案","Find an answer"),t(lang,"记录、提醒、导出与删除，常见问题都在这里。","Common questions about records, reminders, exports and deletion."),"help",t(lang,"查看常见问题","Browse common questions"),"#faq"),
      (t(lang,"直接联系开发者","Contact the developer"),t(lang,"遇到技术问题或有建议，可以通过邮件与我们联系。","Email us about technical problems or suggestions."),"mail",EMAIL,mail_url("Lighter support")),
      (t(lang,"管理自己的记录","Manage your records"),t(lang,"了解本机数据、导出副本与删除范围，做清楚的选择。","Understand local data, exported copies and deletion controls."),"shield",t(lang,"阅读隐私政策","Read the privacy policy"),privacy_link)]:
        cards+=f'<article class="support-card"><div class="feature-icon">{icon(ic)}</div><h2>{heading}</h2><p>{copy}</p><a class="text-link" href="{e(url)}">{label}<span aria-hidden="true">↗</span></a></article>'
    toc=f'<aside class="toc"><p class="toc-title">{t(lang,"支持导航","SUPPORT GUIDE")}</p><a href="#faq">{t(lang,"常见问题","Common questions")}</a><a href="#contact">{t(lang,"提交技术问题","Report a technical issue")}</a><a href="#privacy-help">{t(lang,"隐私与数据请求","Privacy & data requests")}</a><a href="#release">{t(lang,"版本与发布状态","Version & availability")}</a></aside>'
    faq=""
    for key,question,answer in FAQ[lang]:
        answer=answer if answer.startswith("<") else f'<p>{answer}</p>'
        faq+=f'<details class="faq-item" data-faq id="faq-{key}"><summary>{question}</summary><div class="faq-answer">{answer}</div></details>'
    template=t(lang,"问题简述：\nApp 版本：\niOS 版本 / 设备型号：\nApp 语言：\n操作步骤：\n预期结果：\n实际结果 / 错误提示：\n\n请使用示例资料，并遮盖截图中的个人信息。无需附上健康记录或导出文件。","Issue summary:\nApp version:\niOS version / device model:\nApp language:\nSteps to reproduce:\nExpected result:\nActual result / error message:\n\nUse example data and redact personal details in screenshots. Do not attach health records or exports by default.")
    email_url=mail_url(t(lang,"轻一点 · 技术支持","Lighter technical support"),template)
    content=f'''<div><section id="faq" aria-labelledby="faq-title"><div class="faq-header"><h2 id="faq-title">{t(lang,"常见问题","Common questions")}</h2><span class="small-number">12 ANSWERS</span></div><div class="search-control"><label for="faq-search">{t(lang,"搜索帮助内容","Search help topics")}</label><input id="faq-search" name="q" type="search" data-faq-search autocomplete="off" placeholder="{t(lang,"例如：导出、提醒、删除…","Try export, reminders, delete…")}" aria-describedby="search-count">{icon("search")}</div><p class="search-count" id="search-count" data-search-count aria-live="polite"></p>{faq}<p class="no-results" data-no-results hidden>{t(lang,"暂时没有匹配的回答。试试更短的关键词，或通过下方邮箱联系我们。","No matching answers. Try a shorter keyword or email us below.")}</p></section>
<section class="support-block" id="contact"><p class="eyebrow">Let's work it out</p><h2>{t(lang,"遇到问题，一起理清楚。","Let’s work through it.")}</h2><p>{t(lang,"请用邮件描述问题。为方便排查，可以包含操作步骤和环境信息，不需要完整健康记录。","Describe the problem by email. Steps and environment information help us troubleshoot; complete health records are not needed.")}</p><div class="request-panel"><h3>{t(lang,"一封好排查的邮件，可以包含：","A useful support email includes:")}</h3><ol><li>{t(lang,"App 版本、iOS 版本、设备型号和 App 语言。","App version, iOS version, device model and app language.")}</li><li>{t(lang,"具体操作步骤、预期结果和实际提示。","Steps to reproduce, expected result and actual message.")}</li><li>{t(lang,"如需截图，请先遮盖体重、筛查答案和其他个人信息。","If sharing screenshots, redact weight, screening answers and other personal details.")}</li></ol><pre class="template-text" data-template>{e(template)}</pre><div class="copy-actions">{btn(t(lang,"打开邮件，描述问题","Open a support email"),email_url)}<button type="button" class="copy-button" data-copy="template">{icon("copy")}{t(lang,"复制反馈模板","Copy template")}</button></div><p class="copy-status" data-copy-status aria-live="polite"></p><p class="feature-note">{t(lang,"如果没有配置邮件 App，可复制邮箱，在常用邮件服务中发送：","If no mail app is configured, copy this address into your usual email service:")}<a href="mailto:{EMAIL}">{EMAIL}</a></p><div class="copy-actions"><button type="button" class="copy-button" data-copy="{EMAIL}">{t(lang,"复制邮箱","Copy email address")}</button><a class="text-link" href="{REPO}/issues/new/choose" rel="noopener noreferrer">{t(lang,"GitHub 公开技术反馈","Public GitHub feedback")} ↗</a></div><p class="feature-note">{t(lang,"GitHub 反馈公开可见，请勿提交真实健康记录或个人资料。支持回复需要人工处理，不提供实时医疗或急救服务。","GitHub feedback is public. Do not post health records or personal information. Support is handled manually and is not a real-time medical or emergency service.")}</p></div></section>
<section class="support-block" id="privacy-help"><h2>{t(lang,"隐私与数据请求","Privacy & data requests")}</h2><p>{t(lang,"本机记录的查看、导出与删除由你在 App 内操作。开发者无法远程访问设备中的数据。如果希望访问、更正或删除你曾主动发送的支持信息，请通过邮箱说明请求类型。","You control access, export and deletion of device records in the app; the developer cannot remotely access them. To request access, correction or deletion of information you sent to support, email us with the request type.")}</p><div class="button-row">{btn(t(lang,"发送隐私请求","Email a privacy request"),mail_url("Lighter privacy request"),"outline")}<a class="text-link" href="{privacy_link}#control">{t(lang,"查看数据管理说明","Read about data controls")} ↗</a></div></section>
<section class="support-block" id="release"><h2>{t(lang,"版本与发布状态","Version & availability")}</h2><p>{t(lang,"当前 App 为 0.1.0 开发验证版本，支持 iOS 18.0 及以上的 iPhone 与 iPad。尚未在 App Store 发布；专业内容审核、真机及完整平台验收仍在进行。官网上线不代表 App 已正式发布。","The current app is development version 0.1.0 for iPhone and iPad with iOS 18.0 or later. It is not on the App Store yet. Professional content review, device testing and full platform acceptance are still in progress. A live website does not mean the app has been released.")}</p><div class="release-mini"><strong>0.1.0</strong><span>{t(lang,"开发验证版本","Development build")}</span><span>{t(lang,"正在准备发布","Preparing for release")}</span></div></section><div class="notice health-note">{t(lang,"健康问题请寻求专业支持。轻一点提供一般习惯支持与记录，不能替代医生或其他专业医疗人员。若有紧急健康问题，请联系当地医疗或急救服务。","For health concerns, seek professional help. Lighter provides general habit support and records and cannot replace qualified healthcare professionals. Contact local medical or emergency services for urgent health concerns.")}</div><a class="back-top" href="#top">↑ {t(lang,"回到顶部","Back to top")}</a></div>'''
    body=f'<main id="main">{hero}<div class="wrap support-grid">{cards}</div><div class="wrap support-content">{toc}{content}</div></main>'
    return document(lang,"support",body,t(lang,"技术支持 — 轻一点 Lighter","Support — Lighter"),t(lang,"轻一点技术支持：记录、提醒、导出、删除与恢复的常见问题，以及开发者邮箱和隐私请求入口。","Lighter support: common questions about records, reminders, exports, deletion and recovery, plus developer contact and privacy requests."))

def build():
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir()
    shutil.copytree(ROOT / "assets", OUT / "assets")
    for lang in ["zh","en"]:
        for page,make in [("home",home),("privacy",privacy),("support",support)]:
            target=OUT / path(lang,page) / "index.html"
            target.parent.mkdir(parents=True,exist_ok=True)
            target.write_text(make(lang),encoding="utf-8")
    body=f'<main id="main" class="wrap not-found"><p class="eyebrow">404 / A little detour</p><h1>走岔了一小步。<br>A little detour.</h1><p>这个页面暂时找不到。回到首页，或让我们帮你找到答案。<br>This page could not be found. Try the home page or support.</p><div class="not-found-links">{btn("回到首页 / Home",BASE+"/")}{btn("技术支持 / Support",BASE+"/support/","outline")}</div></main>'
    # Absolute site URLs keep assets and navigation valid at arbitrary missing paths.
    error=document("zh","home",body,"页面未找到 / Page not found — Lighter","Return to Lighter or contact support.",current="",index=False)
    error=error.replace('href="./',f'href="{BASE}/')
    for prefix in ['href="assets/','src="assets/']:
        error=error.replace(prefix,prefix.split('assets/')[0]+BASE+'/assets/')
    for target in ["support/","privacy/","en/"]:
        error=error.replace(f'href="{target}"',f'href="{BASE}/{target}"')
    (OUT/"404.html").write_text(error,encoding="utf-8")
    (OUT/".nojekyll").write_text("")
    (OUT/"robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {BASE}/sitemap.xml\n")
    urls="".join(f'<url><loc>{BASE}/{path(lang,page)}</loc><lastmod>{DATE}</lastmod></url>' for lang in ["zh","en"] for page in ["home","support","privacy"])
    (OUT/"sitemap.xml").write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+urls+'</urlset>')
    print("Built 6 bilingual pages, a 404 page, sitemap and local assets.")

if __name__ == "__main__":
    build()

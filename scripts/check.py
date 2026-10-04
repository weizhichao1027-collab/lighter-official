#!/usr/bin/env python3
"""Validate the published artifact, including subpath links and FAQ anchors."""
import json
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse, unquote

ROOT=Path(__file__).resolve().parents[1]
SITE=ROOT/"site"
CONFIG=json.loads((ROOT/"config.json").read_text())
BASE=urlparse(CONFIG["site_url"])
errors=[]

class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids=set(); self.links=[]; self.h1=0; self.lang=None; self.title=False; self.description=False
        self.canonical=False; self.alternates=set(); self.summary=0; self.scripts=[]
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if tag=="html": self.lang=a.get("lang")
        if tag=="title": self.title=True
        if tag=="h1": self.h1+=1
        if tag=="summary": self.summary+=1
        if "id" in a:
            if a["id"] in self.ids: errors.append(f"duplicate id: {a['id']}")
            self.ids.add(a["id"])
        if tag=="meta" and a.get("name")=="description": self.description=bool(a.get("content"))
        if tag=="link" and a.get("rel")=="canonical": self.canonical=True
        if tag=="link" and a.get("rel")=="alternate": self.alternates.add(a.get("hreflang"))
        if tag=="img":
            for key in ["alt","width","height"]:
                if key not in a: errors.append(f"image lacks {key}: {a.get('src')}")
        if tag=="script" and not a.get("src"): errors.append("inline script found")
        if "style" in a: errors.append("inline CSS conflicts with CSP")
        for key in ["href","src","data-image"]:
            if a.get(key): self.links.append(a[key])

pages={}
for file in SITE.rglob("*.html"):
    parser=Page(); raw=file.read_text(); parser.feed(raw); pages[file.resolve()]=parser
    label=file.relative_to(SITE)
    if parser.h1!=1: errors.append(f"{label}: expected one h1, got {parser.h1}")
    if parser.lang not in ["en","zh-Hans"]: errors.append(f"{label}: missing language")
    if not (parser.title and parser.description and parser.canonical): errors.append(f"{label}: missing metadata")
    if parser.alternates!={"en","zh-Hans","x-default"}: errors.append(f"{label}: missing locale alternates")
    if "support" in str(label) and parser.summary!=12: errors.append(f"{label}: expected 12 FAQs")
    for term in ["TODO","lorem ipsum","example.com","your-email","{{","{%"]:
        if term in raw: errors.append(f"{label}: placeholder found: {term}")

links_checked=0
for file,parser in pages.items():
    for href in parser.links:
        url=urlparse(href)
        if url.scheme=="mailto":
            if url.path!=CONFIG["support_email"]: errors.append(f"unexpected email: {href}")
            continue
        if url.scheme in ["http","https"]:
            if url.netloc!=BASE.netloc or not url.path.startswith(BASE.path+"/"): continue
            local=SITE/unquote(url.path[len(BASE.path)+1:])
        elif url.scheme:
            errors.append(f"unsupported URL: {href}"); continue
        else:
            local=(file.parent/unquote(url.path)).resolve() if url.path else file
        if local.is_dir(): local=local/"index.html"
        if not local.exists(): errors.append(f"{file.relative_to(SITE)}: missing target {href}"); continue
        if url.fragment and local.suffix==".html":
            target=pages.get(local.resolve())
            if target and unquote(url.fragment) not in target.ids:
                errors.append(f"{file.relative_to(SITE)}: missing anchor {href}")
        links_checked+=1

if len(pages)!=7: errors.append(f"expected seven pages, got {len(pages)}")
for required in [".nojekyll","robots.txt","sitemap.xml","assets/social-card.jpg","assets/touch-icon.png"]:
    if not (SITE/required).exists(): errors.append(f"missing {required}")
for file in [ROOT/"assets/site.js",ROOT/"assets/style.css"]:
    code=file.read_text()
    for forbidden in ["transition: all","user-scalable=no","maximum-scale=1","document.cookie","localStorage","fetch("]:
        if forbidden in code: errors.append(f"{file.name}: unexpected {forbidden}")
if errors:
    for error in errors: print("ERROR:",error)
    raise SystemExit(1)
print(f"PASS: {len(pages)} pages, {links_checked} internal links/assets/anchors, metadata, images and static privacy checks.")

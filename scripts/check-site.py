#!/usr/bin/env python3
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit,unquote
import re
R=Path(__file__).resolve().parents[1]/'docs';errors=[];checked=0
class Scan(HTMLParser):
 def __init__(self,path):super().__init__();self.path=path;self.ids=set();self.links=[];self.h1=0
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if tag=='h1':self.h1+=1
  if 'id' in a:
   if a['id'] in self.ids:errors.append(f'{self.path}: duplicate id {a["id"]}')
   self.ids.add(a['id'])
  if tag=='img' and 'alt' not in a:errors.append(f'{self.path}: image missing alt')
  if tag=='script':errors.append(f'{self.path}: unexpected script')
  for key in ('href','src'):
   if key in a:self.links.append(a[key])
for path in R.rglob('*.html'):
 if '__qa' in path.parts:continue
 checked+=1;s=path.read_text();p=Scan(path);p.feed(s)
 if p.h1!=1:errors.append(f'{path}: expected one h1, got {p.h1}')
 for link in p.links:
  u=urlsplit(link)
  if u.scheme or u.netloc:continue
  t=(path.parent/unquote(u.path)).resolve() if u.path else path
  if t.is_dir():t/='index.html'
  if not t.is_file():errors.append(f'{path.relative_to(R)}: missing {link}')
  elif u.fragment:
   target=Scan(t);target.feed(t.read_text())
   if u.fragment not in target.ids:errors.append(f'{path.relative_to(R)}: missing anchor {link}')
 for bad in ['ryckmanestates@gmail.com','Ryckman Estates','David &','Kendra','Vault','neighborhood-demo.webp']:
  if bad in s:errors.append(f'{path}: stale/private content {bad}')
 if 'familyestatesapp@gmail.com' not in s:errors.append(f'{path}: missing support email')
for f in R.rglob('*.css'):
 for u in re.findall(r'url\([\'\"]?([^\)\'\"]+)',f.read_text()):
  if not urlsplit(u).scheme and not (f.parent/u).is_file():errors.append(f'{f}: missing CSS asset {u}')
print(f'Checked {checked} HTML pages, local links, anchors, image alt attributes, CSS assets, support email and stale/private content.')
if errors:
 print('\n'.join(errors));raise SystemExit(1)
print('PASS')

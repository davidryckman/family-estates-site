#!/usr/bin/env python3
"""Update public URLs after the chosen GitHub Pages destination is confirmed."""
import argparse,re
from pathlib import Path
from urllib.parse import urlparse
p=argparse.ArgumentParser();p.add_argument('url');args=p.parse_args()
url=args.url.rstrip('/')+'/'
a=urlparse(url)
if a.scheme!='https' or not a.netloc or a.query or a.fragment: p.error('Use a complete HTTPS base URL with no query or fragment.')
root=Path(__file__).resolve().parents[1]/'docs'
pat=r'https://davidryckman\.github\.io/(?:ryckman-estates-site|family-estates-site)/'
for file in root.rglob('*'):
 if file.suffix not in {'.html','.xml','.txt'}: continue
 text=file.read_text();updated=re.sub(pat,url,text)
 if updated!=text:file.write_text(updated)
print('Site metadata and absolute recovery links now use '+url)

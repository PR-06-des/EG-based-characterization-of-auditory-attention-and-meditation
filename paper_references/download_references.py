"""Download the article's CC BY figure assets for attributed reference comparison."""
from concurrent.futures import ThreadPoolExecutor
from html.parser import HTMLParser
from pathlib import Path
from urllib.request import urlopen
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parent
ARTICLE = 'https://pmc.ncbi.nlm.nih.gov/articles/PMC12417730/'


class Assets(HTMLParser):
    def __init__(self):
        super().__init__()
        self.assets = {}

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'img' and 'fnhum-19-1616456-g' in attrs.get('src', ''):
            url = attrs['src']
            number = int(re.search(r'-g(\d+)\.', url)[1])
            self.assets[f'figure_{number:02d}.jpg'] = url


parser = Assets()
if (ROOT / 'sources.json').exists():
    known_sources = json.loads((ROOT / 'sources.json').read_text(encoding='utf-8'))
    parser.assets = {asset['file']: asset['url'] for asset in known_sources['assets']}
else:
    parser.feed(urlopen(ARTICLE, timeout=60).read().decode('utf-8'))


def download(item):
    name, url = item
    destination = ROOT / name
    if not destination.exists():
        destination.write_bytes(urlopen(url, timeout=60).read())
    from PIL import Image
    with Image.open(destination) as picture:
        size = picture.size
    print(name, size, flush=True)
    return dict(file=name, url=url, width=size[0], height=size[1],
                sha256=hashlib.sha256(destination.read_bytes()).hexdigest())


with ThreadPoolExecutor(max_workers=4) as pool:
    manifest = list(pool.map(download, sorted(parser.assets.items())))
(ROOT / 'sources.json').write_text(json.dumps(dict(
    citation='Attar ET (2025). Frontiers in Human Neuroscience 19:1616456.',
    doi='10.3389/fnhum.2025.1616456', article=ARTICLE,
    license='CC BY 4.0', license_url='https://creativecommons.org/licenses/by/4.0/',
    note='Original published images for reference; these are not recomputed EEG results.',
    assets=manifest), indent=2), encoding='utf-8')

import os, re

d = r'c:\Users\byamb\OneDrive\Documents\CEECF'
files = [f for f in os.listdir(d) if f.endswith('.html')]

for fname in files:
    path = os.path.join(d, fname)
    with open(path, 'r', encoding='utf-8') as f:
        c = f.read()
    orig = c
    # Replace index.html#projects href with blog.html
    c = c.replace('index.html#projects', 'blog.html')
    # Replace the text labels (HTML-encoded and raw)
    c = c.replace('>Projects &amp; Impact<', '>Blogs<')
    c = c.replace('>Projects & Impact<', '>Blogs<')
    # Multi-line version split across lines
    c = re.sub(r'>Projects\s+(?:&amp;|&#38;|&)\s*\n\s*Impact<', '>Blog<', c)
    c = re.sub(r'>Projects &amp;\s*\n\s*Impact<', '>Blog<', c)
    if c != orig:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(c)
        print(f'Fixed: {fname}')

print('Done')

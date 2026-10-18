import re, glob

for f in glob.glob('PPL_2/*.html') + glob.glob('*.html'):
    with open(f, 'r', encoding='utf-8') as fl:
        text = fl.read()
    yts = set(re.findall(r'https?://[^\s"\'<>]+(?:youtube|youtu\.be)[^\s"\'<>]*', text))
    if yts:
        print(f, yts)


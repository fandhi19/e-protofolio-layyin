import re, os

with open('PPL_2/video.html', 'r', encoding='utf-8') as f:
    c = f.read()

img_srcs = set(re.findall(r'src=["\']([^"\']+)["\']', c))
url_srcs = set(re.findall(r'url\(["\']?([^"\')]+)["\']?\)', c))
all_srcs = img_srcs.union(url_srcs)

print("Verifying assets in PPL_2/video.html:")
all_ok = True
for src in sorted(all_srcs):
    if src.startswith('http'):
        continue
    rel = os.path.normpath(os.path.join('PPL_2', src))
    exists = os.path.exists(rel)
    print(f"  {src} -> {rel}: {'OK' if exists else 'MISSING'}")
    if not exists:
        all_ok = False

print("\nAll assets exist?", all_ok)


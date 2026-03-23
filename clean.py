import os, re

root = "."
pattern = re.compile(r'hf_[A-Za-z0-9]{20,}')
skip_dirs = {'.git'}

changed = []

for dirpath, dirnames, filenames in os.walk(root):
    dirnames[:] = [d for d in dirnames if d not in skip_dirs]
    for fn in filenames:
        path = os.path.join(dirpath, fn)
        try:
            with open(path, 'r', encoding='utf-8') as f:
                text = f.read()
        except:
            continue
        new_text = pattern.sub('HF_TOKEN_REDACTED', text)
        if new_text != text:
            with open(path, 'w', encoding='utf-8') as f:
                f.write(new_text)
            changed.append(path)

print("Cleaned files:")
for p in changed:
    print(p)

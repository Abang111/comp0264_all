import os
import re
from pathlib import Path

ROOT = Path(".")
TOKEN_PATTERN = re.compile(r"hf_[A-Za-z0-9]{20,}")
SKIP_DIRS = {".git"}
REPLACEMENT = "HF_TOKEN_REDACTED"

changed_files = []
skipped_files = []

for dirpath, dirnames, filenames in os.walk(ROOT):
    dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]

    for filename in filenames:
        path = Path(dirpath) / filename

        try:
            text = path.read_text(encoding="utf-8")
        except Exception:
            skipped_files.append(str(path))
            continue

        new_text = TOKEN_PATTERN.sub(REPLACEMENT, text)

        if new_text != text:
            path.write_text(new_text, encoding="utf-8")
            changed_files.append(str(path))

print("=== Cleaned files ===")
if changed_files:
    for file in changed_files:
        print(file)
else:
    print("No token found.")

print("\n=== Skipped non-text/binary/unreadable files ===")
if skipped_files:
    for file in skipped_files:
        print(file)
else:
    print("None.")

"""Auto-run entrypoint for .pth usage.

When tet.pth is in site-packages, Python runs `import tet.startup` at
interpreter startup, before any user code. Ordinary multi-line code works here
because this is a normal module, not the .pth line itself.
"""
import os

import sys
import time

sys.stderr.write("tet.pth loaded\n")
sleep_seconds = int(os.environ.get("TET_SLEEP_SECONDS", "5"))
for t in range(1, sleep_seconds + 1):
    time.sleep(1)
    sys.stderr.write(f"Sleeping for {sleep_seconds}. {t} passed\n")

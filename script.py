# /// script
# requires-python = ">=3.9"
# dependencies = [
#     "dynaconf",
#     "rich",
# ]
# ///
import time
from rich.progress import track

for i in track(range(20), description="test"):
    time.sleep(0.05)
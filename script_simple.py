import time
from rich.progress import track

for i in track(range(20), description="test"):
    time.sleep(0.05)
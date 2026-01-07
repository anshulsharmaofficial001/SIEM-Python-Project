import time
from datetime import datetime

log_file = "../logs/system_logs.txt"

while True:
    with open(log_file, "a") as f:
        f.write(f"{datetime.now()} - User login attempt detected\n")
    time.sleep(5)

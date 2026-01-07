from datetime import datetime

log_file = "../logs/system_logs.txt"
alert_file = "../alerts/alerts.txt"

failed_attempts = 0

with open(log_file, "r") as f:
    for line in f:
        if "login attempt" in line:
            failed_attempts += 1

if failed_attempts > 5:
    with open(alert_file, "a") as alert:
        alert.write(f"{datetime.now()} - ALERT: Brute force suspected!\n")
    print("🚨 Alert generated!")
else:
    print("✅ No alerts")

log_file = "../logs/system_logs.txt"

failed_attempts = 0

with open(log_file, "r") as f:
    for line in f:
        if "login attempt" in line:
            failed_attempts += 1

if failed_attempts > 5:
    print("⚠️ ALERT: Multiple login attempts detected!")
else:
    print("✅ System normal")

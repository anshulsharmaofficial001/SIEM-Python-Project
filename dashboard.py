log_file = "../logs/system_logs.txt"
alert_file = "../alerts/alerts.txt"

with open(log_file, "r") as f:
    logs = f.readlines()

with open(alert_file, "r") as a:
    alerts = a.readlines()

print("====== SIEM DASHBOARD ======")
print(f"Total Logs Collected : {len(logs)}")
print(f"Total Alerts Raised  : {len(alerts)}")

if len(alerts) > 0:
    print("⚠️ System Status: UNDER ATTACK")
else:
    print("✅ System Status: SAFE")

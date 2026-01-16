from zapv2 import ZAPv2
import time

target = "http://localhost:5000"

zap = ZAPv2()

print("Starting spider...")
zap.spider.scan(target)
time.sleep(2)

while int(zap.spider.status()) < 100:
    print(f"Spider progress: {zap.spider.status()}%")
    time.sleep(1)

print("Spider complete. Starting passive scan...")
zap.pscan.enable_all_scanners()

while int(zap.pscan.records_to_scan) > 0:
    print(f"Records left to scan: {zap.pscan.records_to_scan}")
    time.sleep(1)

print("Passive scan complete.")

alerts = zap.core.alerts()
print(f"Found {len(alerts)} alerts")

for alert in alerts:
    print(f"- {alert['alert']} ({alert['risk']})")

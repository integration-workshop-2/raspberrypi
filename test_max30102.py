from infra.hardware.max30102.heartrate_monitor import HeartRateMonitor

heart_rate_monitor = HeartRateMonitor()

while 1:
    heart_rate_monitor.get_readings()

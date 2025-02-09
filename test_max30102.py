from infra.hardware.max30102.heartrate_monitor import HeartRateMonitor

heart_rate_monitor = HeartRateMonitor()


print(heart_rate_monitor.get_readings())

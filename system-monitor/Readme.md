**System Monitor Automation Script 🚀**

**Overview**

*This Python script automates system monitoring by tracking:*

- CPU Usage
- Memory Usage
- Disk Usage
- System Information
- It logs data, generates reports, and sends alerts when thresholds are exceeded.

**Features**
 - ✅ Automated Monitoring - Runs continuously to check system metrics
 - ✅ Logging & Reporting - Saves logs and generates reports in JSON format
 - ✅ Alert System - Triggers warnings for high CPU, memory, or low disk space
 - ✅ Customizable Thresholds - Easily modify thresholds in config.py
 - ✅ Lightweight & Works with Python 3.9+

Project Structure
```
system_monitor/
│── monitor.py          # Main script to track system metrics
│── config.py           # Configuration settings (e.g., thresholds)
│── logger.py           # Logging utilities
│── notifier.py         # Alerting system (email, SMS, etc.)
│── report.py           # Report generation (e.g., JSON, CSV)
│── README.md           # Documentation
│── requirements.txt    # Required Python libraries
```
---
**Installation & Setup**
1. Clone the Repository
```
git clone https://github.com/yourusername/system_monitor.git
cd system_monitor
```
2. Install Dependencies
```
pip install -r requirements.txt
```
3. Run the Script
```
python monitor.py
```

```
Press Ctrl+C to stop monitoring.
```
---
**Customization**

Modify config.py to adjust alert thresholds:

```python
CPU_THRESHOLD = 80  # Alert if CPU usage exceeds 80%
MEMORY_THRESHOLD = 85  # Alert if Memory usage exceeds 85%
DISK_THRESHOLD = 90  # Alert if Disk usage exceeds 90%
```
---
**Automate Execution**

To run the script automatically at system startup or at intervals:

1. Using Cron (Linux/macOS)
Edit the cron jobs:

```crontab -e```

Add the following line to run the script every 10 minutes:
```
*/10 * * * * /usr/bin/python3 /path/to/system_monitor/monitor.py
```

2. Using Task Scheduler (Windows)
```
- Open Task Scheduler → Create Basic Task
- Set Trigger → "Daily" or "At system startup"
- Set Action → "Start a program"
- Select python.exe and pass the script path
```
---
**Future Improvements**

- Add Email/SMS alerts
- Export reports in CSV format
- Build a Web Dashboard for live monitoring
---

**License**
This project is licensed under the MIT License.
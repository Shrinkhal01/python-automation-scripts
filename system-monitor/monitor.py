import psutil
import platform
import time
import logging
from config import CPU_THRESHOLD, MEMORY_THRESHOLD, DISK_THRESHOLD
from notifier import send_alert
from report import generate_report

# Configure logging
logging.basicConfig(filename="system_monitor.log", level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s")


def get_system_info():
    return {
        "system": platform.system(),
        "node_name": platform.node(),
        "release": platform.release(),
        "version": platform.version(),
        "architecture": platform.architecture()
    }


def get_cpu_usage():
    return psutil.cpu_percent(interval=1)


def get_memory_usage():
    return psutil.virtual_memory().percent


def get_disk_usage():
    return psutil.disk_usage('/').percent


def check_thresholds():
    cpu_usage = get_cpu_usage()
    memory_usage = get_memory_usage()
    disk_usage = get_disk_usage()

    alert_messages = []

    if cpu_usage > CPU_THRESHOLD:
        alert_messages.append(f"High CPU Usage: {cpu_usage}%")
    if memory_usage > MEMORY_THRESHOLD:
        alert_messages.append(f"High Memory Usage: {memory_usage}%")
    if disk_usage > DISK_THRESHOLD:
        alert_messages.append(f"Low Disk Space: {disk_usage}%")

    if alert_messages:
        alert_message = "\n".join(alert_messages)
        logging.warning(alert_message)
        send_alert(alert_message)

    return {
        "CPU Usage": f"{cpu_usage}%",
        "Memory Usage": f"{memory_usage}%",
        "Disk Usage": f"{disk_usage}%"
    }


def main():
    logging.info("System Monitoring Started")
    print("System Monitoring Running... Press Ctrl+C to stop.")

    try:
        while True:
            system_stats = check_thresholds()
            logging.info(system_stats)
            generate_report(system_stats)
            time.sleep(10)  # Adjust frequency
    except KeyboardInterrupt:
        logging.info("System Monitoring Stopped")
        print("\nMonitoring Stopped.")


if __name__ == "__main__":
    main()

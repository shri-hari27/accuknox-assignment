import psutil
import time

CPU_THRESHOLD = 80
MEMORY_THRESHOLD = 80
DISK_THRESHOLD = 80
log_file_path = "/path/to/logfile.log"

def check_cpu():
    cpu_percent = psutil.cpu_percent(interval=1)
    if cpu_percent > CPU_THRESHOLD:
        log_message = f"CPU usage is {cpu_percent}%, exceeding threshold of {CPU_THRESHOLD}%"
        print(log_message)
        log_to_file(log_message)

def check_memory():
    memory_percent = psutil.virtual_memory().percent
    if memory_percent > MEMORY_THRESHOLD:
        log_message = f"Memory usage is {memory_percent}%, exceeding threshold of {MEMORY_THRESHOLD}%"
        print(log_message)
        log_to_file(log_message)

def check_disk():
    disk_percent = psutil.disk_usage('/').percent
    if disk_percent > DISK_THRESHOLD:
        log_message = f"Disk usage is {disk_percent}%, exceeding threshold of {DISK_THRESHOLD}%"
        print(log_message)
        log_to_file(log_message)

def check_processes():
    for proc in psutil.process_iter():
        try:
            process_name = proc.name()
            process_cpu_percent = proc.cpu_percent()
            process_memory_percent = proc.memory_percent()
            if process_cpu_percent > CPU_THRESHOLD:
                log_message = f"Process {process_name} is using {process_cpu_percent}% CPU"
                print(log_message)
                log_to_file(log_message)
            if process_memory_percent > MEMORY_THRESHOLD:
                log_message = f"Process {process_name} is using {process_memory_percent}% memory"
                print(log_message)
                log_to_file(log_message)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

def log_to_file(message):
    with open(log_file_path, "a") as log_file:
        log_file.write(f"{message}\n")

def main():
    while True:
        check_cpu()
        check_memory()
        check_disk()
        check_processes()
        time.sleep(60)

if __name__ == "__main__":
    main()
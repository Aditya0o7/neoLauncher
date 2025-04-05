import os
import time
import psutil
import ctypes
import wmi
import threading
import subprocess

def load_blocked_processes_from_file(filepath="blocked_processes.txt"):
    if not os.path.exists(filepath):
        return []
    with open(filepath, 'r') as f:
        processes = [line.strip().lower() for line in f if line.strip()]
    return processes

def get_neo_browser_path(filepath="neo_path.txt"):
    if not os.path.exists(filepath):
        print(f"Neo Browser path file '{filepath}' not found!")
        return None
    with open(filepath, 'r') as f:
        return f.read().strip()

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except Exception:
        return False

def kill_blocked_processes(blocked):
    for proc in psutil.process_iter(['pid', 'name']):
        try:
            if proc.info['name'] and proc.info['name'].lower() in blocked:
                os.system(f"taskkill /F /PID {proc.info['pid']}")
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue

def watcher_thread(blocked):
    c = wmi.WMI()
    process_watcher = c.Win32_Process.watch_for("creation")
    while True:
        try:
            new_process = process_watcher()
            proc_name = new_process.Name.lower()
            if proc_name in blocked:
                print(f"Killing {new_process.Name} (PID: {new_process.ProcessId})")
                os.system(f"taskkill /F /PID {new_process.ProcessId}")
        except Exception as e:
            print("Watcher error:", e)

def polling_thread(blocked):
    while True:
        kill_blocked_processes(blocked)
        time.sleep(0.1)

def main():
    if not is_admin():
        print("Run this script as Administrator!")
        exit(1)

    blocked = load_blocked_processes_from_file()
    neo_path = get_neo_browser_path()

    if not neo_path:
        print("No Neo Browser path found, exiting.")
        exit(1)

    print("Lockdown active. Blocking:", ', '.join(blocked))

    t1 = threading.Thread(target=watcher_thread, args=(blocked,), daemon=True)
    t2 = threading.Thread(target=polling_thread, args=(blocked,), daemon=True)
    t1.start()
    t2.start()

    try:
        neo_process = subprocess.Popen(f'"{neo_path}"') 
    except Exception as e:
        print("Failed to open Neo Browser:", e)

    while True:
        if neo_process.poll() is not None:
            print("Neo Browser closed.")
            break
    time.sleep(1)
    

if __name__ == "__main__":
    main()

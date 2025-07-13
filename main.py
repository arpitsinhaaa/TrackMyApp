import time
import psutil
import win32gui
import win32process

def get_foreground_app():
    try:
        hwnd = win32gui.GetForegroundWindow()
        _, pid = win32process.GetWindowThreadProcessId(hwnd)
        process = psutil.Process(pid)
        return process.name()
    except Exception:
        return None

def track_apps(log_file="app_usage_log.txt"):
    last_app = None
    start_time = time.time()

    with open(log_file, "a") as f:
        f.write(f"\n--- App Tracking Started at {time.ctime()} ---\n")

        while True:
            current_app = get_foreground_app()

            if current_app != last_app:
                end_time = time.time()

                if last_app is not None:
                    duration = end_time - start_time
                    f.write(f"{time.ctime(start_time)} - {time.ctime(end_time)}: {last_app} (used for {duration:.1f} seconds)\n")
                    f.flush()

                start_time = end_time
                last_app = current_app

            time.sleep(1)

if __name__ == "__main__":
    track_apps()

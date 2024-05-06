import psutil
import wmi

f = wmi.WMI()

def terminate_dyknow_processes():
    for p in psutil.process_iter(attrs=["pid", "name"]):
        if p.pid != 0:
            try:
                path = p.exe()
                if "DyKnow" in path:
                    p.terminate()
                    print("DyKnow process terminated successfully: %d" % p.pid)
            except psutil.NoSuchProcess:
                pass
            except psutil.AccessDenied:
                print("Access denied to terminate process: %d" % p.pid)

while True:
    terminate_dyknow_processes()

import os
import signal
import psutil
import subprocess
import wmi
f = wmi.WMI()
def terminate_process_id(process_id):
    for process in f.Win32_Process (ProcessId=process_id):
        print(process.ProcessId, process.Name)
    try:
        process.Terminate()
        print("Process terminated successfully: %d" % process.ProcessId)
    except:
        print("There is no process running with id: %d" % process_id)

while True:
    for p in psutil.process_iter(attrs=["pid", "name"]):
        path = ""
        try:
            path = str(p.exe())
        except:
            print("Couldn't fetch path")
        if path.find("DyKnow") != -1:
            print("Dyknow found", p.info['pid'], path)
            terminate_process_id(p.info['pid'])

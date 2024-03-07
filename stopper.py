# import necessary libraries
import psutil
import wmi
# initialize WMI
f = wmi.WMI()
# function to end a process with given id
def terminate_process_id(process_id):
    for process in f.Win32_Process (ProcessId=process_id):
        print(process.ProcessId, process.Name)
    try:
        process.Terminate()
        print("Process terminated successfully: %d" % process.ProcessId)
    except:
        print("There is no process running with id: %d" % process_id)
# constantly loop through processes
while True:
    for p in psutil.process_iter(attrs=["pid", "name"]):
        # try to get the exe file location of each process
        path = ""
        try:
            path = str(p.exe())
        except:
            print("Couldn't fetch path")
        # if file path contains "DyKnow" then kill the process
        if path.find("DyKnow") != -1:
            print("Dyknow found", p.info['pid'], path)
            terminate_process_id(p.info['pid'])

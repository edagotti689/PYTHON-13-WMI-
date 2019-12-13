import wmi

conn = wmi.WMI()

## To get process id and name for notepad++
for p in conn.Win32_Process(name="notepad++.exe"):
    print(' \n Process Name is ==>', p.Name)
    print(' \n Process ID   is ==>', p.ProcessID)
    ## To stop process
    # p.Terminate()


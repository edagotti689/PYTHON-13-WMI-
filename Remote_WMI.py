import wmi

try:
    con = wmi.WMI('172.20.56.225',user='Administrato',password='Compaq123')
    print con
except wmi.x_access_denied:
     print 'wmi.x_access_denied'

# To run commnads on remote machine
pid, status = con.Win32_Process.Create(CommandLine=command, \ CurrentDirectory='path') 

'''Return a object which will contain all information about operating system.
Example:
connection.Win32_OperatingSystem()[0].Caption = u'Microsoft Windows 7 Enterprise'
connection.Win32_OperatingSystem()[0].OSArchitecture = u'64-bit'
'''
ret = con.Win32_OperatingSystem()



'''
Return the list of tuple of service and service state.
Example:
services = [(u'Adobe Acrobat Update Service', u'Running'),
(u'Adobe Flash Player Update Service', u'Stopped')]
'''
service = connection.Win32_Service()
print(service.displayName,service.State)


## To run query 
qo = connection.query("Select * from Win32_PnPEntity WHERE ConfigManagerErrorCode <> 0")

import wmi
c = wmi.WMI()
wql = "SELECT Caption, Description FROM Win32_LogicalDisk WHERE DriveType <> 3"
for disk in c.query(wql):
  print disk    

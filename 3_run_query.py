import wmi

# To create a connection object for local machine
c = wmi.WMI()

# To run query to get Disks
wql = "SELECT Caption, Description FROM Win32_LogicalDisk"
for disk in c.query(wql):
  print(disk)


import wmi

# To create a connection object for local machine
c = wmi.WMI()


# To know OS type and OS bit
for os in c.Win32_OperatingSystem():
  print(os.Caption)
  print(os.OSArchitecture)

# To get all processes
# service = c.Win32_Service()
# for s in service:
    # print(s.displayName,'  ::  ', s.State)

# To run query to get Disks
# wql = "SELECT Caption, Description FROM Win32_LogicalDisk"
# for disk in c.query(wql):
  # print(disk)


import wmi

# To create a connection object for local machine
c = wmi.WMI()


##  To know OS type and OS bit
for os in c.Win32_OperatingSystem():
  print(' OS TYPE IS : ', os.Caption)
  print(' OS BIT IS  : ', os.OSArchitecture)




# hostname
# IP-address
# MAC-address
# Operation System
# Processor Model
# System time
# Internet connection speed
# Active ports

import socket
import psutil
import platform
import subprocess
import re

def start():
  
  # Gather the Hostname
  def getSystemHostname():
    return socket.gethostname()
  
   # Get the system's local IP address
  def getSystemIPv4Address():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.connect(("1.1.1.1", 443))
    localIPAddress = sock.getsockname()[0]
    sock.close()
    return localIPAddress

  # Get the MAC address of the NIC that has an active internet connection
  def getSystemMACAddress():
    for interface in psutil.net_if_addrs():
      # Check if the interface has a valid MAC address
      if psutil.net_if_addrs()[interface][0].address:
          # Print the MAC address for the interface
          macAddress = psutil.net_if_addrs()[interface][0].address
          # breakx
    return macAddress
  
  # Get the System Operating system
  def getSystemOS():
    return platform.platform()

  def getSystemCPUInfo():
    if bool(re.search(r'\bLinux\b', getSystemOS())) == True:
      cpu_info = {}
      cpu_info['Processor'] = platform.processor()
      try:
        # Using lscpu command to get detailed CPU information
        lscpu_output = subprocess.check_output("lscpu", shell=True).decode()
        for line in lscpu_output.split('\n'):
            if "Model name" in line:
                cpu_info['Model name'] = line.split(":")[1].strip()
            if "Architecture" in line:
                cpu_info['Architecture'] = line.split(":")[1].strip()
      except Exception as e:
        print(f"An error occurred while retrieving CPU information: {e}")
      return cpu_info
    elif bool(re.search(r'\bWindows\b', getSystemOS())) == True:
      cpu_info = {}
      cpu_info['Processor'] = platform.processor()
      try:
        # Using wmic command to get detailed CPU information
        wmic_output = subprocess.check_output("wmic cpu get name, numberofcores, maxclockspeed", shell=True).decode()
        for line in wmic_output.split('\n'):
            if "Name" in line:
                cpu_info['Model name'] = line.split()[1].strip()
            if "NumberOfCores" in line:
                cpu_info['Number of Cores'] = line.split()[1].strip()
      except Exception as e:
        print(f"An error occurred while retrieving CPU information: {e}")

      return cpu_info
    else:
      return "unknown system"


  print(getSystemCPUInfo())
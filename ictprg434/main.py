# hostname
# IP-address
# MAC-address
# Operation System
# Processor Model
# System time
# Internet connection speed
# Active ports

import socket, psutil, platform, subprocess, re
from datetime import datetime

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
  
  def getSystemTime():
    return datetime.now().strftime("%d/%m/%Y %H:%M:%S")
  
  def getSystemNetworkInterfaceName(target_ip):
    interfaces = psutil.net_if_addrs()
    for interface_name, addresses in interfaces.items():
        for address in addresses:
            if address.family == socket.AF_INET and address.address == target_ip:
                return interface_name
    return None

  def getSystemNetworkSpeed(interfaceName):
    # Retrieve network interfaces and their stats
    nic_stats = psutil.net_if_stats()
    nic_speed = nic_stats.get(interfaceName).speed
    return f"{nic_speed} Mbps"
  

  def getSystemNetworkPorts():
    # Get all network connections
    connections = psutil.net_connections()
    active_ports = []

    for conn in connections:
        # Only consider active connections (e.g., LISTEN or ESTABLISHED states)
        if conn.status in ('LISTEN'):
            port = conn.laddr.port
            active_ports.append(port)
            # print(f"Protocol: {conn.type.name}, Port: {port}, Status: {conn.status}")

    return active_ports

  

  print(getSystemNetworkPorts())

  # 
import socket, psutil, platform, subprocess, re, csv, os
from datetime import datetime

def start():
  # Gather System Hostname
  def getSystemHostname():
    return f"{socket.gethostname()}"

  # Get the system's local IP address based of WAN connection
  def getSystemIPv4Address():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.connect(("1.1.1.1", 443))
    local_IP_address = sock.getsockname()[0]
    sock.close()
    return f"{local_IP_address}"

  # Get the NIC MAC Address
  def getSystemMACAddress(network_interface_name):
    # Get all network interfaces and their addresses
    interfaces = psutil.net_if_addrs()

  	# Check if the specified interface is in the list
    if network_interface_name in interfaces:
      for addr in interfaces[network_interface_name]:
      # Look for the MAC address, which is identified by AF_LINK family
        if addr.family == psutil.AF_LINK:
          return f"{addr.address}"
    return "Missing Information"

  # # Get the System Operating system
  def getSystemOS():
    return f"{platform.platform()}"

  # Get the Systems CPU information
  # Check if the system is Windows or Linux
  # This is due to differance in system information
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
        print(f"Error occurred while retrieving Linux CPU information: {e}")
      return f"{cpu_info['Model name']}"
    elif bool(re.search(r'\bWindows\b', getSystemOS())) == True:
      get_cpu_command = "powershell -Command \"(Get-CimInstance -ClassName Win32_Processor).Name\""
      get_cpu_result = subprocess.check_output(get_cpu_command, shell=True, text=True)
      return get_cpu_result.strip()
    else:
      return "unknown system/CPU Information"

  # Get the system time
  def getSystemTime():
    time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    return f"{time}"

  # Get the NIC name based of the IP with an WAN network connection
  def getSystemNetworkInterfaceName(target_ip):
    interfaces = psutil.net_if_addrs()
    for interface_name, addresses in interfaces.items():
      for address in addresses:
        if address.family == socket.AF_INET and address.address == target_ip:
          return f"{interface_name}"

  # Use the NIC to gather the device's speed
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
      # Only consider activly listening connections
      if conn.status in ('LISTEN'):
        port = conn.laddr.port
        active_ports.append(port)
    return f"{active_ports}"

  # Organise the CSV Headers
  def fieldNames():
    field_names = [
      "@time_",
      "Hostname",
      "IP Address",
      "MAC-address",
      "Operation System",
      "Processor Model",
      "NIC Speed",
      "Listening ports"
    ]
    return field_names

  # Organise the Data into a Json Dictionary
  def combineData():
    data = [{
      "@time_": getSystemTime(),
      "Hostname": getSystemHostname(),
      "IP Address": getSystemIPv4Address(),
      "MAC-address": getSystemMACAddress(getSystemNetworkInterfaceName(getSystemIPv4Address())),
      "Operation System": getSystemOS(),
      "Processor Model": getSystemCPUInfo(),
      "NIC Speed": getSystemNetworkSpeed(getSystemNetworkInterfaceName(getSystemIPv4Address())),
      "Listening ports": getSystemNetworkPorts()
    }]
    return data

  # Write to the file
  # Append the Data if header/file already exist
  with open("hostData.csv", "a", newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldNames()) # Assign the Header of the CSV
    # Only Write to the Header if it doesn't exist
    if os.stat("hostData.csv").st_size == 0:
      writer.writeheader() # Write the headers if no headers
      writer.writerows(combineData()) # Wrie Gathered Data to CSV
      return f"CSV Created, headers added and Data added" # Inform file made, headers added and data added
    else:
      writer.writerows(combineData()) # Wrie Gathered Data to CSV
      return f"Data Appended" # Inform that the data had been added
    
# print(start())
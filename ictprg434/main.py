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


  print(getSystemOS())
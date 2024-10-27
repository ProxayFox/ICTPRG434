# Computer Name
# IP-address
# MAC-address
# Processor Model
# Operation System
# System time
# Internet connection speed
# Active ports

import socket
import psutil
import platform
from datetime import datetime
import speedtest
# import nmap

# Gather the Hostname
hostname = socket.gethostname()

# Get the system's local IP address
# create an datagram socket (single UDP request and response, then close)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# connect to an address on the internet, that's likely to always be up to gather the connection infomation
sock.connect(("1.1.1.1", 80))
# after connecting, the socket will have the IP in its address
localIPAddress = sock.getsockname()[0]
# Close off the socket
sock.close()

# Get the System's MAC address
for interface in psutil.net_if_addrs():
    # Check if the interface has a valid MAC address
    if psutil.net_if_addrs()[interface][0].address:
        # Print the MAC address for the interface
        macAddress = psutil.net_if_addrs()[interface][0].address
        # breakx

# Get CPU Information
cpu_info = platform.processor()
# Get CPU Core Count
cpu_count = psutil.cpu_count(logical=False)
# Get CPU Thread Count
logical_cpu_count = psutil.cpu_count(logical=True)

# Get Current operating system
operatingSystem = platform.platform()

# Get the current time
currentTime = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

# Get Connection Speed
def internet_speed_test():
    try:
        st = speedtest.Speedtest()
        print("Testing internet speed...")

        # Perform the download speed test
        download_speed = st.download() / 1000000  # Convert to Mbps

        # Perform the upload speed test
        upload_speed = st.upload() / 1000000  # Convert to Mbps

        # Print the results
        print("{:.2f} Mpbs / ".format(download_speed)+"{:.2f} Mpbs".format(upload_speed))

    except speedtest.SpeedtestException as e:
        print("An error occurred during the speed test:", str(e))


ip = socket.gethostbyname (socket.gethostname())  #getting ip-address of host
 
# for port in range(65535):      #check for all available ports
 
#     try:
  
#         serv = socket.socket(socket.AF_INET,socket.SOCK_STREAM) # create a new socket
 
#         serv.bind((ip,port)) # bind socket with address
        
            
#     except:
 
#         print(port) #print open port number
 
#     serv.close() #close connection

print(macAddress)
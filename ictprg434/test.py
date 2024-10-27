import platform
import subprocess

def get_cpu_info():
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

cpu_info = get_cpu_info()
print(f"Processor: {cpu_info.get('Processor', 'Unknown')}")
print(f"Model name: {cpu_info.get('Model name', 'Unknown')}")
print(f"Architecture: {cpu_info.get('Architecture', 'Unknown')}")
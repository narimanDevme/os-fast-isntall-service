import platform
import subprocess
host = "194.33.105.38"
system_info = platform.system()
command = "sudo apt-get update"
command2 = f"ping {host}"
if system_info == "linux":
    try:
        result =  subprocess.run(['sudo', '-S'] + command.split(), check=True, text=True, input='dev2256N\n')
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"error : {e}")
elif system_info == "Windows":
    try:
        result = subprocess.run(command2, capture_output=True, text=True, shell=True, check=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"error : {e}")
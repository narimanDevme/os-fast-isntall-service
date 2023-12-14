import platform
import subprocess
import time
host = "194.33.105.38"
system_info = platform.system()

l_command1 = "apt-get update\n"
l_command2 = "curl -o setup-repos.sh https://raw.githubusercontent.com/webmin/webmin/master/setup-repos.sh"
l_command4 = "sh setup-repos.sh"
l_command3 = "apt-get install webmin --install-recommends -y\n"
l_command5 = "apt-get install vsftpd -y"
l_command6 = "systemctl start vsftpd"
l_command7 = "systemctl enable vsftpd"
command2 = f"ping {host}"
if system_info == "Linux":
    try:

        # update
        result1 =  subprocess.run(['sudo', '-S'] + l_command1.split(), check=True, text=True, input='dev2256N\n')
        print(result1.stdout)
        time.sleep(1)

        #webmin
        result2 = subprocess.run(l_command2.split(), check=True, text=True, input='dev2256N\n')
        print(result2)
        result4 = subprocess.run(l_command4.split(), check=True, text=True, input='dev2256N\n')
        print(result4)
        result3 = subprocess.run(l_command3.split(), check=True, text=True, input='dev2256N\n')
        print(result3)

        #vsftpd
        result5 = subprocess.run(l_command5.split(), check=True, text=True, input='dev2256N\n')
        print(result5)
        result6 = subprocess.run(l_command6.split(), check=True, text=True, input='dev2256N\n')
        print(result6)
        result7 = subprocess.run(l_command7.split(), check=True, text=True, input='dev2256N\n')
        print(result7)
        


    except subprocess.CalledProcessError as e:
        print(f"error : {e}")
elif system_info == "Windows":
    try:
        result = subprocess.run(command2, capture_output=True, text=True, shell=True, check=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"error : {e}")
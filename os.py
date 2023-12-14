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
l_command8 = "cd"
l_command9 = "cd /home/"
l_command10 = "mkdir ftp"
l_command11 = "chown nobody:nogroup ftp"
l_command12 = "chmod a-w ftp"
l_command13 = "cd ftp"
l_command14 = "mkdir server"
l_command15 = "chown root:root server"
l_command16 = "cd"
l_command17 = "cd /etc/"
l_command18 = "rm -R vsftpd.conf"
l_command19 = "git clone https://github.com/narimanDevme/vsftpd.conf.git"
command2 = f"ping {host}"
if system_info == "Linux":
    try:

        # update
        result1 =  subprocess.run(['sudo', '-S'] + l_command1.split(), check=True, text=True, input='dev2256N\n')
        print(result1.stdout)
        print("$$$$$$$ update finish $$$$$$$$")
        time.sleep(3)

        #webmin
        result2 = subprocess.run(l_command2.split(), check=True, text=True, input='dev2256N\n')
        print(result2)
        result4 = subprocess.run(l_command4.split(), check=True, text=True, input='dev2256N\n')
        print(result4)
        result3 = subprocess.run(l_command3.split(), check=True, text=True, input='dev2256N\n')
        print(result3)
        print("$$$$$$$ webmin finish $$$$$$$$")
        time.sleep(3)


        #vsftpd
        result5 = subprocess.run(l_command5.split(), check=True, text=True, input='dev2256N\n')
        print(result5)
        result6 = subprocess.run(l_command6.split(), check=True, text=True, input='dev2256N\n')
        print(result6)
        result7 = subprocess.run(l_command7.split(), check=True, text=True, input='dev2256N\n')
        print(result7)
        result8 = subprocess.run(l_command8.split(), check=True, text=True, input='dev2256N\n')
        print(result8)
        result9 = subprocess.run(l_command9.split(), check=True, text=True, input='dev2256N\n')
        print(result9)
        result10 = subprocess.run(l_command10.split(), check=True, text=True, input='dev2256N\n')
        print(result10)
        result11 = subprocess.run(l_command11.split(), check=True, text=True, input='dev2256N\n')
        print(result11)
        result12 = subprocess.run(l_command12.split(), check=True, text=True, input='dev2256N\n')
        print(result12)
        result13 = subprocess.run(l_command13.split(), check=True, text=True, input='dev2256N\n')
        print(result13)
        result14 = subprocess.run(l_command14.split(), check=True, text=True, input='dev2256N\n')
        print(result14)
        result15 = subprocess.run(l_command15.split(), check=True, text=True, input='dev2256N\n')
        print(result15)
        result16 = subprocess.run(l_command16.split(), check=True, text=True, input='dev2256N\n')
        print(result16)
        result17 = subprocess.run(l_command17.split(), check=True, text=True, input='dev2256N\n')
        print(result7)
        result18 = subprocess.run(l_command18.split(), check=True, text=True, input='dev2256N\n')
        print(result18)
        result19 = subprocess.run(l_command19.split(), check=True, text=True, input='dev2256N\n')
        print(result19)
        print("$$$$$$$ vsftpd finish $$$$$$$$")
        time.sleep(3)



    except subprocess.CalledProcessError as e:
        print(f"error : {e}")
elif system_info == "Windows":
    try:
        result = subprocess.run(command2, capture_output=True, text=True, shell=True, check=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"error : {e}")
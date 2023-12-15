import platform
import subprocess
import time
import os
host = "194.33.105.38"
system_info = os.uname()
system_info = system_info.sysname

l_command1 = "apt-get update -y\n"
l_command2 = "curl -o setup-repos.sh https://raw.githubusercontent.com/webmin/webmin/master/setup-repos.sh\nsh setup-repos.sh\n"
#l_command4 = "sh setup-repos.sh"
l_command3 = "apt-get install webmin --install-recommends -y\n"
l_command5 = "apt-get install vsftpd -y"
l_command6 = "systemctl start vsftpd"
l_command7 = "systemctl enable vsftpd"
l_command19 = "git clone https://github.com/narimanDevme/vsftpd.conf.git"
l_command20 = "bash <(curl -Ls https://raw.githubusercontent.com/vaxilu/x-ui/master/install.sh)"
#l_command21 = "echo \"deb [signed-by=/etc/apt/keyrings/openvpn-as.gpg.key] http://as-repository.openvpn.net/as/debian $(lsb_release -cs) main\" | sudo tee /etc/apt/sources.list.d/openvpn-as.list"
#l_command22 = "wget --quiet -O - https://as-repository.openvpn.net/as-repo-public.gpg | sudo tee /etc/apt/keyrings/openvpn-as.gpg.key"
#l_command23 = "sudo apt install apt-transport-https ca-certificates"
#l_command24 = "sudo apt update"
#l_command25 = "sudo apt install -y openvpn-as"
l_command26 = "apt-get install nmap -y"
l_command25 = "wget http://download.configserver.com/csf.tgz"
l_command26 = "tar -xzf csf.tgz"
l_command27 = "ufw disable"
l_command28 = "cd csf\nsh install.sh"
l_command29 = "perl /usr/local/csf/bin/csftest.pl"
command2 = f"ping {host}"
if system_info == "Linux":
    try:

        # update
        os.system(l_command1)
        print("$$$$$$$ update finish $$$$$$$$")
        time.sleep(3)
        #webmin
        os.system(l_command2)
        os.system(l_command3)
        print("$$$$$$$ webmin finish $$$$$$$$")
        time.sleep(3)
        #vsftpd
        os.system(l_command5)
        os.system(l_command6)
        os.system(l_command7)
        os.system(l_command19)
        print("$$$$$$$ vsftpd finish $$$$$$$$")
        time.sleep(3)
        #xui
        os.system(l_command20)
        print("$$$$$$$ v2ray panel finish $$$$$$$$")
        time.sleep(3)
        #open vpn :
        #os.system(l_command21)
        #os.system(l_command22)
        #os.system(l_command23)
        #os.system(l_command24)
        #os.system(l_command25)
        #print("$$$$$$$ openvpn panel finish $$$$$$$$")
        #time.sleep(3)
        #csf 
        os.system(l_command26)
        os.system(l_command27)
        os.system(l_command28)
        os.system(l_command29)
        print("$$$$$$$ csf finish $$$$$$$$")
        time.sleep(3)
    except subprocess.CalledProcessError as e:
        print(" $$$$$$$$$$ $$$$$$$$$$ we have Error ! $$$$$$$$$$$$ $$$$$$$$$$")
elif system_info == "Windows":
    try:
        result = subprocess.run(command2, capture_output=True, text=True, shell=True, check=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"error : {e}")
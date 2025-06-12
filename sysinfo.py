import subprocess

def list_info():
    print("Script")
    print("1. OS & Partisi")
    print("2. lshw")
    print("3. lsusb")
    print("4. NTP")
    print("5. Exit")
    print("Pilih informasi yang ingin ditampilkan :")

def hostname_partisi():
    ipaddr = subprocess.check_output("hostname -I | awk {'print $1'}\n", shell=True)
    hostname = subprocess.check_output("hostnamectl\n", shell=True)
    partisi = subprocess.check_output("df -h\n", shell=True)
    print("IP Address :",ipaddr.decode())
    print(hostname.decode())
    print(partisi.decode())    

def lshw():
    ipaddr = subprocess.check_output("hostname -I | awk '{print $1}'\n", shell=True)
    lshw = subprocess.check_output("sudo lshw -short -C processor -C Storage -C memory -C display", shell=True)
    parted_l = subprocess.check_output("sudo parted -l", shell=True)
    print("IP Address :",ipaddr.decode())
    print(lshw.decode())
    print(parted_l.decode()) 

def lsusb():
    ipaddr = subprocess.check_output("hostname -I | awk {'print $1'}\n", shell=True)
    lsusb = subprocess.check_output("lsusb")
    print("IP Address :",ipaddr.decode())
    print(lsusb.decode())

def ntp():
    ipaddr = subprocess.check_output("hostname -I | awk {'print $1'}\n", shell=True)
    ntp = subprocess.check_output("timedatectl")
    print("IP Address :",ipaddr.decode())
    print(ntp.decode())

while True:
    list_info()
    print("(1 | 2 | 3 | 4 | 5)")
    option = int(input())
    if option == 1:
        hostname_partisi()
    elif option == 2:
        lshw()
    elif option == 3:
        lsusb()
    elif option == 4:
        ntp()
    else:
        break

#def main():
#    hostname_partisi()
#    lshw()
#
#if __name__ == "__main__":
#    main()

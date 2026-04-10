from datetime import datetime
import socket

def risk_level(port, f):
    if port in [21,23,3389]:
        f.write(f"High risk")
    elif port in [22,80]:
        f.write(f"Medium risk")
    elif port in [443]:
        f.write(f"Low risk")
def is_port_open(target_ip,port, f):
    if port ==21:
        f.write(f"FTP service on {target_ip} at {port}\n")
    elif port == 22:
        f.write(f"SSH service on {target_ip} at {port}\n")
    elif port == 23:
        f.write(f"Telnet service on {target_ip} at {port}\n")
    elif port == 80:
        f.write(f"HTTP service on {target_ip}:{port} at \n")
    elif port == 443:
        f.write(f"HTTPS service on {target_ip}:{port} at \n")
    else:
        f.write(f"port {port} on {target_ip} at \n")

target = input("enter ip address")
target_ip = socket.gethostbyname(target)
print(f"scanning {target_ip}")
print("-" * 50)

#file creation 
with open("scan_file.txt", "w") as f:
    f.write(f"scan report- {datetime now()}\n")
    f.write("*" * 50)
    for port in range(1, 100):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.1)
        result = sock.connect_ex((target_ip, port))
        sock.close()

        if result ==0:
            f.write(f"Port {port} is pen at {target_i}....\n")
            is_port_open(target_ip, port, f)
            risk_level(port)
        print("scan complete.")

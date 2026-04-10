from datetime import datetime
import socket
def risk_level(port, f):
    if port in [21,23, 3389]:
        f.write("High risk \n")
    elif port in [22, 80]:
        f.write("Medium risk\n ")
    elif port in [443]:
        f.write("Low risk\n ")

def is_port_open(target_ip, port, f):
    if port == 21:
        f.write(f"  FTP service on {target_ip}:{port} ")
    elif port == 22:
        f.write(f"  SSH service on {target_ip}:{port} at \n")
    elif port == 23:
        f.write(f"  Telnet service on {target_ip}:{port} at \n")
    elif port == 80:
        f.write(f"  HTTP service on {target_ip}:{port} at \n")
    elif port == 443:
        f.write(f"  HTTPS service on {target_ip}:{port} at \n")
    else:
        f.write(f"  port {port} on {target_ip} at \n")
  

target = input("Enter IP address: ")
target_ip = socket.gethostbyname(target)
print(f"Scanning {target_ip}...")
print("-" * 50) 

with open("scan_report.txt", "w") as f:
    f.write(f"Scan Report - {datetime.now()}\n")
    f.write("-" * 50)
    for port in range(1, 1000):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.1)
        result = sock.connect_ex((target_ip, port))
        sock.close()

        # THIS MUST BE INSIDE THE LOOP (INDENTED)
        if result == 0:
             f.write(f"\n Port {port} is open on {target_ip}.....\n")
             is_port_open(target_ip, port, f)
             risk_level(port, f)

print("Scan complete. Report saved to scan_report.txt")   
             
             
            
   
    
    
    






            

        
                
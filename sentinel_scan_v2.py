import socket
import concurrent.futures
import threading
from datetime import datetime

# The 'Lock' ensures only one thread writes to the file at a time
print_lock = threading.Lock()


# ab main add kr raha hu function ko call krne ke liye
def scan_port(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5)
    result= sock.connect_ex((target_ip, port))
    sock.close()

    if result == 0:
        with print_lock:
            with open("scan_reports.txt", "a") as f:
                timestamp = datetime.now().strftime("%H:%M:%S")
                f.write(f"[{timestamp}] Port {port} : OPEN | ")
                is_port_open(port, f)
                risk_level(port, f)

def is_port_open(port, f):
    if port == 21:
        f.write("Service: FTP | ")
    elif port == 22:
        f.write("Service: SSH | ")
    elif port == 23:
        f.write("Service: Telnet | ")
    elif port == 80:
        f.write("Service: HTTP | ")
    elif port == 443:
        f.write("Service: HTTPS | ")
    else:
        f.write("Service: Unknown | ")

def risk_level(port, f):
    if port in [21, 23, 3389]:
        f.write("Risk: High\n")
    elif port in [22, 80]:
        f.write("Risk: Medium\n")
    elif port in [443]:
        f.write("Risk: Low\n")
    else:
        f.write("Risk: Unknown\n")
#step 2 
target = input("Enter IP address or domain: ")
target_ip = socket.gethostbyname(target)
print(f"Scanning {target_ip}...")
#step 3
with open("scan_reports.txt", "w") as f:
    f.write(f"Scan report : {datetime.now()}\n")
    f.write("-" * 50 + "\n")
#step 4
with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
    executor.map(scan_port, range(1, 10000))
print("scan complete. Results saved to scan_reports.txt")

import socket
def is_port_open(target_ip,port):
    if port == 21:
        print("⚠️ FTP detected — file transfer risk")
    elif port == 22:
        print("⚠️ SSH detected — potential remote access risk")
    elif port == 80:
        print("⚠️ HTTP detected — web server")
    elif port == 443:
        print("✅ HTTPS — encrypted web server")   
    else:
        print("No specific risk found for this open port.")
target = input("enter ip address:")
target_ip = socket.gethostbyname(target)
print(f"scanning {target_ip} ...")
print("-" * 50)
#for loop
for port in range(1,1000):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.1)
    result = sock.connect_ex((target_ip, port))
    if result == 0:
        print(f"port {port} is open")
        is_port_open(target_ip, port)
    sock.close()
    
        
#!/usr/bin/env python3
import socket
import json
import threading
from datetime import datetime

# Common ports to scan
COMMON_PORTS = [21, 22, 23, 25, 53, 80, 110, 443, 3306, 3389, 8080, 8443]

# Known services and risk levels
SERVICES = {
    21: {"name": "FTP", "risk": "medium"},
    22: {"name": "SSH", "risk": "medium"},
    23: {"name": "Telnet", "risk": "high"},
    25: {"name": "SMTP", "risk": "low"},
    53: {"name": "DNS", "risk": "medium"},
    80: {"name": "HTTP", "risk": "low"},
    110: {"name": "POP3", "risk": "low"},
    443: {"name": "HTTPS", "risk": "low"},
    3306: {"name": "MySQL", "risk": "medium"},
    3389: {"name": "RDP", "risk": "high"},
    8080: {"name": "HTTP-Alt", "risk": "low"},
    8443: {"name": "HTTPS-Alt", "risk": "low"}
}

def scan_port(ip, port, results, lock):
    """Scan a single port and append result to shared list."""
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(2)
        result = sock.connect_ex((ip, port))
        if result == 0:
            service_info = SERVICES.get(port, {"name": "Unknown", "risk": "unknown"})
            with lock:
                results.append({
                    "ip": ip,
                    "port": port,
                    "status": "open",
                    "service": service_info["name"],
                    "risk": service_info["risk"],
                    "timestamp": datetime.now().isoformat()
                })
        sock.close()
    except Exception:
        pass

def main():
    ip = input("Enter IP address to scan: ")
    results = []
    lock = threading.Lock()
    threads = []

    print(f"Scanning {len(COMMON_PORTS)} ports on {ip}...")
    print("Progress:")

    # Create and start threads
    for port in COMMON_PORTS:
        thread = threading.Thread(target=scan_port, args=(ip, port, results, lock))
        threads.append(thread)
        thread.start()

    # Wait for all threads to complete
    for thread in threads:
        thread.join()

    # Sort results by port number
    results.sort(key=lambda x: x.get("port", 0))

    # Write JSON report
    with open("report.json", "w") as f:
        json.dump(results, f, indent=2)

    print(f"\nScan complete. Found {len(results)} open ports.")
    print("Results saved to report.json")

if __name__ == "__main__":
    main()
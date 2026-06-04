import socket
import sys

def scan_target(target_host, ports=[21, 22, 80, 443, 445]):
    results = []
    for port in ports:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1.0)
        status = s.connect_ex((target_host, port))
        if status == 0:
            results.append({"port": port, "status": "OPEN"})
        else:
            results.append({"port": port, "status": "CLOSED"})
        s.close()
    return results

if __name__ == "__main__":
    host = sys.argv[1] if len(sys.argv) > 1 else "127.0.0.1"
    print(scan_target(host))

import socket

def scan_ports(host, ports=[21, 22, 23, 25, 53, 80, 110, 143, 443, 445, 3389]):
    open_ports = {}
    print(f"[+] Scanning ports on {host}...")
    
    for port in ports:
        try:
            sock = socket.socket()
            sock.settimeout(1)
            result = sock.connect_ex((host, port))
            if result == 0:
                banner = grab_banner(host, port)
                open_ports[port] = banner if banner else "No banner"
            sock.close()
        except Exception as e:
            print(f"[!] Error scanning port {port}: {e}")
    
    return open_ports

def grab_banner(host, port):
    try:
        sock = socket.socket()
        sock.settimeout(2)
        sock.connect((host, port))
        banner = sock.recv(1024).decode().strip()
        sock.close()
        return banner
    except:
        return None

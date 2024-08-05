import socket

def scan(target, ports):
    print('\n' + 'Starting Scan For ' + str(target))
    for port in range(1, ports + 1):
        scan_port(target, port)

def scan_port(ipaddress, port):
    try:
        sock = socket.socket()
        sock.settimeout(1)  # Set a timeout for the connection attempt
        sock.connect((ipaddress, port))
        print(f"[+] Port Opened: {port}")
        sock.close()
    except:
        pass  # Ignore errors for closed ports

targets = input("[*] Enter Targets To Scan (split them by ,): ")
ports = int(input("[*] Enter How Many Ports You Want To Scan: "))

if ',' in targets:
    print("[*] Scanning Multiple Targets")
    for ip_addr in targets.split(','):
        scan(ip_addr.strip(), ports)
else:
    scan(targets.strip(), ports)

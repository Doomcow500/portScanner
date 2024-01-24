import socket

def scan_ports(target, start_port, end_port):
    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target, port))
        if result == 0:
            print(f"Port {port} is open")
        sock.close()

target = "localhost"
start_port = 1
end_port = 65535

scan_ports(target, start_port, end_port)

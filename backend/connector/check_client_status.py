import socket
from typing import Literal, Tuple

HostStatus = Literal["up", "down"]
PortStatus = Literal["open", "closed", "filtered"]

def check_host_and_port(
    client_credentials,
    timeout: float = 3.0
) -> Tuple[HostStatus, PortStatus]:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(timeout)
    try:
        result = sock.connect_ex((client_credentials.node_id,client_credentials.node_port))
        if result == 0:
            return "up", "open"
        elif result == socket.errno.ECONNREFUSED:
            return "up", "closed"
        else:
            return "down", "filtered"
    except socket.gaierror:
        return "down", "filtered"
    except socket.timeout:
        return "down", "filtered"
    finally:
        sock.close()

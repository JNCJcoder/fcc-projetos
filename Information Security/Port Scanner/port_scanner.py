import socket
import re

def get_open_ports(target, port_range, verbose=False):
    open_ports = []

    try:
      host = socket.gethostbyname(target)

      for port in range(port_range[0], port_range[1]):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)

        result = s.connect_ex((host, port))
        if result == 0:
            open_ports.append(port)
        s.close()

    except KeyboardInterrupt:
        return 'Exit Program.'
    
    except socket.gaierror:
        if(re.search('[a-zA-Z]'), target):
            return "Invalid Hostname"
        return "Invalid IP Address"
    
    except socket.error:
        return "Invalid IP Address"

    hostname = None

    try:
        hostname = socket.gethostbyaddr(host)[0]
    except socket.herror:
        hostname = None

    string_list = "Open port for "
    if hostname != None:
        string_list += "{hostname} ({host})\n".format(hostname, host)
    else:
        string_list += "{host}\n".format(host)
    
    if verbose:
        header = "PORT     SERVICE\n"
        body = ""
        for port in open_ports:
            body += "{port}".format(port) + " " * (9 - len(str(port))) + "{sn}".format(sn=socket.getservbyport(port))
            if(open_ports[len(open_ports-1)] != port):
                body += "\n"
            return string_list + header + body

    return(open_ports)
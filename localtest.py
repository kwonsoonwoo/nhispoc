import subprocess
import socket

cmd = "ifconfig ens3 | grep Mask | cut -d: -f 2 | awk '{print$1}'"
result = subprocess.check_output([cmd], shell=True, universal_newlines=True)
soc = socket.gethostbyname(socket.getfqdn())

print(result)
print(soc)
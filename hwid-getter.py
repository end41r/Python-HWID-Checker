import getpass, os, uuid, hashlib
from getmac import get_mac_address as gma
print(hashlib.sha256((os.name + getpass.getuser() + gma() + str(hex(uuid.getnode()))).encode()).hexdigest())

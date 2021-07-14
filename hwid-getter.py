import getpass
import os
from getmac import get_mac_address as gma
import uuid
import hashlib

hwid = os.name + getpass.getuser() + gma() + str(hex(uuid.getnode()))
print(hashlib.sha256(hwid.encode()).hexdigest())


import getpass
import os
from getmac import get_mac_address as gma
import uuid
import hashlib
from requests import get

hwid = os.name + getpass.getuser() + gma() + str(hex(uuid.getnode()))

file = get(url='raw pastebin with hwids goes here')
stripped = file.text[:500]
stripped = stripped.split('\r\n')

x = len(stripped)

for i in range(x):
    if hashlib.sha256(hwid.encode()).hexdigest() == stripped[i]:
        print("ok")

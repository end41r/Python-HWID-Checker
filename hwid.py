import getpass, os, uuid, hashlib
from getmac import get_mac_address as gma
from requests import get
file = get(url='raw pastebin with hwids goes here')
stripped = file.text[:500].split('\r\n')
for i in range(len(stripped)):
    if hashlib.sha256((os.name + getpass.getuser() + gma() + str(hex(uuid.getnode()))).encode()).hexdigest() == stripped[i]: print("ok")

import getpass, os, uuid, hashlib, getmac as gma, requests
file = requests.get(url='raw pastebin with hwids goes here')
stripped = file.text[:500].split('\r\n')
for i in range(len(stripped)):
    if hashlib.sha256((os.name + getpass.getuser() + gma.get_mac_address() + str(hex(uuid.getnode()))).encode()).hexdigest() == stripped[i]: print("ok")

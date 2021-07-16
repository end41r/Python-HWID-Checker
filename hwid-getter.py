import getpass, os, uuid, hashlib, getmac as gma
print(hashlib.sha256((os.name + getpass.getuser() + gma.get_mac_address() + str(hex(uuid.getnode()))).encode()).hexdigest())


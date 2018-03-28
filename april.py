# import library
from netmiko import ConnectHandler

# connection properties described in a dictionary
csr = {
    'device_type': 'cisco_ios',
    'ip': '192.168.252.148',
    'username': 'rancid',
    'password': 'place',
}
# the ** unpacks a dictionary
csr_session = ConnectHandler(**csr)

print(csr_session.send_command('show interfaces description'))


import ipaddress
iplist = ['']
nets = [ipaddress.ip_network(_ip) for _ip in iplist]
cidrs = ipaddress.collapse_addresses(nets)
cidrs = list(cidrs)
cidrs = [_cidr.exploded for _cidr in cidrs]
for _cidr in cidrs:
    print('{}'.format(_cidr))
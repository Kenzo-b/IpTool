import re


def IsIp(ip):
    """check if a string is an IPv4 and return a boolean"""

    pattern = '^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$'
    return re.match(pattern, ip)


def IsMask(mask):
    """check if a string is a mask and return a boolean"""

    pattern = '^(((255\.){3}(255|254|252|248|240|224|192|128|0+))|((255\.){2}(255|254|252|248|240|224|192|128|0+)\.0)|((255\.)(255|254|252|248|240|224|192|128|0+)(\.0+){2})|((255|254|252|248|240|224|192|128|0+)(\.0+){3}))$'
    return re.match(pattern, mask)


def DTB(dec_p):
    """take a decimal pointed form and return it binary pointed form"""

    bin_p = '.'.join([bin(int(octet))[2:].zfill(8) for octet in dec_p.split('.')])
    return bin_p


def BTD(bin_p):
    """take a binary pointed form and return it decimal pointed form"""

    dec_p = '.'.join(str(int(octet, 2)) for octet in bin_p.split('.'))
    return dec_p


def NetIp(ip, mask):
    """Calculate a network IPv4 with an AND operation and return both dec and bin form"""

    str_bin_ip = ''.join(DTB(ip).split('.'))
    str_bin_subnet_mask = ''.join((DTB(mask)).split('.'))

    str_bin_ip = ''.join('1' if str_bin_subnet_mask[i] == '1' and str_bin_ip[i] == '1' else '0' for i in range(0, 32))
    bin_net_ip = '.'.join(str_bin_ip[i:i + 8] for i in range(0, len(str_bin_ip), 8))
    net_ip = BTD(bin_net_ip)

    return net_ip, bin_net_ip


def CIP(ip):

    classe_str = "ABCDE"
    first_octet = DTB(ip).split('.')[0]
    for i in first_octet:
        if i == '0':
            return classe_str[first_octet.index(i)]
        else:
            return classe_str[4]

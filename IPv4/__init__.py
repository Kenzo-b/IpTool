import re


def IsIp(ip):
    """check if a string is an IPv4 and return a boolean"""

    pattern = '^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$'
    return re.match(pattern, ip)


def IsCidr(cidr):
    """check if a string is a CIDR and return a boolean"""

    pattern = "^(/(3[0-2]|2[0-9]|1[0-9]|[1-9]))$"
    return re.match(cidr, pattern)


def IsMask(mask):
    """check if a string is a mask and return a boolean"""

    pattern = '^(((255\.){3}(255|254|252|248|240|224|192|128|0+))|((255\.){2}(255|254|252|248|240|224|192|128|0+)\.0)|((255\.)(255|254|252|248|240|224|192|128|0+)(\.0+){2})|((255|254|252|248|240|224|192|128|0+)(\.0+){3}))$'
    return re.match(pattern, mask)


def DTB(dec_p: str):
    """take a decimal pointed form and return it binary pointed form -> bin.bin.bin.bin"""

    bin_p = '.'.join([bin(int(octet))[2:].zfill(8) for octet in dec_p.split('.')])
    return bin_p


def BTD(bin_p: str):
    """take a binary pointed form and return it decimal pointed form -> dec.dec.dec.dec"""

    dec_p = '.'.join(str(int(octet, 2)) for octet in bin_p.split('.'))
    return dec_p


def NetIp(ip: str, mask: str):
    """Calculate a network IPv4 with an AND operation and return both dec and bin form
    -> bin.bin.bin.bin <=> dec.dec.dec.dec"""

    str_bin_ip = ''.join(DTB(ip).split('.'))
    str_bin_subnet_mask = ''.join((DTB(mask)).split('.'))

    str_bin_ip = ''.join('1' if str_bin_subnet_mask[i] == '1' and str_bin_ip[i] == '1' else '0' for i in range(0, 32))
    bin_net_ip = '.'.join(str_bin_ip[i:i + 8] for i in range(0, len(str_bin_ip), 8))
    net_ip = BTD(bin_net_ip)

    return net_ip, bin_net_ip


def CIP(ip: str):
    """take a dec ip and return the char of it ip classe -> "X" """

    classe_str = "ABCDE"
    first_octet = DTB(ip).split('.')[0]
    for i in first_octet:
        if i == '0':
            return classe_str[first_octet.index(i)]
        else:
            return classe_str[4]


def CITBM(cidr: str):
    """take a cidr notation string and return a binary mask string -> bin.bin.bin.bin"""

    o_bit_nb = int(cidr.split("/")[1])
    z_bit_nb = 32 - int(o_bit_nb)
    str_bin_mask = "" + "1" * o_bit_nb + "0" * z_bit_nb
    bin_mask = ".".join(str_bin_mask[i:i + 8] for i in range(0, len(str_bin_mask), 8))
    return bin_mask


def CTBM(classe_ip: chr):
    """take an ip classe and return a binary mask string -> bin.bin.bin.bin"""

    classe = {"A": 8, "B": 16, "C": 24, "D": 28, "E": 28}
    for key, value in classe.items():
        if classe_ip == key:
            str_bin_mask = "" + "1" * value + "0" * (32 - value)
            bin_mask = ".".join(str_bin_mask[i:i + 8] for i in range(0, len(str_bin_mask), 8))
            return bin_mask


def BrdIp(ip: str, mask: str):
    """take an ip str and a mask str and return a broadcast ip string -> int.int.int.int"""

    str_bin_mask = "".join(DTB(mask).split('.'))
    str_bin_ip = "".join(DTB(ip).split('.'))

    broadcast_address = ""
    for i in range(len(str_bin_mask)):
        if str_bin_mask[i] == "0":
            broadcast_address += "1"
        else:
            broadcast_address += str_bin_ip[i]

    broadcast_ip = ".".join([str(int(broadcast_address[i:i + 8], 2)) for i in range(0, 32, 8)])

    return broadcast_ip


def NbHost(mask: str):
    """take a mask string and return number of host possible integer"""

    str_bin_mask = "".join(DTB(mask).split('.'))

    return 2 ** len(str_bin_mask[str_bin_mask.find("0"):len(str_bin_mask)]) - 2


def NbSR(mask1: str, mask2: str):

    mask1 = "".join(DTB(mask1).split('.'))
    mask2 = "".join(DTB(mask2).split('.'))

    if int(mask1) > int(mask2):

        last_ind = int("".join(str(mask1.find("0"))))
        first_ind = int("".join(str(mask2.find("0"))))

        return 2 ** (last_ind - first_ind)

    elif int(mask1) < int(mask2):

        last_ind = int("".join(str(mask2.find("0"))))
        first_ind = int("".join(str(mask1.find("0"))))

        return 2 ** (last_ind - first_ind)

    elif int(mask1) == int(mask2):

        return 0

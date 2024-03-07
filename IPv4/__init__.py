import re


def is_ip(ip):
    """check if a string is an IPv4 and return a boolean"""

    pattern = '^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$'
    return re.match(pattern, ip)


class IpFormatError(Exception):
    def __init__(self):
        self.Error = "IpFormatError : string value is not an IPv4, it must be -> n.n.n.n"


def is_cidr(cidr):
    """check if a string is a CIDR and return a boolean"""

    pattern = "^(/(3[0-2]|2[0-9]|1[0-9]|[1-9]))$"
    return re.match(cidr, pattern)


class CidrFormatError(Exception):
    def __init__(self):
        self.Error = "CidrFormatError : string value is not a Cidr, it must be -> /n"


def is_mask(mask):
    """check if a string is a mask and return a boolean"""

    pattern = '^(((255\.){3}(255|254|252|248|240|224|192|128|0+))|((255\.){2}(255|254|252|248|240|224|192|128|0+)\.0)|((255\.)(255|254|252|248|240|224|192|128|0+)(\.0+){2})|((255|254|252|248|240|224|192|128|0+)(\.0+){3}))$'
    return re.match(pattern, mask)


class MaskFormatError(Exception):
    def __init__(self):
        self.Error = "MaskFormatError : string value is not a mask, it must be -> n.n.n.n"


def dec_to_bin(dec_p: str):
    """take a decimal pointed form and return it binary pointed form -> bin.bin.bin.bin"""

    bin_p = '.'.join([bin(int(octet))[2:].zfill(8) for octet in dec_p.split('.')])
    return bin_p


def bin_to_dec(bin_p: str):
    """take a binary pointed form and return it decimal pointed form -> dec.dec.dec.dec"""

    dec_p = '.'.join(str(int(octet, 2)) for octet in bin_p.split('.'))
    return dec_p


def net_ip(ip: str, mask: str):
    """Calculate a network IPv4 with an AND operation and return both dec and bin form
    -> bin.bin.bin.bin  dec.dec.dec.dec"""

    str_bin_ip = ''.join(dec_to_bin(ip).split('.'))
    str_bin_subnet_mask = ''.join((dec_to_bin(mask)).split('.'))

    str_bin_ip = ''.join('1' if str_bin_subnet_mask[i] == '1' and str_bin_ip[i] == '1' else '0' for i in range(0, 32))

    return bin_to_dec(str_to_dotted(str_bin_ip)), str_to_dotted(str_bin_ip)


def class_ip(ip: str):
    """take a dec ip and return the char of it ip classe -> "X" """

    classe_str = "ABCDE"
    first_octet = dec_to_bin(ip).split('.')[0]
    for i in first_octet:
        if i == '0':
            return classe_str[first_octet.index(i)]
        else:
            return classe_str[4]


def cidr_to_bin_mask(cidr: str):
    """take a cidr notation string and return a binary mask string -> bin.bin.bin.bin"""

    o_bit_nb = int(cidr.split("/")[1])
    str_bin_mask = "" + "1" * o_bit_nb + "0" * (32 - o_bit_nb)

    return str_to_dotted(str_bin_mask)


def class_to_bin_mask(classe_ip: chr):
    """take an ip classe and return a binary mask string -> bin.bin.bin.bin"""

    classe = {"A": 8, "B": 16, "C": 24, "D": 28, "E": 28}
    for key, value in classe.items():
        if classe_ip == key:
            str_bin_mask = "" + "1" * value + "0" * (32 - value)
            return str_to_dotted(str_bin_mask)


def bin_str_dec_dotted(str_bin: str):

    return ".".join([str(int(str_bin[i:i + 8], 2)) for i in range(0, len(str_bin), 8)])


def str_to_dotted(str_format):

    return ".".join([str(int(str_format[i:i + 8])) for i in range(0, len(str_format), 8)])


def brd_ip(ip: str, mask: str):
    """take an ip str and a mask str and return a broadcast ip string -> int.int.int.int"""

    str_bin_mask = "".join(dec_to_bin(mask).split('.'))
    str_bin_ip = "".join(dec_to_bin(ip).split('.'))

    broadcast_address = ""
    for i in range(len(str_bin_mask)):
        if str_bin_mask[i] == "0":
            broadcast_address += "1"
        else:
            broadcast_address += str_bin_ip[i]

    broadcast_ip = ".".join([str(int(broadcast_address[i:i + 8], 2)) for i in range(0, 32, 8)])

    return broadcast_ip


def nb_host(mask: str):
    """take a mask string and return number of host possible integer"""

    str_bin_mask = "".join(dec_to_bin(mask).split('.'))

    return 2 ** len(str_bin_mask[str_bin_mask.find("0"):len(str_bin_mask)]) - 2


def nb_subnet(mask1: str, mask2: str):
    """take to mask format str and return the number of subnet that can be made with those masks as an int"""

    if is_mask(mask1) and is_mask(mask2):
        mask1 = "".join(dec_to_bin(mask1).split('.'))
        mask2 = "".join(dec_to_bin(mask2).split('.'))
    else:
        raise MaskFormatError

    if int(mask1) > int(mask2):

        return 2 ** (mask1.find("0") - mask2.find("0"))

    elif int(mask1) < int(mask2):

        return 2 ** (mask2.find("0") - mask1.find("0"))

    elif int(mask1) == int(mask2):

        return 0


def addr_range(ip: str, mask: str):
    """take an ip and a mask format string and return a list -> [net_ip, broadcast_ip]"""

    if is_ip(ip) is False:
        raise IpFormatError
    if is_mask(mask) is False:
        raise MaskFormatError

    return [net_ip(ip, mask)[0], brd_ip(ip, mask)]


def all_addr_range(ip: str, mask1: str, mask2: str):
    """take an ip and 2 mask format string and return all the subnet range in a list -> [[net_ip, broadcast_ip], ...]"""

    if is_ip(ip) is False:
        raise IpFormatError
    if is_mask(mask1) and is_mask(mask2) is False:
        raise MaskFormatError

    ip_bin = "".join(dec_to_bin(ip).split('.'))
    mask1_bin = "".join(dec_to_bin(mask1).split('.'))
    mask2_bin = "".join(dec_to_bin(mask2).split('.'))
    subnet = nb_subnet(mask1, mask2)
    counter = 0
    addr_ran_list = []

    if int(mask1_bin, 2) > int(mask2_bin, 2):

        last_ind = mask1_bin.find("0")
        first_ind = mask2_bin.find("0")

        while counter < subnet:

            ip_bin = ip_bin[:first_ind] + bin(counter)[2:].zfill(last_ind - first_ind) + ip_bin[last_ind:]
            modified_ip = bin_str_dec_dotted(ip_bin)
            addr_ran_list.append(addr_range(modified_ip, mask1))
            counter += 1

    elif int(mask1_bin, 2) < int(mask2_bin, 2):

        last_ind = mask2_bin.find("0")
        first_ind = mask1_bin.find("0")

        while counter < subnet:

            ip_bin = ip_bin[:first_ind] + bin(counter)[2:].zfill(last_ind - first_ind) + ip_bin[last_ind:]
            modified_ip = bin_str_dec_dotted(ip_bin)
            addr_ran_list.append(addr_range(modified_ip, mask2))
            counter += 1

    return addr_ran_list

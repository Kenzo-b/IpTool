import IPv4


def user_friendly_name(name):
    def decorator(func):
        func.user_friendly_name = name
        return func

    return decorator


class Ipv4:

    last_id = 0

    def __init__(self, ip: str, mask: str, last_id):
        self.ip = self.verif_ip(ip)
        self.mask = self.verif_mask(mask)
        last_id += 1
        self.id = last_id
        self.classe_ip = IPv4.class_ip(self.ip)

    def get_ip(self):
        return self.ip

    def get_mask(self):
        return self.mask

    def get_classe(self):
        return self.classe_ip

    def set_ip(self, ip):
        self.ip = self.verif_ip(ip)

    def set_mask(self, mask):
        self.mask = self.verif_mask(mask)

    @staticmethod
    def verif_ip(ip):
        if IPv4.is_ip(ip):
            return ip
        else:
            raise IPv4.IpFormatError

    @staticmethod
    def verif_mask(mask):
        if IPv4.is_mask(mask):
            return mask
        else:
            raise IPv4.MaskFormatError

    @staticmethod
    def verif_cidr(cidr):
        if IPv4.is_cidr(cidr):
            return cidr
        else:
            raise IPv4.CidrFormatError

    @user_friendly_name("binary ip")
    def dec_to_bin_ip(self):
        return IPv4.dec_to_bin(self.ip)

    @user_friendly_name("binary mask")
    def dec_to_bin_mask(self):
        return IPv4.dec_to_bin(self.mask)

    @user_friendly_name("network ip")
    def calc_net_ip(self):
        return IPv4.net_ip(self.ip, self.mask)

    @user_friendly_name("broadcast ip")
    def calc_brd_ip(self):
        return IPv4.brd_ip(self.ip, self.mask)

    @user_friendly_name("number of host")
    def calc_nb_host(self):
        return IPv4.nb_host(self.mask)

    @user_friendly_name("number of subnet")
    def calc_nb_subnet(self, mask2):
        return IPv4.nb_subnet(self.mask, mask2)

    @user_friendly_name("Addressing range")
    def calc_addr_range(self):
        return IPv4.addr_range(self.ip, self.mask)

    @user_friendly_name("Subnet addressing ranges")
    def calc_all_addr_range(self, mask2):
        return IPv4.all_addr_range(self.ip, self.mask, mask2)

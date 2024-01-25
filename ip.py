import IPv4


class ipv4:

    last_id = 0

    def __init__(self, ip, mask, last_id):
        self.ip = self.verif_ip(ip)
        self.mask = self.verif_mask(mask)
        last_id += 1
        self.id = last_id
        self.classe_ip = IPv4.CIP(self.ip)

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
        if IPv4.IsIp(ip):
            return ip
        else:
            raise IpFormatError

    @staticmethod
    def verif_mask(mask):
        if IPv4.IsMask(mask):
            return mask
        else:
            raise MaskFormatError

    def dec_to_bin_ip(self):
        return IPv4.DTB(self.ip)

    def dec_to_bin_mask(self):
        return IPv4.DTB(self.mask)

    def calc_net_ip(self):
        return IPv4.NetIp(self.ip, self.mask)


class IpFormatError(Exception):
    def __init__(self):
        self.Error = "IpFormatError : string value is not an IPv4"


class MaskFormatError(Exception):
    def __init__(self):
        self.Error = "MaskFormatError : string value is not a mask"

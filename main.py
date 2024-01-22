import os


from ip import *


IPtool_ind = "IPtool > "


def i_obj_ip():
    try:
        ip = input("{}enter an IPv4 adresse : ".format(IPtool_ind))
        mask = input("{}enter a mask : ".format(IPtool_ind))
        obj_ip = ipv4(ip, mask, ipv4.last_id)
        return obj_ip
    except (IpFormatError, MaskFormatError):
        i_obj_ip()


def help(null=0):
    return("0 - get help\n1 - clear\n2 - IPv4 to binary\n3 - mask to binary\n4 - net IPv4 calculation")


def clear(null=0):
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def main():
    obj_ip = i_obj_ip()
    cmds = {"0": help, "1": clear, "2": ipv4.dec_to_bin_ip, "3": ipv4.dec_to_bin_mask, "4": ipv4.calc_net_ip}
    print(help())
    while True:
        response = input("IPtools > ")
        try:
            for key, value in cmds.items():
                if response == key:
                    function = cmds[key]
                    result = function(obj_ip)
                    print(result)

        except Exception as e:
            print(e)


main()

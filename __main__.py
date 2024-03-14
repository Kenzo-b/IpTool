import os
from ip import *
from GUI import *
import sys

IPtool_ind = "IPtools> "


def i_obj_ip():
    try:
        ip = input("{}enter an IPv4 address : ".format(IPtool_ind))
        mask = input("{}enter a mask : ".format(IPtool_ind))
        obj_ip = Ipv4(ip, mask)
        return obj_ip
    except (IPv4.IpFormatError, IPv4.MaskFormatError):
        i_obj_ip()


def help(cmds: dict):
    help_print = "".join("{} - {}\n".format(key, value.user_friendly_name if hasattr(value, 'user_friendly_name')else value.__name__) for key, value in cmds.items())
    return help_print


def clear(null=0):
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def cli_main():

    obj_ip = i_obj_ip()

    cmds = {"0": help, "1": clear, "2": Ipv4.dec_to_bin_ip, "3": Ipv4.dec_to_bin_mask, "4": Ipv4.calc_net_ip,
            "5": Ipv4.calc_brd_ip, "6": Ipv4.calc_nb_host, "7": Ipv4.calc_nb_subnet, "8": Ipv4.calc_addr_range,
            "9": Ipv4.calc_all_addr_range}

    print(help(cmds))
    while True:
        response = input("{}".format(IPtool_ind))
        try:

            for key, value in cmds.items():
                function = cmds[key]

                if response == key:

                    if key == "0":
                        print(help(cmds))

                    if key == "7" or key == "9":
                        mask2 = input("{}enter the second mask : ".format(IPtool_ind))

                        if IPv4.is_mask(mask2):

                            result = function(obj_ip, mask2)
                            print("\n".join("{} -> {}".format(result[i][0], result[i][1]) for i in range(len(result))))

                        else:
                            raise IPv4.MaskFormatError
                    else:
                        result = function(obj_ip)
                        print(result)

        except Exception as e:
            print(e)


if __name__ == "__main__":
    try:
        if len(sys.argv) > 1:
            for arg in sys.argv:
                if arg == "-c":
                    cli_main()
                if arg == "-g":
                    gui_main()
        else:
            cli_main()
    except KeyboardInterrupt:
        sys.exit()

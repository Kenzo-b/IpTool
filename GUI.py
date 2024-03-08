from customtkinter import *
from ip import *



def gui_main():

    root_tk = CTk()
    root_tk.title("IpTools")
    root_tk.geometry("500x400")

    ip_label = CTkLabel(master=root_tk, text="enter an ip address :")
    ip_label.pack(anchor="w", padx=10)
    ip_entry = CTkEntry(master=root_tk, placeholder_text="172.0.0.1")
    ip_entry.pack(anchor="w", padx=10)

    mask_label = CTkLabel(master=root_tk, text="enter a mask :")
    mask_label.pack(anchor="w", padx=10)
    mask_entry = CTkEntry(master=root_tk, placeholder_text="255.255.0.0")

    mask_entry.pack(anchor="w", padx=10)

    enter_btn = CTkButton(master=root_tk, text="enter")


    def i_obj_ip():
        if ip_entry.get() != "" and mask_entry.get() != "":
            try:
                ip = ip_entry.get()
                mask = mask_entry.get()
                obj_ip = Ipv4(ip, mask, Ipv4.last_id)
                return obj_ip
            except (IPv4.IpFormatError, IPv4.MaskFormatError):
                i_obj_ip()
        else:
            return

    enter_btn.pack(command=i_obj_ip())
    obj_ip = enter_btn.cget("command")
    func_frame = CTkScrollableFrame(master=root_tk)
    func_frame.pack(anchor="e")



    func1_btn = CTkButton(master=func_frame, text="decimal to binary")

    def test(self):
        print(mask_entry.get())
        if mask_entry.get() != "" and ip_entry.get() != "":
            func1_btn.pack()
        elif mask_entry.get() == "" or ip_entry.get() == "":
            print("test")
            func1_btn.forget()


    for i in range(10):
        mask_entry.bind(sequence="{}".format(i), command=test, add=True)
        ip_entry.bind(sequence="{}".format(i), command=test, add=True)

    root_tk.mainloop()


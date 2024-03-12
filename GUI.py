from customtkinter import *
from ctypes import windll
from BlurWindow.blurWindow import blur

import ip
from ip import *


def gui_main():

    root_tk = CTk()
    root_tk.title("IpTools")
    root_tk.geometry("500x400")
    root_tk.resizable(False, False)
    root_tk.config(bg="green")
    root_tk.wm_attributes("-transparent", 'green')
    root_tk.update()

    def color():
        hwnd = windll.user32.GetForegroundWindow()
        blur(hwnd, hexColor=False)

    color()

    top_frame = CTkFrame(master=root_tk, fg_color="transparent")
    top_frame.grid_columnconfigure(1, weight=1)
    top_frame.grid_rowconfigure(1, weight=1)
    top_frame.configure(bg_color="green")

    entry_frame = CTkFrame(master=top_frame,bg_color="green", corner_radius=15, border_color="grey", border_width=2)

    ip_label = CTkLabel(master=entry_frame, text="enter an ip address :")

    ip_entry = CTkEntry(master=entry_frame, placeholder_text="172.0.0.1")

    mask_label = CTkLabel(master=entry_frame, text="enter a mask :")

    mask_entry = CTkEntry(master=entry_frame, placeholder_text="255.255.0.0")

    mask2_label = CTkLabel(master=entry_frame, text="enter a second mask (optional) :")

    mask2_entry = CTkEntry(master=entry_frame, placeholder_text="255.255.192.0")

    OBJ_ip : ip.Ipv4

    def i_obj_ip():
        if mask_entry.get() != "" and ip_entry.get() != "":
            try:
                ip = ip_entry.get()
                mask = mask_entry.get()
                obj_ip = Ipv4(ip, mask)
                return obj_ip
            except (IPv4.IpFormatError, IPv4.MaskFormatError):
                enter_error_label.configure(text="wrong values")
        else:
            enter_error_label.configure(text="empty entry")

    enter_btn = CTkButton(master=entry_frame, text="enter")

    enter_error_label = CTkLabel(master=entry_frame, text="")

    func_frame = CTkScrollableFrame(master=top_frame)

    response_frame = CTkScrollableFrame(master=root_tk, bg_color="green", width=450)
    response_frame.grid_columnconfigure(0, weight=1)

    response_label = CTkLabel(master=response_frame, text="result :", padx=10, pady=10)

    response_value_label = CTkLabel(master=response_frame, text="")


    def func1_btn_handler():
        if mask_entry.get() != "" and ip_entry.get() != "":
            response_value_label.configure(text=Ipv4.dec_to_bin_ip(i_obj_ip()))

    def func2_btn_handler():
        if mask_entry.get() != "" and ip_entry.get() != "":
            response_value_label.configure(text=Ipv4.dec_to_bin_mask(i_obj_ip()))

    def func3_btn_handler():
        if mask_entry.get() != "" and ip_entry.get() != "":
            response_value_label.configure(text=Ipv4.calc_net_ip(i_obj_ip())[0])

    def func4_btn_handler():
        response_value_label.configure(text=Ipv4.calc_brd_ip(i_obj_ip()))

    def func5_btn_handler():
        response_value_label.configure(text=Ipv4.calc_nb_host(i_obj_ip()))

    def func6_btn_handler():
        if mask2_entry.get() != "":
            response_value_label.configure(text=Ipv4.calc_nb_subnet(i_obj_ip(), mask2_entry.get()))

    def func7_btn_handler():
        response_value_label.configure(text=Ipv4.calc_addr_range(i_obj_ip()))

    def func8_btn_handler():
        if mask2_entry.get() != "":
            response_value_label.configure(text=Ipv4.calc_all_addr_range(i_obj_ip(), mask2_entry.get()))

    func_btn_width = 100

    func1_btn = CTkButton(master=func_frame, text="decimal to binary ip", command=func1_btn_handler, width=func_btn_width)

    func2_btn = CTkButton(master=func_frame, text="decimal to binary mask", command=func2_btn_handler, width=func_btn_width)

    func3_btn = CTkButton(master=func_frame, text="network ip", command=func3_btn_handler, width=func_btn_width)

    func4_btn = CTkButton(master=func_frame, text="broadcast ip", command=func4_btn_handler, width=func_btn_width)

    func5_btn = CTkButton(master=func_frame, text="host number", command=func5_btn_handler, width=func_btn_width)

    func6_btn = CTkButton(master=func_frame, text="number of subnet", command=func6_btn_handler, width=func_btn_width)

    func7_btn = CTkButton(master=func_frame, text="addressing range", command=func7_btn_handler, width=func_btn_width)

    func8_btn = CTkButton(master=func_frame, text="subnet addressing range", command=func8_btn_handler, width=func_btn_width)

    def test(self):
        print(mask_entry.get())
        if mask_entry.get() != "" and ip_entry.get() != "":
            func1_btn.pack(pady=10)
            func2_btn.pack(pady=10)
            func3_btn.pack(pady=10)
            func4_btn.pack(pady=10)
            func5_btn.pack(pady=10)
            func6_btn.pack(pady=10)
            func7_btn.pack(pady=10)
            func8_btn.pack(pady=10)
        elif mask_entry.get() == "" or ip_entry.get() == "":
            print("test")
            func1_btn.forget()

    for i in range(10):
        mask_entry.bind(sequence="{}".format(i), command=test, add=True)
        ip_entry.bind(sequence="{}".format(i), command=test, add=True)

    top_frame.grid(row=0, sticky="nsew")
    entry_frame.grid(row=0, column=0, sticky="nw", padx=10, pady=10)
    ip_label.pack(anchor="w", padx=10, pady=10)
    ip_entry.pack(anchor="w", padx=10)
    mask_label.pack(anchor="w", padx=10)
    mask_entry.pack(anchor="w", padx=10)
    mask2_label.pack(anchor="w", padx=10)
    mask2_entry.pack(anchor="w", padx=10)
    enter_btn.pack(anchor="w", padx=10, pady=10)
    enter_error_label.pack(padx=10)
    func_frame.grid(row=0, column=1, sticky="ne", padx=10, pady=10)
    response_frame.grid(row=1, padx=10, pady=10, sticky="new")
    response_label.pack()
    response_value_label.pack()

    root_tk.mainloop()


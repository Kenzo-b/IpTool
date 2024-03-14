from customtkinter import *
from ctypes import windll
from BlurWindow.blurWindow import blur
import subprocess
from ip import *


def gui_main():

    root_tk = CTk()
    root_tk.title("IpTools")
    root_tk.geometry("500x510")
    root_tk.resizable(False, False)
    root_tk.config(bg="green")
    root_tk.wm_attributes("-transparent", 'green')
    root_tk.update()

    def color():
        hwnd = windll.user32.GetForegroundWindow()
        blur(hwnd, hexColor=False)

    if os.name == "nt":
        color()
    if os.name == "posix":
        # Enable transparency for Linux
        root_tk.wait_visibility(root_tk)
        root_tk.wm_attributes("-alpha", 0.9)
        subprocess.Popen(['compton', '--backend', 'glx', '--blur-background', '--blur-method', 'gaussian'])

    top_frame = CTkFrame(master=root_tk, fg_color="transparent")
    top_frame.grid_columnconfigure(1, weight=1)
    top_frame.grid_rowconfigure(1, weight=1)
    top_frame.configure(bg_color="green")

    entry_frame = CTkFrame(master=top_frame,bg_color="green", corner_radius=15, border_color="#2c8cbf", border_width=2)

    ip_label = CTkLabel(master=entry_frame, text="ip address :")

    ip_entry = CTkEntry(master=entry_frame, placeholder_text="172.0.0.1")

    mask_label = CTkLabel(master=entry_frame, text="mask :")

    mask_entry = CTkEntry(master=entry_frame, placeholder_text="255.255.0.0")

    mask2_label = CTkLabel(master=entry_frame, text="second mask (optional) :")

    mask2_entry = CTkEntry(master=entry_frame, placeholder_text="255.255.192.0")

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

    enter_error_label = CTkLabel(master=entry_frame, text="")

    func_frame = CTkScrollableFrame(master=top_frame, bg_color="green", corner_radius=15, border_color="#2c8cbf",
                                    border_width=2, scrollbar_button_color="#2c8cbf",
                                    scrollbar_button_hover_color="#2c8cbf")

    response_frame = CTkScrollableFrame(master=root_tk, bg_color="green",height=10, width=425, corner_radius=15,
                                        border_color="#2c8cbf", border_width=2, scrollbar_button_color="#2c8cbf",
                                        scrollbar_button_hover_color="#2c8cbf")

    response_frame.grid_columnconfigure(0, weight=1)

    response_label = CTkLabel(master=response_frame, text="result :", padx=10, pady=10)

    response_value_label = CTkLabel(master=response_frame, text="")

    def func1_btn_handler():
        response_value_label.configure(text=Ipv4.dec_to_bin_ip(i_obj_ip()))

    def func2_btn_handler():
        response_value_label.configure(text=Ipv4.dec_to_bin_mask(i_obj_ip()))

    def func3_btn_handler():
        response_value_label.configure(text=Ipv4.calc_net_ip(i_obj_ip())[0])

    def func4_btn_handler():
        response_value_label.configure(text=Ipv4.calc_brd_ip(i_obj_ip()))

    def func5_btn_handler():
        response_value_label.configure(text=Ipv4.calc_nb_host(i_obj_ip()))

    def func6_btn_handler():
        if mask2_entry.get() != "":
            response_value_label.configure(text=Ipv4.calc_nb_subnet(i_obj_ip(), mask2_entry.get()))
        else:
            enter_error_label.configure(text="second mask empty/wrong")

    def func7_btn_handler():
        response_value_label.configure(text=Ipv4.calc_addr_range(i_obj_ip()))

    def func8_btn_handler():
        if mask2_entry.get() != "":
            result = Ipv4.calc_all_addr_range(i_obj_ip(), mask2_entry.get())
            response_value_label.configure(text="\n".join("{} -> {}".format(result[i][0], result[i][1]) for i in range(len(result))))
        else:
            enter_error_label.configure(text="second mask empty/wrong")

    func_btn_width = 100

    func1_btn = CTkButton(master=func_frame, text="decimal to binary ip", command=func1_btn_handler,
                          width=func_btn_width, fg_color="#2c8cbf")

    func2_btn = CTkButton(master=func_frame, text="decimal to binary mask", command=func2_btn_handler,
                          width=func_btn_width, fg_color="#2c8cbf")

    func3_btn = CTkButton(master=func_frame, text="network ip", command=func3_btn_handler, width=func_btn_width,
                          fg_color="#2c8cbf")

    func4_btn = CTkButton(master=func_frame, text="broadcast ip", command=func4_btn_handler, width=func_btn_width,
                          fg_color="#2c8cbf")

    func5_btn = CTkButton(master=func_frame, text="host number", command=func5_btn_handler, width=func_btn_width,
                          fg_color="#2c8cbf")

    func6_btn = CTkButton(master=func_frame, text="number of subnet", command=func6_btn_handler, width=func_btn_width,
                          fg_color="#2c8cbf")

    func7_btn = CTkButton(master=func_frame, text="addressing range", command=func7_btn_handler, width=func_btn_width,
                          fg_color="#2c8cbf")

    func8_btn = CTkButton(master=func_frame, text="subnet addressing range", command=func8_btn_handler,
                          width=func_btn_width, fg_color="#2c8cbf")

    func_btn_list = [func1_btn, func2_btn, func3_btn, func4_btn, func5_btn, func6_btn, func7_btn, func8_btn]

    def show_func_btn(self):
        if ip_entry.get() != "" and mask_entry.get() != "":
            for i in range(len(func_btn_list)):
                func_btn_list[i].grid(row=i, pady=10, sticky="nsew")
        elif mask_entry.get() == "" or ip_entry.get() == "":
            for i in range(len(func_btn_list)):
                func_btn_list[i].forget()

    for i in range(1):
        mask_entry.bind(sequence="{}".format(i), command=show_func_btn, add=True)
        ip_entry.bind(sequence="{}".format(i), command=show_func_btn, add=True)

    top_frame.grid(row=0, sticky="nsew")
    entry_frame.grid(row=0, column=0, sticky="nsw", padx=15, pady=10)
    ip_label.pack(anchor="w", padx=10, pady=10)
    ip_entry.pack(anchor="w", padx=10)
    mask_label.pack(anchor="w", padx=10)
    mask_entry.pack(anchor="w", padx=10)
    mask2_label.pack(anchor="w", padx=10)
    mask2_entry.pack(anchor="w", padx=10)

    enter_error_label.pack(padx=10)
    func_frame.grid(row=0, column=1, sticky="nse", padx=15, pady=10)
    response_frame.grid(row=1, padx=15, pady=10, sticky="new")
    response_label.pack(anchor="w")
    response_value_label.pack()

    root_tk.mainloop()


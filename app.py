import create_salt
import tkinter
import customtkinter

#sul = create_salt.generate_salt()
#print(sul)

#UI
customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("blue")


UI_main = customtkinter.CTk()
UI_main.geometry("520x720")
UI_main.title("CryptoMessage")
title_text = customtkinter.CTkLabel(UI_main,text="CryptoMessage",anchor="center",font=("Arial",30),pady=40)
title_text.pack()
main_UI_frame = customtkinter.CTkFrame(master=UI_main,width=260,height=360)

main_UI_frame.pack(anchor="sw",padx=20)

def login_page():


    username_text = customtkinter.CTkLabel(UI_main, text="username: ")
    password_text = customtkinter.CTkLabel(UI_main, text="password: ")
    username_input = customtkinter.CTkEntry(master=UI_main,width=320,height=30,corner_radius=10)
    password_input = customtkinter.CTkEntry(master=UI_main,width=320,height=30,corner_radius=10)
    username_input.pack(padx=5,pady=5)
    username_text.pack(padx=5,pady=5)
    password_input.pack(padx=5,pady=5)
    password_text.pack(padx=5,pady=5)

UI_main.mainloop()
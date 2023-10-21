import create_salt
import tkinter
import customtkinter
from my_sqlalchemy import session,User
import bcrypt
import UI_scripts
from db_utils import delete_account

# UI
customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("blue")

UI_main = customtkinter.CTk()
UI_main.geometry("520x720")
UI_main.title("CryptoMessage")

UI_scripts.register_page(UI_main)

UI_main.mainloop()
#print_users()
session.close()
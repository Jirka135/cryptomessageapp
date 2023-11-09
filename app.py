import customtkinter
from my_sqlalchemy import session,User
import UI_scripts
from db_utils import delete_account,get_usernames
from icecream import ic


# UI

def main_loop():
    customtkinter.set_appearance_mode("Dark")
    customtkinter.set_default_color_theme("blue")

    UI_main = customtkinter.CTk()
    UI_main.geometry("520x720")
    UI_main.title("CryptoMessage")

    #UI_scripts.main_page(UI_main)
    UI_scripts.register_page(UI_main)

    UI_main.mainloop()
    session.close()



if __name__ == "__main__":
    main_loop() 
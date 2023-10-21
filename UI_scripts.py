import tkinter
import customtkinter
import bcrypt
from db_utils import create_account_in_db,check_login,get_usernames,get_emails
from other_utils import check_password_strength,is_valid_email,is_valid_username
from icecream import ic

def title(UI_main):
    title_text = customtkinter.CTkLabel(UI_main, text="CryptoMessage", anchor="center", font=("Arial", 30), pady=40)
    title_text.pack()

def clear_ui(UI_main):
    for widget in UI_main.winfo_children():
        widget.destroy()

def register_page(UI_main):

    clear_ui(UI_main)
    title(UI_main)
    main_UI_frame = customtkinter.CTkFrame(UI_main)
    main_UI_frame.pack(anchor="center", padx=20)

    username_text = customtkinter.CTkLabel(main_UI_frame, text="Username:")
    email_text = customtkinter.CTkLabel(main_UI_frame, text="Email:")
    password_text = customtkinter.CTkLabel(main_UI_frame, text="Password:")
    username_input = customtkinter.CTkEntry(main_UI_frame, width=300, corner_radius=10)
    email_input = customtkinter.CTkEntry(main_UI_frame, width=300, corner_radius=10)
    password_input = customtkinter.CTkEntry(main_UI_frame, width=300, corner_radius=10, show="*")
    register_status_text = customtkinter.CTkLabel(main_UI_frame, text="")

    username_text.grid(row=0, column=0, padx=5, pady=5)
    email_text.grid(row=1, column=0, padx=5, pady=5)
    password_text.grid(row=2, column=0, padx=5, pady=5)
    username_input.grid(row=0, column=1, padx=5, pady=5)
    email_input.grid(row=1, column=1, padx=5, pady=5)
    password_input.grid(row=2, column=1, padx=5, pady=5)
    register_status_text.grid(row=3, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")

    def check_password():
        password = password_input.get()
        register_status_text.configure(text="")
        if len(password) > 5:
            is_valid_username(password,register_status_text)

    def check_username():
        username = username_input.get()
        register_status_text.configure(text="")
        if len(username) > 5:
            is_valid_username(username,register_status_text)

    def create_account_UI():
        register_status_text.configure(text="")
        username = username_input.get()
        email = email_input.get()
        password = password_input.get()
        can_create_account = True
        if not is_valid_username(username,register_status_text):
            can_create_account = False
        elif not is_valid_email(email,register_status_text):
            can_create_account = False
        elif not check_password_strength(password,register_status_text):
            can_create_account = False
        elif can_create_account:
            create_account_in_db(username, email, password)
            register_status_text.configure(text="Account created successfully")
        else:
            register_status_text.configure(text="Unexpected error")
    
    username_input.bind("<KeyRelease>", lambda event: check_username())
    password_input.bind("<KeyRelease>", lambda event: check_password())

    create_account_button = customtkinter.CTkButton(main_UI_frame, text="Create Account", command= lambda : create_account_UI())
    create_account_button.grid(row=4, columnspan=2, padx=5, pady=10)

    UI_main.bind('<Return>', lambda event: create_account_UI())

    register_button = customtkinter.CTkButton(UI_main, text="Login", command= lambda : login_page(UI_main))
    register_button.pack(padx=20, pady=10,side="bottom",anchor="sw")

def login_page(UI_main):

    clear_ui(UI_main)
    title(UI_main)

    main_UI_frame = customtkinter.CTkFrame(UI_main)
    main_UI_frame.pack(anchor="center", padx=20)

    username_text = customtkinter.CTkLabel(main_UI_frame, text="Username:")
    password_text = customtkinter.CTkLabel(main_UI_frame, text="Password:")
    username_input = customtkinter.CTkEntry(main_UI_frame, width=300, corner_radius=10)
    password_input = customtkinter.CTkEntry(main_UI_frame, width=300, corner_radius=10, show="*")
    login_status_text = customtkinter.CTkLabel(main_UI_frame, text="")


    username_text.grid(row=0, column=0, padx=5, pady=5)
    password_text.grid(row=1, column=0, padx=5, pady=5)
    username_input.grid(row=0, column=1, padx=5, pady=5)
    password_input.grid(row=1, column=1, padx=5, pady=5)
    login_status_text.grid(row=2, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")

    login_button = customtkinter.CTkButton(main_UI_frame, text="login", command= lambda: check_login(username_input.get(), password_input.get(),login_status_text))
    login_button.grid(row=3, columnspan=2, padx=5, pady=10)

    UI_main.bind('<Return>', lambda event: check_login())

    register_button = customtkinter.CTkButton(UI_main, text="Create Account", command= lambda : register_page(UI_main))
    register_button.pack(padx=20, pady=10,side="bottom",anchor="sw")



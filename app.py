import create_salt
import tkinter
import customtkinter

# sul = create_salt.generate_salt()
# print(sul)

def title():
    title_text = customtkinter.CTkLabel(UI_main, text="CryptoMessage", anchor="center", font=("Arial", 30), pady=40)
    title_text.pack()

def clear_ui():
    for widget in UI_main.winfo_children():
        widget.destroy()

def switch_to_register_page():

    def create_account():
        print("account created")

    clear_ui()
    title()
    main_UI_frame = customtkinter.CTkFrame(UI_main)
    main_UI_frame.pack(anchor="center", padx=20)

    username_text = customtkinter.CTkLabel(main_UI_frame, text="Username:")
    email_text = customtkinter.CTkLabel(main_UI_frame, text="Email:")
    password_text = customtkinter.CTkLabel(main_UI_frame, text="Password:")
    username_input = customtkinter.CTkEntry(main_UI_frame, width=300, corner_radius=10)
    email_input = customtkinter.CTkEntry(main_UI_frame, width=300, corner_radius=10)
    password_input = customtkinter.CTkEntry(main_UI_frame, width=300, corner_radius=10, show="*")

    username_text.grid(row=0, column=0, padx=5, pady=5)
    email_text.grid(row=1, column=0, padx=5, pady=5)
    password_text.grid(row=2, column=0, padx=5, pady=5)
    username_input.grid(row=0, column=1, padx=5, pady=5)
    email_input.grid(row=1, column=1, padx=5, pady=5)
    password_input.grid(row=2, column=1, padx=5, pady=5)

    create_account_button = customtkinter.CTkButton(main_UI_frame, text="Create Account", command=create_account)
    create_account_button.grid(row=3, columnspan=2, padx=5, pady=10)


def login_page():

    clear_ui()
    title()

    def print_data():
        print(username_input.get(), password_input.get())

    main_UI_frame = customtkinter.CTkFrame(UI_main)
    main_UI_frame.pack(anchor="center", padx=20)

    username_text = customtkinter.CTkLabel(main_UI_frame, text="Username:")
    password_text = customtkinter.CTkLabel(main_UI_frame, text="Password:")
    username_input = customtkinter.CTkEntry(main_UI_frame, width=300, corner_radius=10)
    password_input = customtkinter.CTkEntry(main_UI_frame, width=300, corner_radius=10, show="*")

    username_text.grid(row=0, column=0, padx=5, pady=5)
    password_text.grid(row=1, column=0, padx=5, pady=5)
    username_input.grid(row=0, column=1, padx=5, pady=5)
    password_input.grid(row=1, column=1, padx=5, pady=5)

    login_button = customtkinter.CTkButton(main_UI_frame, text="login", command=print_data)
    login_button.grid(row=2, columnspan=2, padx=5, pady=10)

    register_button = customtkinter.CTkButton(UI_main, text="Create Account", command=switch_to_register_page)
    register_button.pack(padx=20, pady=10,side="bottom",anchor="sw")


# UI
customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("blue")

UI_main = customtkinter.CTk()
UI_main.geometry("520x720")
UI_main.title("CryptoMessage")


login_page()
UI_main.mainloop()
import string
import requests
import os
from icecream import ic
import re
from db_utils import get_usernames,get_emails
import customtkinter
import time

def is_valid_username(username,register_status_text):
    username_list = get_usernames()
    
    if username in username_list:
        register_status_text.configure(text=f"User {username} already exist") 
        return False
    elif not username:
        register_status_text.configure(text=f"Username, cannot be empty")
        return False
    else:
        return True

def is_valid_email(email,register_status_text):

    email_list = get_emails()
    email_pattern = r'^[\w\.-]+@[\w\.-]+(\.\w+)+$'


    if email in email_list:
        register_status_text.configure(text=f"Account with Email {email} already exist")
        return False
    elif not email:
        register_status_text.configure(text=f"Email, cannot be empty") 
        return False
    elif re.match(email_pattern, email):
        return True
    else:
        register_status_text.configure(text=f"this email does not exist")
        return False
    
def download_file(url, file_name):
    response = requests.get(url)

    if response.status_code == 200:
        with open(file_name, "wb") as file:
            file.write(response.content)
        print(f"File '{file_name}' downloaded successfully.")
    else:
        print(f"Failed to download the file. Status code: {response.status_code}")

github_raw_url = "https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-1000000.txt"
local_file_name = "password_list.txt"

def check_password_strength(password, register_status_text):
    if not os.path.exists(local_file_name):
        download_file(github_raw_url, local_file_name)

    min_password_length = 12
    min_uppercase_letters = 1
    min_special_characters = 1
    special_characters_list = set(string.punctuation)
    
    number_of_uppercase = sum(1 for character in password if character.isupper())
    number_of_numbers = sum(1 for character in password if character.isdigit())
    number_of_special_characters = sum(1 for character in password if character in special_characters_list)

    if not password:
        return register_status_text.configure(text="Password cannot be empty") and False

    with open(local_file_name, "r") as file:
        for line in file:
            if password in line:
                register_status_text.configure(text="Password is in the wordlist")
                return False
    
    if ' ' in password:
        register_status_text.configure(text="Password contains spaces")
        return False
    
    elif len(password) < min_password_length:
        register_status_text.configure(text=f"Password is too short, Min {min_password_length}")
        return False
    
    elif number_of_uppercase < min_uppercase_letters:
        register_status_text.configure(text=f"Min uppercase {min_uppercase_letters}")
        return False
    elif number_of_uppercase == len(password) - number_of_numbers:
        register_status_text.configure(text="Min lowercase 1")
        return False
    elif number_of_special_characters < min_special_characters:
        register_status_text.configure(text=f"Min special characters {min_special_characters}")
        return False
    else:
        register_status_text.configure(text="Password is strong")
        return True

def check_password_strength_karel(password, register_status_text):
    num_uppercase_letters = 0
    num_special_characters = 0
    num_lowercase_letters = 0
    num_numbers = 0
    start_time = time.time()
    ic(password)
    
    with open(local_file_name, "r") as file:
        for line in file:
            if password in line:
                return register_status_text.configure(text="Password in wordlist") and False
            
    for character in password:
        if character.isupper():
            num_uppercase_letters += 1
        for special in character:
            if special in string.punctuation:
                num_special_characters += 1
        if character.islower():
            num_lowercase_letters += 1
        for digit in character:
            if digit in string.digits:
                num_numbers += 1

    if not password:
        end_time = time.time()
        elapsed_time_ms = (end_time - start_time) * 1000
        ic(elapsed_time_ms)
        register_status_text.configure(text="Password cannot be empty")
        return True
    elif (num_uppercase_letters >= 1 and num_special_characters >= 1 and num_lowercase_letters >= 1 and num_numbers >= 1 and len(password) >= 12):
        register_status_text.configure(text="Password is strong")
        return True
    elif (num_uppercase_letters < 1):
        register_status_text.configure(text="You don't have 1 or more uppercase letters")
        return False
    elif (num_special_characters < 1):
        register_status_text.configure(text="You don't have 1 or more special characters")  
        return False
    elif (num_lowercase_letters < 1):
        register_status_text.configure(text="You don't have 1 or more lowercase characters")  
        return False
    elif (num_numbers < 1):
        register_status_text.configure(text="You don't have 1 or more numbers")  
        return False
    elif (len(password) < 12):
        register_status_text.configure(text="Your password is less than 12 characters long")    
        return False
    else:
        register_status_text.configure(text="Unexpected error")
        return False


if __name__ == "__main__":
    UI = customtkinter.CTk()
    UI.geometry("520x720")
    UI.title("CryptoMessage")
    status_text = customtkinter.CTkLabel(UI,text="")
    username_input = customtkinter.CTkEntry(UI, width=300, corner_radius=10)
    status_text.pack(side="top", fill="both", expand=True)
    username_input.pack(side="top", fill="both", expand=True)
    UI.bind('<Return>', lambda event: check_password_strength(username_input.get(), status_text))
    UI.mainloop()


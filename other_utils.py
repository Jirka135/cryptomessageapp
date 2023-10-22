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
        return register_status_text.configure(text=f"User {username} already exist"),False
    elif not username:
        return register_status_text.configure(text=f"Username, cannot be empty"),False
    else:
        return True

def is_valid_email(email,register_status_text):

    email_list = get_emails()
    email_pattern = r'^[\w\.-]+@[\w\.-]+(\.\w+)+$'


    if email in email_list:
        return register_status_text.configure(text=f"Account with Email {email} already exist") and False
    elif not email:
        return register_status_text.configure(text=f"Email, cannot be empty") and False
    elif re.match(email_pattern, email):
        return True
    else:
        return register_status_text.configure(text=f"this email does not exist") and False
    
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

def check_password_strength(password,register_status_text):

    if not os.path.exists(local_file_name):
        download_file(github_raw_url, local_file_name)

    start_time = time.time()

    min_password_length = 12
    min_uppercase_letters = 1
    min_special_characters = 1
    special_characters_list = set(string.punctuation)
    #print(f"Checking password {password}")
    
    # Character counting
    number_of_uppercase = sum(1 for character in password if character.isupper())
    number_of_numbers = sum(1 for character in password if character.isdigit())
    number_of_special_characters = sum(1 for character in password if character in special_characters_list)

    if not password:
        return register_status_text.configure(text=f"Password cannot be empty") and False

    # Wordlist checking
    with open(local_file_name, "r") as file:
        for line in file:
            if password in line:
                register_status_text.configure(text=f"Password is in the wordlist")
                end_time = time.time()
                elapsed_time_ms = (end_time - start_time) * 1000
                ic(elapsed_time_ms)
                return False
    
    # Space checking
    if ' ' in password:
        register_status_text.configure(text=f"Password contains spaces")
        end_time = time.time()
        elapsed_time_ms = (end_time - start_time) * 1000
        ic(elapsed_time_ms)
        return False
    
    # Length checking
    elif len(password) < min_password_length:
        register_status_text.configure(text=f"Password is too short, Min {min_password_length}")
        end_time = time.time()
        elapsed_time_ms = (end_time - start_time) * 1000
        ic(elapsed_time_ms)
        return False
    
    # Uppercase checking
    elif number_of_uppercase < min_uppercase_letters:
        register_status_text.configure(text=f"Min uppercase {min_uppercase_letters}")
        end_time = time.time()
        elapsed_time_ms = (end_time - start_time) * 1000
        ic(elapsed_time_ms) 
        return False
    elif number_of_uppercase == len(password) - number_of_numbers:
        register_status_text.configure(text=f"Min lowercase 1")
        end_time = time.time()
        elapsed_time_ms = (end_time - start_time) * 1000
        ic(elapsed_time_ms)
        return False
    elif number_of_special_characters < min_special_characters:
        end_time = time.time()
        elapsed_time_ms = (end_time - start_time) * 1000
        ic(elapsed_time_ms)
        register_status_text.configure(text=f"Min special characters {min_special_characters}")
        return False
    else:
        end_time = time.time()
        elapsed_time_ms = (end_time - start_time) * 1000
        register_status_text.configure(text=f"Password is strong")
        return True

def kontrola_síly_hesla(heslo,register_status_text):
    pocet_velkych_pismen = 0
    pocet_specifickych_znaku = 0
    pocet_malych_pismen = 0
    pocet_cisel = 0
    start_time = time.time()
    ic(heslo)
    with open(local_file_name, "r") as file:
        for line in file:
            if heslo in line:
                return register_status_text.configure(text=f"Password in wordlist") and False
            
    for znak in heslo:
        if znak.isupper():
            pocet_velkych_pismen += 1
        for special in znak:
            if special in string.punctuation:
                pocet_specifickych_znaku += 1
        if znak.islower():
            pocet_malych_pismen += 1
        for character in znak:
            if character in string.digits:
                pocet_cisel += 1

    if (pocet_velkych_pismen >= 1 and pocet_specifickych_znaku >= 1 and pocet_malych_pismen >= 1 and pocet_cisel >= 1 and len(heslo) >= 12):
        end_time = time.time()
        elapsed_time_ms = (end_time - start_time) * 1000
        ic(elapsed_time_ms)
        register_status_text.configure(text=f"Password is strong")
        return True
    elif (pocet_velkych_pismen < 1):
        register_status_text.configure(text=f"You dont have 1 or more uppercase letters") 
        end_time = time.time()
        elapsed_time_ms = (end_time - start_time) * 1000
        ic(elapsed_time_ms) 
        return False
    elif (pocet_specifickych_znaku < 1 ):
        register_status_text.configure(text=f"you dont have 1 or more special characters")  
        end_time = time.time()
        elapsed_time_ms = (end_time - start_time) * 1000
        ic(elapsed_time_ms)
        return False
    elif (pocet_malych_pismen <1):
        register_status_text.configure(text=f"you dont have 1 or more lowercase characters")  
        end_time = time.time()
        elapsed_time_ms = (end_time - start_time) * 1000
        ic(elapsed_time_ms)
        return False
    elif (pocet_malych_pismen < 1):
        register_status_text.configure(text=f"you dont have 1 or more numbers")  
        end_time = time.time()
        elapsed_time_ms = (end_time - start_time) * 1000
        ic(elapsed_time_ms)
        return False
    elif (pocet_malych_pismen < 1):
        register_status_text.configure(text=f"you dont have 12 charcter long password")    
        end_time = time.time()
        elapsed_time_ms = (end_time - start_time) * 1000
        ic(elapsed_time_ms)
        return False
    else:
        register_status_text.configure(text=f"Unexpected error")
        return False

if __name__ == "__main__":
    UI = customtkinter.CTk()
    UI.geometry("520x720")
    UI.title("CryptoMessage")
    status_text = customtkinter.CTkLabel(UI,text="")
    username_input = customtkinter.CTkEntry(UI, width=300, corner_radius=10)
    status_text.pack(side="top", fill="both", expand=True)
    username_input.pack(side="top", fill="both", expand=True)
    UI.bind('<Return>', lambda event: kontrola_síly_hesla(username_input.get(), status_text))
    UI.mainloop()


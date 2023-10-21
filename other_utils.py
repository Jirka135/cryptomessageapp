import string
import requests
import os
from icecream import ic
import re
from db_utils import get_usernames,get_emails

def is_valid_username(username,status_text):
    username_list = get_usernames()
    
    if username in username_list:
        return status_text.configure(text=f"User {username} already exist"),False
    elif not username:
        return status_text.configure(text=f"Username, cannot be empty"),False
    else:
        return True

def is_valid_email(email,status_text):

    email_list = get_emails()
    email_pattern = r'^[\w\.-]+@[\w\.-]+(\.\w+)+$'


    if email in email_list:
        return status_text.configure(text=f"Account with Email {email} already exist"),False
    elif not email:
        return status_text.configure(text=f"Email, cannot be empty"),False
    elif re.match(email_pattern, email):
        return True
    else:
        return status_text.configure(text=f"this email does not exist"),False
    
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

def check_password_strength(password,status_text):

    if not os.path.exists(local_file_name):
        download_file(github_raw_url, local_file_name)

    min_password_length = 12
    min_uppercase_letters = 1
    min_special_characters = 1
    special_characters_list = set(string.punctuation)
    print(f"Checking password {password}")
    
    # Character counting
    number_of_uppercase = sum(1 for character in password if character.isupper())
    number_of_numbers = sum(1 for character in password if character.isdigit())
    number_of_special_characters = sum(1 for character in password if character in special_characters_list)
    
    if not password:
        return status_text.configure(text=f"Password cannot be empty"),False

    # Wordlist checking
    with open(local_file_name, "r") as file:
        for line in file:
            if password in line:
                return status_text.configure(text=f"Password {password} is in the wordlist"),False
    
    # Space checking
    if ' ' in password:
        return status_text.configure(text=f"Password {password} contains spaces"),False
    
    # Length checking
    elif len(password) < min_password_length:
        return status_text.configure(text=f"Password {password} is too short"),False
    
    # Uppercase checking
    elif number_of_uppercase < min_uppercase_letters:
        return status_text.configure(text=f"Password {password} doesn't have enough uppercase letters"),False
    elif number_of_uppercase == len(password) - number_of_numbers:
        return status_text.configure(text=f"Password {password} doesn't have enough lowercase letters"),False
    elif number_of_special_characters < min_special_characters:
        return status_text.configure(text=f"Password {password} doesn't have enough special characters"),False
    else:
        return status_text.configure(text="Password {password} is strong as heck"),True

""""
if __name__ == "__main__":
    result = is_valid_email("jirkajebest@gmail.com")
    ic(result)
"""
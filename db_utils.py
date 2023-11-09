from my_sqlalchemy import session,User
import bcrypt
from icecream import ic
from create_salt import generate_salt

def create_account_in_db(username,email,password):
    salt = generate_salt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'),salt)
    new_user = User(username=username, email=email, password=hashed_password,salt=salt)
    session.add(new_user)
    session.commit()

def check_login(username,password,login_status_text):
    user_salt_row = session.query(User.salt).filter(User.username == username).first()
    password_hash_row = session.query(User.password).filter(User.username == username).first()
    
    if user_salt_row and password_hash_row:
        user_salt = user_salt_row.salt
        password_hash_from_db = password_hash_row.password

        password_hash_input = bcrypt.hashpw(password.encode('utf-8'), user_salt)
        login_status_text.configure(text="")

        if password_hash_input == password_hash_from_db:
            ic("login successful")
            login_status_text.configure(text="")
            return True
        else:
            ic("login failed, wrong password")
            #password_status_value = "wrong password"
            login_status_text.configure(text="wrong password")
    else:
        ic("tento uživatel neexistuje")
        #username_status_value = "tento uživatel neexistuje"
        login_status_text.configure(text="user dont exists")
        

    
def get_usernames():
    users = session.query(User.username).all()
    return [user[0] for user in users]

def get_emails():
    emails = session.query(User.email).all()
    return [email[0] for email in emails]

def delete_account(to_remove):
    users_to_remove = session.query(User).filter(User.id.in_(to_remove))
    users_to_remove.delete(synchronize_session=False)
    session.commit()

def check_username_in_database(username):
    users = session.query(User.username).all()
    for user in users:
        user_name = user[0]
        if user_name == username:
            ic("user already exists")

#delete_account([1,2,3,4,5,6,7,8,9])
#create_account(username="jirka",email="nnheo@example.com",password="jirkajebest")
#check_login("pepa", "password")
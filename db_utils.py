from my_sqlalchemy import session,User
import bcrypt
from icecream import ic
from create_salt import generate_salt

def create_account(username,email,password):
    
    salt = generate_salt()
    hashed_username = username
    hashed_email = email
    hashed_password = bcrypt.hashpw(password.encode('utf-8'),salt)
    new_user = User(username=hashed_username, email=hashed_email, password=hashed_password,salt=salt)
    session.add(new_user)
    session.commit()

def print_users():
    users = session.query(User).all()
    for user in users:
        ic(user)

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
#create_account(username="pepa",email="nnheo@example.com",password="password")
print_users()
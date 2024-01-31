from db.querys import *

class User:
    def __init__(self, username, password, confirm_password="", first_name="", last_name="", email_address="", phone_number=""):
        self.username = username
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.email_address = email_address
        self.phone_number = phone_number
        self.isactive= True
        self.is_logined = False
    
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}".title()
    
    def save(self):
        # connect to Database and save user info
        user_save(self)
        print("User successfully created.")
        
    def __str__(self):
        return self.username
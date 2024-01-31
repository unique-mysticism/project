from db.querys import *
from libs.verification import *
from .models import *
from libs.messages import *


def if_empty(info):
        return [False for ele in list(info.values()) if ele == ""]

        
#deleted#
# def info_validation(username, password, confirm_password, first_name, last_name, email_address, phone_number):
#         chk_paswod = list(password_validate(password))
#         #If entered username was found in db, show error 
#         if not username_validate(username):
#             return error_username
#         elif chk_paswod: 
#             return "\n".join(chk_paswod)
#         if not password == confirm_password:
#             return error_passwords_match
#         elif not name_validate(first_name):
#             return error_first_name
#         elif not name_validate(last_name):
#             return error_last_name
#         elif not phone_num_validate(phone_number):
#             return error_phone_num
#         return


        
def check1(username, password):
    chk_paswod = list(password_validate(password))
    if not username_validate(username):
        return error_username
    elif chk_paswod: 
        return "\n".join(chk_paswod)
    return
    
def check2(username, password, confirm_password):
    result = check1(username, password)
    if result: return result
    elif not password == confirm_password:
        return error_passwords_match
    return
        
def check3(username, password, confirm_password, first_name, last_name, email_address, phone_number):
    if duplicate_found(username): 
        return error_duplicate_username
    result = check2(username, password, confirm_password)
    if result: return result
    if not name_validate(first_name):
        return error_first_name
    elif not name_validate(last_name):
        return error_last_name
    elif not phone_num_validate(phone_number):
        return error_phone_num
    return
 
    
    
def check_signup(info):
    """Check signup input validation

    Arguments:
        info {dict} -- user info
    """

    if if_empty(info):
        return error_empty_input
    
    validation_result = check3(**info)
    if validation_result:
        return validation_result
    
    chk_emal = email_validate(info["email_address"],info["first_name"])  
    if not chk_emal:
        return error_email_address
    del info["confirm_password"]
    user_save(info)
    return chk_emal

# def profile(info):
#     ToggleToProfile()
#     # Put res and info in a Dictonary and Show
#     res = ("user_id", "username", "password", "first_name", "last_name", "email_address", "phone_num")
#     info = dict(map(lambda i,j : (i,j) , res,info))
#     profile_result.config(text=f'{successful_login}\n\n\nFirst Name: {info["first_name"]}\nLast Name: {info["last_name"]}\nEmail Address:\n{info["email_address"]}\nPhone Number:{info["phone_num"]}', fg="green")

def check_login(info):
    """_summary_

    Arguments:
        info {_type_} -- _description_

    Returns:
        _type_ -- _description_
    """
    if if_empty(info):
        return error_empty_input
        
    validation_result = check1(**info)
    if validation_result:
        return validation_result
    elif user_found(info):
        return successful_login
    else:
        return error_username_password_match
        


def check_reset_password(info):
    """_summary_

    Arguments:
        info {_type_} -- _description_

    Returns:
        _type_ -- _description_
    """
    if if_empty(info):
        return error_empty_input
    
    validation_result = check2(**info)
    del info["confirm_password"]
    if validation_result:
        return validation_result
    elif not duplicate_found(info["username"]):
        return error_exist_username
    if user_found(info):
        return error_duplicate_password
    change_password(info)
    return successful_password_changed




    
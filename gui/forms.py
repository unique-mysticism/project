from .function import *
from auth.validation import check_signup, check_login, check_reset_password



def signup():
    info = get_info(lbls, entries)
    result = check_signup(info)
    color = message_color(result)
    if color == "red":
        result = result.strip("Error:")
    elif color == "blue":
        empty_inputs()
    result_signup.config(text=result, fg=color)
    
def login():
    info = get_info(lbls, entries)
    result = check_login(info)
    color = message_color(result)
    if color == "red":
        result = result.strip("Error:")
    elif color == "blue":
        empty_inputs()
        ToggleToProfile()
        return result_profile.config(text="Here is your profile:", fg="black")
    result_login.config(text=result, fg=color)
    
def reset_password():
    info = get_info(lbls, entries)
    result = check_reset_password(info)
    color = message_color(result)
    if color == "red":
        result = result.strip("Error:")
    elif color == "blue":
        empty_inputs()
    result_resetpassword.config(text=result, fg=color)



def lbl_entry_pairs(lbls:list, entries:list):
    """Create Lables and Entries on form
    
    Arguments:
        lbls {list} -- List of Lables name
        entries {list} -- List of Entries name
    """
    for row_num, lbl, entry in zip(range(len(lbls)), lbls, entries):
        lbl = Label(currentframe, text=lbl, font=TEXT_FONT, bd=15, bg=TEXT_BG, width=20)
        lbl.grid(row = row_num)
        # If the entry is password ,instead of letters shows *
        entry_show = "*" if entry in [PASSWORD, CONFIRM_PASSWORD] else None
        entry = Entry(currentframe, textvariable=entry, font=TEXT_FONT, bg=ENTRY_BG, width=20, show=entry_show)
        entry.grid(row = row_num, column=1, sticky="W",padx=(0,50))
 

       
def signup_form():
    """
    Create Signup form
    """
    global currentframe, result_signup, lbls, entries
    lbls = ["Username:", "Password:", "Confirm Password:", "First name:", "Last name:", "Email Address:", "Phone Number:"]
    entries = [USERNAME, PASSWORD, CONFIRM_PASSWORD, FIRST_NAME, LAST_NAME, EMAIL_ADDRESS, PHONE_NUMBER]
    links = ["Already have account?"]
    
    currentframe = create_frame()
    lbl_entry_pairs(lbls, entries)
    link_login = Label(currentframe, text=links[0], font="Helvetica 15 underline", bg=TEXT_BG)
    link_login.grid(row=8, columnspan=2)
    link_login.bind("<Button-1>", ToggleToLogin)
    btn_sginup = Button(currentframe, text="Register", font=TEXT_FONT, command=signup, width=20, bg=ENTRY_BG, borderwidth=8)
    btn_sginup.grid(row=9, columnspan=2, pady=(10,0))   
    result_signup = Label(currentframe, text="", font=TEXT_FONT, bg=TEXT_BG, wraplength=500)
    result_signup.grid(row=10, columnspan=2, pady=(10,0))
    # deleted#
    # lbl_username            = Label(currentframe, text=lbls[0], font=TEXT_FONT, bd=15, bg=TEXT_BG)
    # lbl_password            = Label(currentframe, text=lbls[1], font=TEXT_FONT, bd=15, bg=TEXT_BG)
    # lbl_password_confirm    = Label(currentframe, text=lbls[2], font=TEXT_FONT, bd=15, bg=TEXT_BG)
    # lbl_firstname           = Label(currentframe, text=lbls[3], font=TEXT_FONT, bd=15, bg=TEXT_BG)
    # lbl_lastname            = Label(currentframe, text=lbls[4], font=TEXT_FONT, bd=15, bg=TEXT_BG)
    # lbl_email_address       = Label(currentframe, text=lbls[5], font=TEXT_FONT, bd=15, bg=TEXT_BG)
    # lbl_phone_num           = Label(currentframe, text=lbls[6], font=TEXT_FONT, bd=15, bg=TEXT_BG)
    # entry_username          = Entry(currentframe, textvariable=entries[0], font=TEXT_FONT, width=20, bg=ENTRY_BG)
    # entry_password          = Entry(currentframe, textvariable=entries[1], font=TEXT_FONT, width=20, show="*", bg=ENTRY_BG)
    # entry_password_confirm  = Entry(currentframe, textvariable=entries[2], font=TEXT_FONT, width=20, show="*", bg=ENTRY_BG)
    # entry_firstname         = Entry(currentframe, textvariable=entries[3], font=TEXT_FONT, width=20, bg=ENTRY_BG)
    # entry_lastname          = Entry(currentframe, textvariable=entries[4], font=TEXT_FONT, width=20, bg=ENTRY_BG)
    # entry_email_address     = Entry(currentframe, textvariable=entries[5], font=TEXT_FONT, width=30, bg=ENTRY_BG)
    # entry_phone_num         = Entry(currentframe, textvariable=entries[6], font=TEXT_FONT, width=20, bg=ENTRY_BG)
    # lbl_username.grid(row=1, sticky="E")
    # lbl_password.grid(row=2, sticky="E")
    # lbl_password_confirm.grid(row=3, sticky="E")
    # lbl_firstname.grid(row=4, sticky="E")
    # lbl_lastname.grid(row=5, sticky="E")
    # lbl_email_address.grid(row=6, sticky="E")
    # lbl_phone_num.grid(row=7, sticky="E")
    # entry_username.grid(row=1, column=1, sticky="W")
    # entry_password.grid(row=2, column=1, sticky="W")
    # entry_password_confirm.grid(row=3, column=1, sticky="W")
    # entry_firstname.grid(row=4, column=1, sticky="W")
    # entry_lastname.grid(row=5, column=1, sticky="W")
    # entry_email_address.grid(row=6, column=1)
    # entry_phone_num.grid(row=7, column=1, sticky="W")    
          
def login_form():
    """
    Create Login form
    """
    global currentframe, result_login, lbls, entries
    lbls = ["Username:", "Password:"]
    entries = [USERNAME, PASSWORD]
    links = ["Forget Password", "Don't have account?"]
    
    currentframe = create_frame()
    lbl_entry_pairs(lbls, entries)
    link_forget_password = Label(currentframe, text=links[0], font="Helvetica 15 underline", bg=TEXT_BG)
    link_forget_password.grid(row=3, columnspan=2)
    link_forget_password.bind("<Button-1>", ToggleToResetPassword)
    link_signup = Label(currentframe, text=links[1], font="Helvetica 15 underline", bg=TEXT_BG)
    link_signup.grid(row=4, columnspan=2)
    link_signup.bind("<Button-1>", ToggleToSignup)
    btn_login = Button(currentframe, text="Login", command=login, font=TEXT_FONT, width=20, bg=ENTRY_BG, borderwidth=8)
    btn_login.grid(row=5, columnspan=2, pady=(10,0))
    result_login = Label(currentframe, text="", font=TEXT_FONT, bg=TEXT_BG, wraplength=500)
    result_login.grid(row=6, columnspan=2, pady=(10,0))
    # deleted#
    # lbl_username        = Label(currentframe, text=lbls[0], font=TEXT_FONT, bd=15, bg=TEXT_BG)
    # lbl_password        = Label(currentframe, text=lbls[1], font=TEXT_FONT, bd=15, bg=TEXT_BG)
    # entry_username      = Entry(currentframe, textvariable=entries[0], font=TEXT_FONT, width=20, bg=ENTRY_BG)
    # entry_password      = Entry(currentframe, textvariable=entries[1], font=TEXT_FONT, width=20, show="*", bg=ENTRY_BG)
    # lbl_username.grid(row=1)
    # lbl_password.grid(row=2)
    # entry_username.grid(row=1, column=1)
    # entry_password.grid(row=2, column=1)

def reset_password_form():
    """
    Create Reset Password form
    """
    global currentframe, result_resetpassword, lbls, entries
    lbls = ["Username:", "Password:", "Confirm Password:"]
    entries = [USERNAME, PASSWORD, CONFIRM_PASSWORD]
    
    currentframe = create_frame()
    lbl_entry_pairs(lbls, entries)
    btn_back = Button(currentframe, text="⬅️Back", command=ToggleToLogin, font=TEXT_FONT, bg=ENTRY_BG, borderwidth=8)
    btn_back.grid(row=4, sticky="W", pady=(10,0), padx=(100,0))
    btn_change_password = Button(currentframe, text="Change Password", font=TEXT_FONT, command=reset_password, width=20, bg=ENTRY_BG, borderwidth=8)
    btn_change_password.grid(row=4, columnspan=2, pady=(10,0), padx=(110,0))
    result_resetpassword = Label(currentframe, text="", font=TEXT_FONT, bd=15, bg=TEXT_BG, wraplength=500)
    result_resetpassword.grid(row=5, columnspan=2, pady=(10,0))
    # deleted#
    # lbl_username            = Label(currentframe, text=lbls[0], font=TEXT_FONT, bd=15, bg=TEXT_BG)
    # lbl_password            = Label(currentframe, text=lbls[1], font=TEXT_FONT, bd=15, bg=TEXT_BG)
    # lbl_password_confirm    = Label(currentframe, text=lbls[2], font=TEXT_FONT, bd=15, bg=TEXT_BG)
    # entry_username          = Entry(currentframe, textvariable=entries[0], font=TEXT_FONT, bg=ENTRY_BG, width=20)
    # entry_password          = Entry(currentframe, textvariable=entries[1], font=TEXT_FONT, bg=ENTRY_BG, width=20, show="*")
    # entry_password_confirm  = Entry(currentframe, textvariable=entries[2], font=TEXT_FONT, bg=ENTRY_BG, width=20, show="*")
    # lbl_username.grid(row=1)
    # lbl_password.grid(row=2)
    # lbl_password_confirm.grid(row=3)
    # entry_username.grid(row=1, column=1)
    # entry_password.grid(row=2, column=1)
    # entry_password_confirm.grid(row=3, column=1)

def profile_form():
    """
    Create Profile form
    """
    global currentframe, result_profile
    
    currentframe = create_frame()    
    btn_logout  = Button(currentframe, text="Logout", command=ToggleToLogin, font=TEXT_FONT, bg=ENTRY_BG, borderwidth=8)
    btn_logout.grid(row=1, column=1, sticky="W")
    result_profile = Label(currentframe, text="", font=TEXT_FONT, bd=15, bg=TEXT_BG)
    result_profile.grid(row=1, column=2, padx=(0,200))

    
    
def ToggleToLogin(event=None):
    """
    ToggleToLogin changes 'current_form' to 'login_form'
    """
    currentframe.destroy()
    login_form()

def ToggleToSignup(event=None):
    """
    ToggleToSignup changes 'current_form' to 'signup_form'
    """
    currentframe.destroy()
    signup_form()

def ToggleToResetPassword(event=None):
    """
    ToggleToResetPassword changes 'current_form' to 'reset_password_form'
    """
    currentframe.destroy()
    reset_password_form()

def ToggleToProfile(event=None):
    """
    ToggleToProfile changes 'current_form' to 'profile_form'
    """
    currentframe.destroy()
    profile_form()

def empty_inputs():
    USERNAME.set("")
    PASSWORD.set("")
    CONFIRM_PASSWORD.set("")
    FIRST_NAME.set("")
    LAST_NAME.set("")
    EMAIL_ADDRESS.set("")
    PHONE_NUMBER.set("")
    
# Define global Entries name
USERNAME = StringVar()
PASSWORD = StringVar()
CONFIRM_PASSWORD = StringVar()
FIRST_NAME = StringVar()
LAST_NAME = StringVar()
EMAIL_ADDRESS = StringVar()
PHONE_NUMBER = StringVar()


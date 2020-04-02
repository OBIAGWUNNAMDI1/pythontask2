import os
import random 
import string 
f_name = input("Insert User 1 First name:")
l_name = input("Insert User 2 last name:")
email = input("Insert User 2 email_address:")
User_Full_Details1={'firstname':f_name,
'lastname':l_name,
'email_address':email}
def randomstrings(stringlength=6):
    pas= string.ascii_letters
    return ''.join(random.choice(pas)for i in range (stringlength))
system_generated_password1= f_name[0:2]+ l_name[-2:] + randomstrings()
print(system_generated_password1)
password_selection = " " 
while (password_selection==" "):
    password_selection= input('''password_satisfaction Enter yes to save password 
                              enter no to create desired password: >''').lower()
    if password_selection == "yes":
        print(User_Full_Details1)
    else:
        password_selection =="no"
        print("Please create desired new password")
        User_generated_password1=input("Generate desired password:")
        if len(User_generated_password1) > 7:
            print (User_Full_Details1)
            print(User_generated_password1)
        else:
            len(User_generated_password1)<7
            print ("New password must be more than seven numbers")
            User_generated_password1=input("Enter generated password more than seven numbers:")
            print(User_Full_Details1)
            print(User_generated_password1)
        continue
next_action = input('''Do you want to enter another user details
                        Enter yes to input another detail
                        Enter no to print break command:''').lower()
if next_action=='no':
    print(User_Full_Details1)
else:
    f_name2= input("Insert User 2 First name : ")
    l_name2 = input("Insert User 2 Second name:")
    email2 = input("Insert user 2 email address:")
    User_Full_Details2 = {'firstname of user 2': f_name2,
                          'lastname of user 2': l_name2,
                          'email_address of user 2': email2}
    system_generated_password2= f_name2[0:2]+ l_name2[-2:] + randomstrings()
    print(system_generated_password2)
    password_selection = input('''password_satisfaction Enter yes to save password 
                              enter no to create desired password: >''').lower()
    if password_selection == "yes":
        print(User_Full_Details2)
        print(system_generated_password2)
    else:
        password_selection == "no"
        print("Please create desired new password")
        User_generated_password2 = input("Generate desired password:")
        if len(User_generated_password2) > 7:
            print(User_Full_Details2)
            print(User_generated_password2)
        else:
            len(User_generated_password2) < 7
            print("New password must be more than seven numbers")
            User_generated_password2 = input(
                "Enter generated password more than seven numbers:")
            print(User_Full_Details2)
            print(User_generated_password2)
        


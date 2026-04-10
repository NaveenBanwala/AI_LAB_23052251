#1 Password Validator: Develop a Python function to validate a user&#39;s password. The
# function should check for minimum length, presence of uppercase and lowercase
# letters, at least one digit, and a special character. If the password is valid, return
# True, otherwise return False and display an informative error message.



import string

oldPass=input("Enter password:")

while True:
    if len(oldPass)>=8 and any(c.isupper() for c in oldPass) and any(c.islower() for c in oldPass) and any(c.isdigit() for c in oldPass) and any(c in string.punctuation for c in oldPass):
        print("Password is valid.")
        break
    print("Invalid password.")
    # print(oldPass)
    print("Enter password again ")
    print(oldPass, end="")
    oldPass += input("")


# import string
# oldPass = ""
# while True:
#     if oldPass!="": 
#         print("Your Old password is : ",oldPass)
#     password = oldPass
    
#     password=input("Enter password:")
#     if len(password)<8:
#         print("Password must be at least 8 characters long.")
#         oldPass = password
#         continue
#     if not any(c.isupper() for c in password):
#         print("Password must contain at least one uppercase letter.")
#         oldPass = password
#         continue
#     if not any(c.islower() for c in password):
#         print("Password must contain at least one lowercase letter.")
#         oldPass = password
#         continue
#     if not any(c.isdigit() for c in password):
#         print("Password must contain at least one digit.")
#         oldPass = password
#         continue
#     if not any(c in string.punctuation for c in password):
#         print("Password must contain at least one special character.")
#         oldPass = password
#         print(oldPass)
#         continue
#     print("Password is valid.")
#     break


# password=input("Enter password:")
# validate_password(password)

import re


#Function to validate email/username
def username_check(email):   
    #regex to validate email
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    if(re.search(regex,email)):   
        pass   
    else:   
        print("Invalid Email/Username")




# Password validation 
# Function to validate the password
def password_check(passwd):

    SpecialSym =['!', '@', '#', '$', '%', '^', '&','*','(',')','?','_']
    passwd_val = True

    if len(passwd) < 5:
        print('length should be at least 5')
        passwd_val = False
        
    if len(passwd) > 16:
        print('length should be not be greater than 16')
        passwd_val = False

    if not any(char.isdigit() for char in passwd):
        print('Password should have at least one numeral')
        passwd_val = False

    if not any(char.isupper() for char in passwd):
        print('Password should have at least one uppercase letter')
        passwd_val = False

    if not any(char.islower() for char in passwd):
        print('Password should have at least one lowercase letter')
        passwd_val = False

    if not any(char in SpecialSym for char in passwd):
        print('Password should have at least one of the symbols $@#')
        passwd_val = False
    if passwd_val == True:
        pass
    else:
        print("Invalid Password !!")

# Main method
def main():
    print("Please Provide username and password to register")
    username = str(input("Name: "))
    password = str(input("Password: "))

    username_check(username)
    password_check(password)
    with open('user_passwd.txt','a') as f:
        f.write(username+','+password+'\n')

# Driver Code
if __name__ == '__main__':
    main()

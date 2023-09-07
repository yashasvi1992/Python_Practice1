[![Pylint Score of storeSensors](https://img.shields.io/badge/storeSensors%20Pylint%20Score-8.421052631578947-yellow.svg)]
def get_existing_users(PASSWORD_FNAME):
    with open(PASSWORD_FNAME,'r' ) as fp:
         for line in fp.readlines():
             # This expects each line of a file to be (name, pass) seperated by comma
             username, password = line.split(',')
             yield username, password

def is_authorized(username, password,PASSWORD_FNAME):
    return any((user == (username, password) for user in get_existing_users(PASSWORD_FNAME)) 

def user_exists(username,PASSWORD_FNAME):
    return any((usr_name == username) for usr_name, _ in get_existing_users(PASSWORD_FNAME))

def forgot_passwd(username,PASSWORD_FNAME):
    with open(PASSWORD_FNAME,'r') as fp:
         for line in fp.readlines():
             name,password=line.split(',')
             if name == username:
                 return password
             else:
                 pass

def checkdetails(username,password,PASSWORD_FNAME):
    if is_authorized(username, password,PASSWORD_FNAME):
       print("Welcome Back, " + name)
       return True        
    if user_exists(name,PASSWORD_FNAME):
       print("Password entered is wrong")
       return False
    
    print("Name not found. Please Register.")
    return False

def getdetails(username,password,PASSWORD_FNAME):
    if not user_exists(name,PASSWORD_FNAME):
       print("Name Unavailable. Please Register")
       return False
               
def main():
    PASSWORD_FNAME='user_passwd.txt'
    #choose to login or forgot password
    print("choose login or forgot_password")
    action=str(input("Action: "))
    if action == "forgot_password":
       usernname = str(input("Name: "))
       val1 = forgot_passwd(username,PASSWORD_FNAME)
       print("password for "+username+" is "+val1)
    elif action == "login"   
    #please enter username and password to login
        usernname = str(input("Name: "))
        password = str(input("Password: "))
        PASSWORD_FNAME='user_passwd.txt'
        val1=getdetails(username,password)
        if val1 == False:
            pass
        else:
            checkdetails(username,password)
    else:
        print("choose action either login or forgot_password")
       
       
# Driver Code
if __name__ == '__main__':
    main()

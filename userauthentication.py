


userdata = {}


class authe():
    def __init__(self) -> None:
        pass

    def singin(self,name,password):
        for i in list(userdata.keys()):
            if name == i and password == userdata[i][1]:
                print('successfully longin !!!')
            else:
                print("user not found !!")

    def singup(self,name,password,repassword,age ):
        
            if not name in list(userdata.keys()) and password == repassword :
                us =len(userdata)+1
                userdata[name]=[us,password,age]
                print("user is created !!!")
                return True
            else:
                print("user name is already ")     
                


# user = authe()
# user.singin('samir','samir2003')
# print(userdata)

if __name__ == "__main__":
    user = authe()
    while True:
        print('''
        Wellcome to your authe system
        press 1 for create account
        press 2 for singin
        press 3 for account details
        press 4 for exit

        ''')
        try:
            users =int(input("enter number \n"))
        except :
            users = None
            print("enter a number")
        if users == 1 :
            user_name = input('enter your name')
            user_password = input('enter your password')
            user_repassword = input('enter your re-password')
            user_age = input('enter your age ')
            user.singup(user_name,user_password,user_repassword,user_age)
        elif users ==2:
            user_name = input("enter your name")
            user_password = input("enter your password")
            user.singin(user_name,user_password)
        elif users == 3 :
            print(userdata)
        elif users ==4:
            exit()
        elif user == None:
            pass    
        else:
            break   

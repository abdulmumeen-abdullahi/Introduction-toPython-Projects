def signup(self):
        q=input("Enter your matriculation number")
        if len(q)!=10:
            print("Incorrect Matriculation number")
        else:
            t1=input("Enter your surname: ")
            t2=input("Enter your name: ")
            t3=input("Enter your other name: ")
            b = t3[0] + t3[1] + t3[2] + t3[3]
            print("Your new username is: ", b)
            w = "user" + q[3] + q[4] + q[5] + q[7] + q[9]
            return ("Your new password is: ", w)
class sign():
    def signin(self):
        print("This program confirm the sign in password of AFIT's CICT Wi-Fi")
        c = input("User name: ")
        o = input("Enter your password: ")
        #if (i, o != int or len(o) != 2 or len(i) != 2 or i, o.islower()):
        if c == 'user' and o == 'afit':
            print("You are signed up \nIf nothing happens, refresh the page")
            return True
        elif c == 'hr' and o =='hr':
            print("You are signed up \nIf nothing happens, refresh the page")
            return True
        elif len(c) <= 4 and len(o) <= 4:
            print("You are signed up \nIf nothing happens, refresh the page")
            return True
        else:
            print("Incorrect password \nTry again later")
            return False
    def new_signup(self):
        i = 0
        while i < 3:
            if self.signin():
                break
            i += 1
            if i == 3:
                print("Maximum attempts reached. Please create new password.")
                print(signup(self))
nsignup = sign()
nsignup.new_signup()
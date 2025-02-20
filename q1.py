# Write a class called Password_manager. The class should have a list called old_passwords that
# holds all of the user’s past passwords. The last item of the list is the user’s current pass word.
# There should be a method called get_password that returns the current password and a method
# called set_password that sets the user’s password. The set_password method should only
# change the password if the attempted password is different from all the user’s past passwords.
# Finally, create a method called is_correct that receives a string and returns a boolean True or
# False depending on whether the string is equal to the current password or not.

class Password_manager:
    def __init__(self):
        self.old_passwords = []
    def set_password(self,password):
        if(len(self.old_passwords) != 0):
            if password in self.old_passwords:
                print("It is an old password")
                print("Try Again")
        else:
             print("Incorrect password or password have not been set yet")
             self.old_passwords.append(input("Enter the new password: "))

    def get_password(self):
        if(len(self.old_passwords) == 0):
            print("No passwords have been set yet !")
        else:
            return self.old_passwords[len(self.old_passwords)-1]
    def is_correct(self, password):
        if(self.old_passwords[len(self.old_passwords)-1] == password):
            return True
        else:
            return False
    

print("Welcome to password manager !")
p1 = Password_manager()
password = input("Enter the password: ")
p1.set_password(password)
print(p1.get_password())
print(p1.is_correct(input("Enter to check")))





        
            
        
    


        
        
        
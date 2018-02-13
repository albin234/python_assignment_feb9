class Email_gen():
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def get_email(self):
        print(self.fname.lower() + "." + self.lname.lower() + "@gmail.com")


first_name = input("Enter first name: ")
last_name = input("Enter last name: ")
obj = Email_gen(first_name, last_name)
print(obj.get_email())
class String():

    def get_string(self):
        n_string = input("Enter any string: ")
        return n_string

    def print_string(self, str):
        print(str.upper())


s = String()
str = s.get_string()
s.print_string(str)
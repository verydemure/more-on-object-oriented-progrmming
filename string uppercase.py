class IOstring():


    def __init__(self):
        self.str1 = ""


    def get_string(self):
        self.str1 = input("Enter a string :")


    def print_string(self):
        print("result is :" , self.str1.upper())

str0bj = IOstring()



str0bj.get_string()

str0bj.print_string()

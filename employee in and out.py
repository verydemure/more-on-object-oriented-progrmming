class Employee:



    def __init__(self):
        print("Employee created")


    def __del__(self):
        print("Destructor called")

def Create__obj():
    print("making object")
    obj = Employee()
    print("funtion end")
    return obj

obj = Create__obj()
print("project end..")
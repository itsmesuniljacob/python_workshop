# Eventhough Python is interpreter , it have taken some compiler functionalities from C
class Mom:
    """
    Notation self is the first parameter for the class, you can use any there
    The first parameter to the method of the class is the object for the class
    Implicit in C++ & Java, but explicit in Python & Perl
    """
    def Walk(self):
        print('Walk elegantly')
        #print('id(self)',id(self))
    #Constructor
    def __init__(self):
        print('Object created successfully')
    #Destructor
    def __del__(self):
        print('Object destroyed')
Mother = Mom()
Mother.Walk()
# print('id(Mother)',id(Mother))
class Infant:
    """
    Example class
    PASS is a command which does nothin
    """
    pass
# help(Infant)
baby = Infant()
del(Mother)
print('This is the last statement to be printed')
# help(baby)


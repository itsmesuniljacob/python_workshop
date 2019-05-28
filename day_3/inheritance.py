# Eventhough Python is interpreter , it have taken some compiler functionalities from C
class Mom:
    """
    Notation self is the first parameter for the class, you can use any there
    The first parameter to the method of the class is the object for the class
    Implicit in C++ & Java, but explicit in Python & Perl
    """
    def Walk(self):
        print('Walk - Mom')
    #Constructor
    def __init__(self):
        print('Constructor - Mom')
    #Destructor
    def __del__(self):
        print('Destructor - Mom')
# print('id(Mother)',id(Mother))
class Infant(Mom):
    """
    Example class
    PASS is a command which does nothin
    """
    def __init__(self):
        print('Constructor - Infant')
    #Destructor
    def __del__(self):
        print('Destructor - Infant')
# help(Infant)
baby = Infant()
baby.Walk()



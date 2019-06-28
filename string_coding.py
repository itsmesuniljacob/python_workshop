def fisrtReverseMethod(string):
    string = string[::-1]
    return string

def secondReverseString(string):
    str = ""
    for i in string:
        str = i + str
        print(str)
    return str

#Recursive Function
def thirdReverseMethod(string):
    if len(string) == 0:
        return string
    else:
        return thirdReverseMethod(string[1:]) + string[0]    

str = input("Please enter the string    ")
rev_str = secondReverseString(str)
print("Original String is : ", str, "   And Reverse String is : ", rev_str)
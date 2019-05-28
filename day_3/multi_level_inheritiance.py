# Eventhough Python is interpreter , it have taken some compiler functionalities from C
class MGM:
    def Walk3(self):
        print('Walk - MGM')
class MGF:
    def Walk4(self):
        print('Walk - MGF')
class PGM:
    def Walk6(self):
        print('Walk - PGM')
class PGF:
    def Walk(self):
        print('Walk - PGF')
class Mom(MGM,MGF):
    def Walk2(self):
        print('Walk - Mom')
# print('id(Mother)',id(Mother))
class Dad(PGM,PGF):
    def Walk5(self):
        print("Walk - Dad")
class Infant(Mom,Dad):
    def Walk1(self):
        print("Walk - Infant")
# help(Infant)
baby = Infant()
baby.Walk()

#Explanation 
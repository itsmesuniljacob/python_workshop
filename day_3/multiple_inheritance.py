# Eventhough Python is interpreter , it have taken some compiler functionalities from C
class Mom:
    def Walk(self):
        print('Walk - Mom')
# print('id(Mother)',id(Mother))
class Dad:
    def Talk(self):
        print("Talk - Dad")
class Infant(Mom,Dad):
    pass
# help(Infant)
baby = Infant()
baby.Walk()
baby.Talk()
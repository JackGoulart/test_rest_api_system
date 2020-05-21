# def add(a, b):
#     return a + b
#
#
# def sub(a, b):
#     return a - b
#
#
# def mult(a, b):
#     return a * b
#
#
# def switch_calc(a, b):
#     return {"add": lambda: a + b,
#             "sub": lambda: a - b,
#             "mult": lambda: a * b,
#             "div": lambda: a / b,
#             }.get(option)()
#
#
# switch_case = {"add": add,
#                "sub": sub,
#                "mult": mult,
#                }
#
# menu = [option for option in switch_case.keys()]
#
# print(f"Please choice the options to  {menu[0]},  to {menu[1]} and  to {menu[2]} ")
#
# option = input("type the option _$: ")
# a = int(input("Enter value A "))
# b = int(input("Enter value B "))
# # print(switch_case.get(option)(int(a), int(b)))
# print(switch_calc(a,b))


class Candidate:
    def __init__(self, name):
        self.name = name
        self.skills = ['Git', 'Flask', 'Js', 'web2py']
        self.curiosity = 1
        self.pythonExperience = 3

pwdList = ["Ib#", "Blo", "F09", "Hkf", "Ev!", "K%2", "Awe", "Cve", "Lee", "J61", "Gvc", "Dde"]

skillList = ["Git", "Django", "Flask", "Ansible", "CI"]

cdt = Candidate("Jackson")

if cdt.skills in skillList:

    for skill in cdt.skills:

         cdt.pythonExperience += 1

else:

 cdt.curiosity += 1

if cdt.pythonExperience + cdt.curiosity > 4:

   pwdList.sort()

thePassword = ""

test = 'lol un castor"'

for i in range(0, 5):

 thePassword += pwdList[i][1:]

print("Give this password to Nathalie our HR manager: " + thePassword)

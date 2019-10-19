from os import system
from math import sqrt


def carre(var):
    return var * var


def ard(number):
    x = int(number * 100)
    y = int(number * 1000)
    y -= x * 10
    if int(y) >= 5:
        x += 1
    x /= 100
    return x


def nomSeg(desc, str="abc"):
    desc[0][1] = (str[1] + str[2]).upper()
    desc[1][1] = (str[0] + str[1]).upper()
    desc[2][1] = (str[0] + str[2]).upper()
    return desc[0][1], desc[1][1], desc[2][1]


bool = True
loopBreak = None

while bool:
    desc = [[None, "BC"], [None, "AB"], [None, "AC"]]
    nomTri = input("Nom du triangle (trois lettre max et minimum dans l'ordre ABC où BC est l'hypoténuse): ")
    if nomTri == " " or nomTri == "":
        nomSeg(desc)
    else:
        nomSeg(desc, nomTri)
    try :
        desc[0][0] = float(input("Longueur {} (Rien si vous cherchez cette longueur) : ".format(desc[0][1])))
    except :
        desc[0][0] = 0
    try :
        desc[1][0] = float(input("Longueur {} (Rien si vous cherchez cette longueur) : ".format(desc[1][1])))
    except :
        desc[1][0] = 0
    try :
        desc[2][0] = float(input("Longueur {} (Rien si vous cherchez cette longueur) : ".format(desc[2][1])))
    except :
        desc[2][0] = 0
    result = round(carre(desc[1][0])) + round(carre(desc[2][0]))
    if desc[0][0] > 0 and desc[1][0] > 0 and desc[2][0] > 0:
        if carre(desc[1][0]) + carre(desc[2][0]) == round(carre(desc[0][0])):
            print("D'après le théorème de pythagore le triangle est rectangle")
        else:
            print("D'après la contraposée de pythagore le triangle n'est pas rectangle")
    if desc[0][0] == 0:
        print(
            "d'après le théorème de pythagore on a : \n {0}² = {1}² + {2}² \n {0}² = {3}² + {4}² \n {0}² = {5} + {6} \n {0}² = {7} \n {0} = √{7} \n {0} = {8}".format(
                desc[0][1], desc[1][1], desc[2][1], desc[1][0], desc[2][0], ard(carre(desc[1][0])), ard(carre(desc[2][0])),
                result, ard(sqrt(result))))
    if desc[1][0] == 0 or desc[2][0] == 0:
        if desc[2][0] == 0:
            result = round(carre(desc[0][0])) - round(carre(desc[1][0]))
            print(
                "d'après le théorème de pythagore on a : \n {0}² = {1}² + {2}² \n {3}² = {4}² + {2}² \n {5} = {6} + {2}² \n {2}² = {5} - {6} \n {2}² = {7} \n {2} = √{7} \n {2} = {8}".format(
                    desc[0][1], desc[1][1], desc[2][1], desc[0][0], desc[1][0], ard(carre(desc[0][0])),
                    ard(carre(desc[1][0])), result, ard(sqrt(result))))
        else:
            result = round(carre(desc[0][0])) - round(carre(desc[2][0]))
            print(
                "d'après le théorème de pythagore on a : \n {0}² = {1}² + {2}² \n {3}² = {4}² + {2}² \n {5} = {1} + {6}² \n {1}² = {5} - {6} \n {1}² = {7} \n {1} = √{7} \n {1} = {8}".format(
                    desc[0][1], desc[1][1], desc[2][1], desc[0][0], desc[2][0], ard(carre(desc[0][0])),
                    ard(carre(desc[2][0])), result, ard(sqrt(result))))
    loopBreak = input("continuer ? o/N")
    if loopBreak == "o": continue
    else: bool = False


system("pause")

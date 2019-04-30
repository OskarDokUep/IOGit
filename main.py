class Kolo():
    def __init__(self,r):
        self.pole = 3.14159265*r**2
class Prostokat():
    def __init__(self,a ,b):
        self.pole = a*b

class Trojkat():
    def __init__(self,a,b,c):
        p = (a+b+c)/2
        self.pole = (p*(p-a)*(p-b)*(p-c))**(0.5)

n = int(input())
figury = []
for i in range(0,n):
    liczby = input()
    liczby = liczby.split(sep=' ')
    if len(liczby) == 1:
        figury.append(Kolo(float(liczby[0])))
    if len(liczby) == 2:
        figury.append(Prostokat(float(liczby[0]),float(liczby[1])))
    if len(liczby) == 3:
        figury.append(Trojkat(float(liczby[0]),float(liczby[1]),float(liczby[2])))
wynik = 0
for figura in figury:
    wynik += figura.pole

print(round(wynik,2))
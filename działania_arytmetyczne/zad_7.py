import math                #oblicz pole koła o promieniu r

r = float(input())

pole = math.pi * (r**2)
wynik = round(pole, 2)

print(wynik)
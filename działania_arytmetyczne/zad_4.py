#Napisz program, który podzieli liczbę a przez liczbe b; w jednym wierszu wprowadzane, wynik zaokraglony do dwoch liczb po przecinku

a,b = input().split()

print(f"{float(a)/float(b):.2f}")
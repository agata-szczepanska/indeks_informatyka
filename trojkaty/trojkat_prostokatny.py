boki = input("Podaj dlugosci bokow: ").split()
boki = list(map(int, boki))

a = boki[0]
b = boki[1]
c = boki[2]

if a+b > c and b+c>a and a+c>b:
    if a**2 + b**2 == c**2 or b**2 + c**2 == a**2 or a**2 + c**2 == b**2:
        print("Z tych bokow mozna zbudowac trojkat prostokatny")
    else:
        print("Z tych bokow mozna zbudowac trojkat, ale nie prostokatny")
else: 
    print("Z tych bokow nie mozna zbudowac trojkata")
    
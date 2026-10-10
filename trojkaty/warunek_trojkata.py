boki = input().split()

a = int(boki[0])
b = int(boki[1])
c = int(boki[2])

if a+b>c and b+c>a and a+c>b:
    print("Z tych bokow mozna zbudowac trojkat")
else:
    print("Z tych bokow nie mozna zbudowac trojkata")
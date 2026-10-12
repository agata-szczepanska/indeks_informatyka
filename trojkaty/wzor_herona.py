from math import sqrt #UWAGA inny sposob na sqrt, mozna by bylo tez zwyczajnie: "import math" na poaczatku a potem math.sqrt()

a = float(input("podaj dlugosc boku a: "))
b = float(input("podaj dlugosc boku b: "))
c = float(input("podaj dlugosc boku c: "))

if a + b > c and b + c > a and a + c > b:
    p = (a + b + c)/2
    pole = sqrt(p*(p-a)*(p-b)*(p-b)*(p-c))
    print(f"Pole trojkata wynosi:{pole:.2f}")
else:
    print("z tych bokow nie mozna utworzyc trojkata")
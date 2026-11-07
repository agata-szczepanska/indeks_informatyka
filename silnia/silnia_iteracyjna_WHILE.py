def silnia_iteracyjna(n):
    wynik=1
    i=2
    while i<=n:
        wynik = wynik *i
        i+=1
    return wynik

n = int(input("podaj n: "))
print(f"{n}! = {silnia_iteracyjna(n)}")
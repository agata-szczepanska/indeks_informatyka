def silna_rekurencyjna(n):
    if n <=1:
        return 1
    return n * silna_rekurencyjna(n-1)

n = int(input("podaj n: "))
print(f"{n}! = {silna_rekurencyjna(n)}")

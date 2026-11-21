#Napisz program z użyciem funkcji wbudowanych.

liczby = []
with open("liczby.txt", "r", encoding="utf-8") as plik:
    for linia in plik:
        linia = linia.strip()
        if linia != "":
            liczby.append(int(linia))

print("min= ", min(liczby))
print("max= ", max(liczby))

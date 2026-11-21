#Program bez funkcji wbudowanych: znajdź minimum, policz oddalenia od początku i od końca, wypisz wniosek.
#Przyjmujemy: jeśli wartość leży na indeksie i od zera w tablicy o dlugosci n to:
# oddalenie_od_poczatku = i
# oddalenie_od_konca = n-1 -i
#Mniejsze oddalenie oznacza bliższy brzeg — i krótszą drogę skanu do pierwszego trafienia w tę wartość.


liczby = []
with open("liczby.txt", "r", encoding="utf-8") as plik:
    for linia in plik:
        linia = linia.strip()
        if linia != "":
            liczby.append(int(linia))

n = len(liczby)
min = liczby[0]
indeks_min = 0

for i in range(1,n):
    if liczby[i]<min:
        min=liczby[i]
        indeks_min=i

od_poczatku = indeks_min
od_konca = n-1-indeks_min

print("min =", min)
print("indeks =", indeks_min)
print("oddalenie od początku =", od_poczatku)
print("oddalenie od końca    =", od_konca)

if od_poczatku<od_konca:
    print("wniosek: min jest blizej poczatku")
elif od_poczatku>od_konca:
    print("wniosek: min jest blizej konca")
else:
    print("wniosek: rowne oddalenia - min w sorku lezy")

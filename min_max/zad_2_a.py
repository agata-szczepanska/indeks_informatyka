#Napisz program, który znajdzie najmniejszą i największą  w pliku  liczby.txt — 100 liczb całkowitych, każda w osobnym wierszu - liczbę bez funkcji wbudowanych.

liczby = []
with open("liczby.txt", "r", encoding="utf-8") as plik:
    for linia in plik:
        linia = linia.strip()
        if linia != "":
            liczby.append(int(linia))

n = len(liczby)
min = liczby[0]
max = liczby[0]

for i in range(1, n):
    if liczby[i]<min:
        min=liczby[i]
    if liczby[i]>max:
        max=liczby[i]

print("min= ", min)
print("max= ", max)

#Napisz program, który znajdzie min i max z użyciem sortowania.

liczby = []
with open("liczby.txt", "r", encoding="utf-8") as plik:
    for linia in plik:
        linia = linia.strip()
        if linia != "":
            liczby.append(int(linia))

liczby.sort() #posortuje rosnaco, gdybysmy chcieli posortowac malejaco to bysmy napisali liczby.sort(reverse=True)
print("min= ", liczby[0]) #pierwszy element listy
print("max= ", liczby[-1]) #ostatni element listy (dla przypomnienia przedostani ma indeks -2, przed przed ostatni ma indeks -3 itd)
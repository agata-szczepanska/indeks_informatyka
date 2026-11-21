#Napisz program w Pythonie lub C++ bez użycia funkcji wbudowanych min/max.

A = [47, 12, 65, 3, 28, 91, 17, 54, 8, 73, 35, 60, 22, 41, 5, 88, 19, 76, 14, 50]

n = len(A) #po prostu dlugpsc zbioru A
min = A[0]
max = A[0]

for i in range (1, n):
    if A[i]<min:
        min = A[i]
    if A[i]>max:
        max = A[i]

print("min= ", min)         #tutaj zapisuje tego printa w ten sposob, bo chce wypisac zmienna a nie funkcje dlatego bez f i bez {}
print("max= ", max)
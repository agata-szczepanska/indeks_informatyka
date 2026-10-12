def pole_troj(A, B, C):

    xA, yA = A
    xB, yB = B
    xC, yC = C


    pole = 0.5 * abs(xA*(yB-yC)+xB*(yC-yA)+xC*(yA-yB))
    return pole


A = (1, 2)
B = (4, 6)
C = (5, 2)

print(f"Pole trojkata wynosi: {pole_troj(A, B, C)}")
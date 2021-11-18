A = int(input("Nilai a : "))
B = int(input("Nilai b : "))
C = int(input("Nilai c : "))
D = (B * B) - (4 * A * C)
E = (-B + D / 2) / 2 * A
F = (-B - D / 2) / 2 * A
if D<0 :
    print("Fungsi tersebut tidak memiliki akar riil")
elif D>0 :
    print("Akar akar dari persamaan tersebut adalah" , F,"dan", E)
else :
    print("Fungsi tersebut memiliki akar kembar yaitu" , E)
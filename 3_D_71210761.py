A = input("Masukan daftar belanja : ").title().split(",")
print("Daftar belanja :",A)
B = input("Masukan barang yang ingin ditambahkan : ").lower()
if B.title() in A: print("Barang",B.upper(),"sudah berada dalam daftar belanja")
else:
    A.append(B.title())
    print("Hasil penambahan pada daftar belanja",A)
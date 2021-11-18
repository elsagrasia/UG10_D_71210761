a = int(input("Harga makanan sebesar RP "))
b = int(input("Harga snack sebesar Rp "))
c = int(input("Harga minuman sebesar Rp "))
d = int(input("Uang yang anda bawa sebesar Rp "))
e = a+b+c
total = d-e
if d<e:
    print("Total yang harus anda bayar sebesar Rp", e)
    print("Uang anda kurang! Anda memiliki hutang sebesar Rp", total*-1)
elif d>e:
    print("Total yang harus anda bayar sebesar Rp", e)
    print("Anda memiliki kembalian sebesar Rp", total)
else:
    print("Total yang harus anda bayar sebesar Rp", e)
    print("Uang anda pas! Tidak ada kembalian dan Utang :D")
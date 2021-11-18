num_1 = int(input("Masukkan bilangan 1 : "))
num_2 = int(input("Masukkan bilangan 2 : "))
num_3 = int(input("Masukkan bilangan 3 : "))
if num_1 > num_2 > num_3:
    print("Urutan bilangan dari yang terbesar adalah",num_1,num_2,num_3)
elif num_2 > num_1 > num_3:
    print("Urutan bilangan dari yang terbesar adalah",num_2,num_1,num_3)
elif num_2 > num_3 > num_1:
    print("Urutan bilangan dari yang terbesar adalah",num_2,num_3,num_1)
elif num_3 > num_1 > num_2:
    print("Urutan bilangan dari yang terbesar adalah",num_3,num_1,num_2)
elif num_3 > num_2 > num_1:
    print("Urutan bilangan dari yang terbesar adalah",num_3,num_2,num_1)
elif num_1 > num_3 > num_2:
    print("Urutan bilangan dari yang terbesar adalah",num_1,num_3,num_2)
elif num_1 == num_2 > num_3:
    print("Urutan bilangan dari yang terbesar adalah",num_1,num_2,num_3)
elif num_1 > num_2 == num_3:
    print("Urutan bilangan dari yang terbesar adalah",num_1,num_2,num_3)
elif num_3 > num_1 == num_2:
    print("Urutan bilangan dari yang terbesar adalah",num_3,num_1,num_2)
elif num_1 == num_3 > num_2:
    print("Urutan bilangan dari yang terbesar adalah",num_1,num_3,num_2)
elif num_3 == num_2 > num_1:
    print("Urutan bilangan dari yang terbesar adalah",num_3,num_2,num_1)
elif num_2 > num_1 == num_3:
    print("Urutan bilangan dari yang terbesar adalah",num_2,num_1,num_3)
elif num_1 > num_3 == num_2:
    print("Urutan bilangan dari yang terbesar adalah",num_1,num_3,num_2)
else:
    num_1 == num_2 == num_3
    print("Urutan bilangan dari yang terbesar adalah",num_1,num_2,num_3)
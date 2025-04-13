<<<<<<< HEAD
# TRIANGLE MAKER
print(10*":",'Triangle',10*":")

alas =  int(input("Masukkan Alas : "))
spasi = int(alas / 2)
count = 1

while True:
    if count%2 != 0:
        print(" "*spasi,'^'*count)
        count += 1
    else:
        count += 1
        spasi -= 1

    if count > alas:
        break
=======
# TRIANGLE MAKER
print(10*":",'Triangle',10*":")

alas =  int(input("Masukkan Alas : "))
spasi = int(alas / 2)
count = 1

while True:
    if count%2 != 0:
        print(" "*spasi,'^'*count)
        count += 1
    else:
        count += 1
        spasi -= 1

    if count > alas:
        break
>>>>>>> cd1aaeb9d87aeb86de2fca0ed17417b15189fc16
        
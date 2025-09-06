# global scope adalah cara mengambil variabel dari environment global ke dlm fungsi

name_global = 'Rei' # <-- global variable (bisa diakses di mana pun)

## akses
def cetakG():
    print(f"{name_global} merupakan variabel global")
cetakG()

def cetakL():
    name_local = 'Yui' # <-- local variable (hnya dpt diakses di dlm fungsi deklarasi)
    print(f"{name_local} merupakan variabel local")
cetakL()


## ubah
def ubahG(): # selain dari parameter dn argumen kita bisa memasukkan var dgn global 
    global varG # mengakses varG
    varG = 'Rutera'
    return varG

varG = 'Elair'
print(f"Sebelum : {varG}")
print(f"Sesudah : {ubahG()}")


## var local di if dan for bisa diakses
num = 0
for nums in range(0,7):
    num += nums
    numD = 99

print(num)
print(numD)


if True:
    num = 111
    numD = 999

print(num)
print(numD)

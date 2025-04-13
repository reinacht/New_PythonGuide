# packages adalah modules modules file .py
# cara importnya
# __init__.py adalah file yang akan otomatis menjalankan/menginisiasikan perintah di dalam modules/packages
# file ini akan langsung mengembalikan fungsi yang tinggal dipanggil

## import
import init_basic


# basic pack
num1 = init_basic.times(3, 90)
print(num1)

num2 = init_basic.floor_division(10, 6)
print(num2)

num3 = init_basic.plus(3, 90)
print(num3)

square5 = init_basic.square(5)
num4 = square5(10)
print(num4)


## Fisika pack
hambatan1 = init_basic.resistant1(12, 0.5)
print(hambatan1)

hambatan2 = init_basic.resistant2(1.68e-8, 2, 10e-6)
print(hambatan2)

pressure = init_basic.pressure(75, 25)
print(pressure)

weight = init_basic.weight(62)
print(weight)

force = init_basic.force(250, 5)
print(force)






## pers lingkaran
# persLing = input("Masukkan Persamaan Lingkaran : ")
# init_basic.circle(persLing) # fungsi circle ada di circle.py (lihatlah kontol biar paham)

def twoCircles(cir1, cir2):
    import math

    ## 1. lingkaran 1
    print("="*50)
    a = int(input("\nMasukkan Nilai a1 : "))
    b = int(input("Masukkan Nilai b1 : "))
    c = int(input("Masukkan Nilai c1 : "))
    print("\nHasil")
    print(f"Lingkaran 1 : {cir1}")


    a1 = int((1/2) * a)
    b1 = int((1/2) * b)
    centre1 = a1, b1 # pusat
    centA = a1 + b1

    print(f"Pusat A : {centre1}")
    r1 = int(math.sqrt((1/2 * a)**2 + (1/2 * b)**2 - c)) # jari jari
    print(f"r1 : {r1}")


    ## 2. lingkaran 2
    print("="*50)
    a = int(input("\nMasukkan Nilai a2 : "))
    b = int(input("Masukkan Nilai b2 : "))
    c = int(input("Masukkan Nilai c2 : "))
    print("\nHasil")
    print(f"Lingkaran 2 : {cir2}")


    a2 = int((1/2) * a)
    b2 = int((1/2) * b)
    centre2 = a2, b2 # pusat
    centB = a2 + b2

    print(f"Pusat B : {centre2}")
    r2 = int(math.sqrt((1/2 * a)**2 + (1/2 * b)**2 - c)) # jari jari
    print(f"r1 : {r2}")


    ## 3. centre and r
    print("="*50)
    centres = (centA) * (centB)
    rState1 = r1 + r2
    rState2 = r1 - r2

    print(f"\nAB = {centres}")
    print(f"r1 + r2 = {rState1}")
    print(f"r1 - r2 = {rState2}")
    
    ## 5. logics
    print("="*50)
    if centres < rState1 or rState2:
        print("Dua Lingkaran Saling Berpotongan")
        print("AB < r1 + r2 atau AB < r1 - r2")
    
    elif centres == rState1:
        print("Dua Lingkaran Bersinggungan Luar")
        print("AB = r1 + r2")

    elif centres == rState2:
        print("Dua Lingkaran Bersinggungan Dalam")
        print("AB = r1 - r2")

    elif centres > rState1:
        print("Dua Lingkaran Tidak Bersinggungan Luar")
        print("AB > r1 + r2")

    elif centres > rState2:
        print("Dua Lingkaran Tidak Bersinggungan Dalam")
        print("AB > r1 - r2")

    else:
        print("Kedudukannya Ganda")
    print("="*50)

c1 = input("Masukkan Lingkaran 1 : ")
c2 = input("Masukkan Lingkaran 2 : ")

twoCircles(c1, c2)


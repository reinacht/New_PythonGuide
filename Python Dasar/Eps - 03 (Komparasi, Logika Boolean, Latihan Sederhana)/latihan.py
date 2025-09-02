<<<<<<< HEAD
# latihan komparasi dan logika sederhana boolean
# 1
print("====SOAL_1====")
num = int(input("Masukkan Angka : "))

val_true1 = num > 0 and num < 5
val_true2 = num > 8 and num < 11

val_end = val_true1 or val_true2
print(val_true1, "dan", val_true2, ":", val_end)


# 2
print("====SOAL_2====")
num = int(input("Masukkan Angka : "))

val_true1 = num < 0 
val_true2 = num > 5 and num < 8
val_true3 = num > 11

val_end = val_true1 or val_true2 or val_true3
print(val_true1, "dan", val_true2, " dan", val_true3, ":", val_end)

>>>>>>> cd1aaeb9d87aeb86de2fca0ed17417b15189fc16

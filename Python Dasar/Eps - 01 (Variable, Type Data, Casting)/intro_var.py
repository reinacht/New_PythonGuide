<<<<<<< HEAD
# beberapa shortcut vscode
# ALT + Shift + PgDown

# 01 variabel hanya dideklarasikan dengan simpel
a = 10
print(a)


#  02 type data yang umum di python ada 4, tetapi ada tipe khusus yaitu Bil.Kompleks 
# dan data yang bisa menggunakan type data C dengan Import Library ()


# 4 data tipe utama dalam pyhton
print("===Integer===")
a = 7
print("Tipe data dari :", a ,"adalah", type(a))

print("===String===")
b = "7"
print("Tipe data dari :", b ,"adalah", type(b))

print("===Float===")
c = 7.7
print("Tipe data dari :", c ,"adalah", type(c))

print("===Boolean===")
d = True
print("Tipe data dari :", d ,"adalah", type(d))


# tipe khusus (bil.kompleks dan tipe bahasa C)
print("===Complex===")
data_complex = complex(7,9)
print("Tipe data dari :", data_complex ,"adalah", type(data_complex))


from ctypes import c_double # import 
print("===C-Type===")
data_c = c_double(7.9)
print("Tipe data dari :", data_c ,"adalah", type(data_c))




# 03 casting data adalah mengubah tipe data dari satu ke lainnya (tergantung value)
# INTEGER 
d_int = 9
print("=====Integer_Casting=====")
print(d_int, "bertipe :", type(d_int))

d_str   = str(d_int)
d_float = float(d_int)
d_bool  = bool(d_int) # bool menjadi false ketika value = 0
print(d_str, "bertipe :", type(d_str))
print(d_float, "bertipe :", type(d_float))
print(d_bool, "bertipe :", type(d_bool))

#STRING
d_str = "9"
print("=====String_Casting=====")
print(d_str, "bertipe :", type(d_str))

d_int   = int(d_str)
d_float = float(d_str)
d_bool  = bool(d_str) # bool menjadi false ketika value = " " (kosong)
print(d_int, "bertipe :", type(d_int))
print(d_float, "bertipe :", type(d_float))
print(d_bool, "bertipe :", type(d_bool))


#FLOAT
d_float = 9.5 
print("=====Float_Casting=====")
print(d_float, "bertipe :", type(d_float))

d_str = str(d_float)
d_int   = int(d_float) # dibulatkan kebawah
d_bool  = bool(d_float) # bool menjadi false ketika value = 0
print(d_str, "bertipe :", type(d_str))
print(d_int, "bertipe :", type(d_int))
print(d_bool, "bertipe :", type(d_bool))


#BOOLEAN
d_bool = True
print("=====Boolean_Casting=====")
print(d_bool, "bertipe :", type(d_bool))

d_str  = str(d_bool) 
d_int   = int(d_bool) # bool menjadi 1 ketika True, jadi 0 ketika false
d_float = float(d_bool) # bool menjadi 1.0 ketika True, jadi 0 ketika false
print(d_str, "bertipe :", type(d_str))
print(d_int, "bertipe :", type(d_int))
print(d_float, "bertipe :", type(d_float)) 




=======
# beberapa shortcut vscode
# ALT + Shift + PgDown

# 01 variabel hanya dideklarasikan dengan simpel
a = 10
print(a)


#  02 type data yang umum di python ada 4, tetapi ada tipe khusus yaitu Bil.Kompleks 
# dan data yang bisa menggunakan type data C dengan Import Library ()


# 4 data tipe utama dalam pyhton
print("===Integer===")
a = 7
print("Tipe data dari :", a ,"adalah", type(a))

print("===String===")
b = "7"
print("Tipe data dari :", b ,"adalah", type(b))

print("===Float===")
c = 7.7
print("Tipe data dari :", c ,"adalah", type(c))

print("===Boolean===")
d = True
print("Tipe data dari :", d ,"adalah", type(d))


# tipe khusus (bil.kompleks dan tipe bahasa C)
print("===Complex===")
data_complex = complex(7,9)
print("Tipe data dari :", data_complex ,"adalah", type(data_complex))


from ctypes import c_double # import 
print("===C-Type===")
data_c = c_double(7.9)
print("Tipe data dari :", data_c ,"adalah", type(data_c))




# 03 casting data adalah mengubah tipe data dari satu ke lainnya (tergantung value)
# INTEGER 
d_int = 9
print("=====Integer_Casting=====")
print(d_int, "bertipe :", type(d_int))

d_str   = str(d_int)
d_float = float(d_int)
d_bool  = bool(d_int) # bool menjadi false ketika value = 0
print(d_str, "bertipe :", type(d_str))
print(d_float, "bertipe :", type(d_float))
print(d_bool, "bertipe :", type(d_bool))

#STRING
d_str = "9"
print("=====String_Casting=====")
print(d_str, "bertipe :", type(d_str))

d_int   = int(d_str)
d_float = float(d_str)
d_bool  = bool(d_str) # bool menjadi false ketika value = " " (kosong)
print(d_int, "bertipe :", type(d_int))
print(d_float, "bertipe :", type(d_float))
print(d_bool, "bertipe :", type(d_bool))


#FLOAT
d_float = 9.5 
print("=====Float_Casting=====")
print(d_float, "bertipe :", type(d_float))

d_str = str(d_float)
d_int   = int(d_float) # dibulatkan kebawah
d_bool  = bool(d_float) # bool menjadi false ketika value = 0
print(d_str, "bertipe :", type(d_str))
print(d_int, "bertipe :", type(d_int))
print(d_bool, "bertipe :", type(d_bool))


#BOOLEAN
d_bool = True
print("=====Boolean_Casting=====")
print(d_bool, "bertipe :", type(d_bool))

d_str  = str(d_bool) 
d_int   = int(d_bool) # bool menjadi 1 ketika True, jadi 0 ketika false
d_float = float(d_bool) # bool menjadi 1.0 ketika True, jadi 0 ketika false
print(d_str, "bertipe :", type(d_str))
print(d_int, "bertipe :", type(d_int))
print(d_float, "bertipe :", type(d_float)) 




>>>>>>> cd1aaeb9d87aeb86de2fca0ed17417b15189fc16

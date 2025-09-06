# string adalah sekumpulan char
read = "ini adalah string"
print(type(read))

# 1. Cara membuat String
text_1 = 'dengan single quote'
text_2 = "dengan double quote"

print(text_1)
print(text_2)
print("Hari ini adalah Hari Jum'at")



# 2. Menggunakan tanda \

# untuk membaca tanda ' atau "
print('Hari Jum\'at')

# untuk fungsi tab
print("Dekat \tJauh")
# untuk fungsi backspace
print("Dekat \bJauh")

# untuk newline
print("Baris 1\nBaris 2")
print("Baris 1\rBaris 2") # baris 1 jadi hilang
print("Baris 1\r\nBaris 2")

# untuk backslash \\
print("D:\\Project Code\\Python\\Eps - 04 (Bitwise Operator, Operator Assignment, String)")



# 3. Multiline dan Raw (GA BERPENGARUH)
print("""
Name     : Xery
Class    : XII - 2
Identity : Unknown
Age      : 99          
""")

print(r"Apapun itu \ndianggap \tstring jika ada r di depan, \n  ")

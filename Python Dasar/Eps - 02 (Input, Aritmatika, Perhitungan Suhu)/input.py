# input adalah fungsi untuk memasukkan nilai ke dalam variable melalui masukan dari user
# data yang dimasukkan pasti str, jadi perlu di casting jika tipenya tidak sesuai dengan yang diinginkan

# cnth
data_str = input("Masukkan data : ")
print("Data :", data_str)
print("Bertipe :", type(data_str))

# casting dulu ke int atau float untuk angka
data_angka = int(input("Masukkan angka : "))
print("Data :", data_angka)
print("Bertipe :", type(data_angka))

data_float = float(input("Masukkan angka : "))
print("Data :", data_float)
print("Bertipe :", type(data_float))

# casting dulu ke int lalu ke boolean (2 kali)
data_bool = bool(int(input("Masukkan angka : ")))
print("Data :", data_bool)
print("Bertipe :", type(data_bool))

# manipulasi string

# 1. Menyambung String (concatenate) 
nama_dpn = "Rei"
nama_blkng = "Ayanami"
full_name = nama_dpn + " " + nama_blkng

print("Nama Lengkapnya : ", full_name)

# 2. Mengukur panjang Str
name = "Lelouch VI Britannia"
length = len(name)
print("Panjang String : ", length)

# 3. Operator untuk Str

# cek ketersediaan
check = "VI" in name
print("Ketersediaan : ", check)
check = "Great" not in name
print("Ketersediaan : ", check)

# pengulangan
print("Wleo"*10)
print(15*"Rero")

# indexing
print("Index ke-0 : ", name[0])
print("Index ke-(-1) : ", name[-1])
print("Index ke-[0:6] : ", name[0:7]) # range index
print("Index ke-[0,2,4,6,8,10] :", name[0:11:2]) # index genap

# max-min item
print("Min : ", min(name))
print("Max : ", max(name))

# cek ascii
ascii_code = str(ord(" ")) 
print("ASCII Code utk spasi : ", ascii_code)
data = chr(170) 
print("Char utk 170 : ", data)


# 4. Metode Str
text = "kuku kaki kakak dan kakek adalah jumlah dari kuku kaki nenek"
count = text.count("k")
print("Jumlah huruf K dari kalimat", text, "adalah", count)

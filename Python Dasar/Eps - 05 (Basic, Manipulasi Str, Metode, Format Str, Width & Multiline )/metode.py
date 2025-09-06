# metode

## case changing

# to lower and upper
waifu = "Rei"
text = f"{waifu} : \"Ohayou Anata\"".lower()
print(text)

waifu = "Rei"
text = f"{waifu} : \"Ohayou Anata\"".upper()
print(text)

## pengecekan isX (hasil boolean)

# isalpha() : untuk mengecek semuanya huruf
# isalnum() : huruf dan angka
# isdecimal() : angka saja
# isspace() : spasi, newtab, newline
# istitle() : semua kata dimulai kapital

judul = "\"Rei Ayanami Is My Darling\""
check = judul.istitle()
print(judul, "is title : ", check)

## start and endwith
text_start = "Waifu is real!".startswith('Waifu')
text_end = "Waifu is real!".endswith('!')
print("Start : ", text_start)
print("End : ", text_end)


## join() and split()
random = ['Satu', 'adalah', 'angka']
join_text = ','.join(random)
print(random, "digabung : ", join_text)

join_text = 'p'.join(random)
print(random, "digabung : ", join_text)

join_text = ' '.join(random)
print(random, "digabung : ", join_text)

split_text = join_text.split()
print(split_text)


## aloklasi karakter rjust(), ljust(), center()
right = "'kanan'".rjust(15)
print("'"+right+"'")

left = "'kiri'".ljust(15)
print("'"+left+"'")

center = "'tengah'".center(15)
print("'"+center+"'")

center = "'tengah'".center(15, ";")
print("'"+center+"'")

# kebalikannya strip() : menghapus
strip = center.strip(";")
print("'"+strip+"'")

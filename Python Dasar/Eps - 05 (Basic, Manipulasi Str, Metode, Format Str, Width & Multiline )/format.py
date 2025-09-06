# format dalam str untuk efisiensi kode

# regular str
name1 = "Rei"
name2 = "Ayanami"
name3 = name1 + "" + name2
print(name3)

# efisien = f"STRING {var}"
name2 = "Sinora"
name2 = f"Sinus {name2}"
print(name2)


# angka
num = 234.6
f_str = f"Angka = {num}"
print(f_str)

num = 234.656
f_str = f"Angka = {num:.2f}" # angka belakang koma
print(f_str)

num = 234.6433457
f_str = f"Angka = {num:7.2f}" # total char / leading zero
print(f_str)

num = 1000000
f_str = f"Angka = {num:,}" # ngasih koma
print(f_str)

num = -77
f_str = f"Angka = {num:+d}" # ngasih -+
print(f_str)

num = 77
f_str = f"Angka = {num:+d}"
print(f_str)


# boolean
state = True
f_str = f"Kondisi = {state}"
print(f_str)


# persentase
percent = 0.875
f_str = f"Nilai {percent} diubah menjadi persen = {percent:%}"
print(f_str)

# aritmatika
hutang = 150000
bunga = (12 * 0.02) + 1
f_str = f"Hutang Milik si A adalah sebesar : {hutang*bunga:,}"
print(f_str)

# angka lain (binary, octal, hexadesimal)
while True:
    num = int(input("Masukkan : "))
    f_strb = f"Binary : {format(num,'08b')}"
    f_stro = f"Octal : {format(num,'o')}"
    f_strh = f"Hex : {format(num,'#x')}"
    print(f_strb)
    print(f_stro)
    print(f_strh)

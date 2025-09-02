<<<<<<< HEAD
# Witdh and Multiline

# Data
name = "Hizuyuki"
age = 77
gender = "Netral"
height = 190
weight = 70
time = str(input("Masukkan Waktu : "))

# Standard String
profile_user = f"Hai {name}, Selamat {time}. Berikut ini data pribadi Anda : Umur ({age}), Jenis Kelamin ({gender}), Tinggi ({height}), Berat Badan ({weight})"
print(profile_user)

# Multiline with /n
profile_user = f"\nHai {name}, \nSelamat {time}. \nBerikut ini data pribadi Anda : \nUmur ({age}), \nJenis Kelamin ({gender}), \nTinggi ({height}), \nBerat Badan ({weight})"
print(profile_user)

# Multiline with Triplets
profile_user = f"""\nHai {name}, Selamat {time}. 
Berikut ini data pribadi Anda : 
    Umur ({age})
    Jenis Kelamin ({gender})
    Tinggi ({height})
    Berat Badan ({weight})"""
print(profile_user)


# Width Order
profile_user = f"""\nHai {name}, Selamat {time:}. 
Berikut ini data pribadi Anda : 
    Umur : {age:>15}
    Jenis Kelamin : {gender:>10}
    Tinggi : {height:>15}
    Berat Badan : {weight:>10}"""
print(profile_user)

>>>>>>> cd1aaeb9d87aeb86de2fca0ed17417b15189fc16

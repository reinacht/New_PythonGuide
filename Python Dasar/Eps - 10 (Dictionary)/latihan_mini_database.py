<<<<<<< HEAD
import datetime as dt
import os

os.system('cls')
persons_data = {}
inte = 0

while True:
    # Template dict
    inte += 1
    toSTR = str(inte)
    person_template = {
        'nama': 'nama', 
        'umur': 0,
        'kota': 'kota', 
        'warna_kulit': 'warna_kulit', 
        'status' : 'status',
        'lahir': dt.date(1111, 1, 11)
    }
    
    print("Masukkan Inputan\n") 
    person = dict.fromkeys(person_template.keys())

    person['nama'] = input("Masukkan Nama : ")
    person['umur'] = int(input("Masukkan Umur : "))
    person['kota'] = input("Masukkan Kota Asal : ")
    person['warna_kulit'] = input("Masukkan Warna Kulit : ")
    person['status'] = input("Masukkan Status : ")

    # Tanggal Lahir
    YEARS = int(input("Masukkan Tahun Lahir : "))
    MONTHS = int(input("Masukkan Bulan Lahir : "))
    DAYS = int(input("Masukkan Tanggal : ")) 

    birth = dt.date(YEARS, MONTHS, DAYS)
    birth_str = birth.strftime("%Y-%m-%d")
    person['lahir'] = birth_str
    persons_data[toSTR] = person
    print(persons_data)

    print("\n","="*40, "MINI DATABASE", "="*40)
    print(f"{'NO':<3} {'NAMA':<25} {'UMUR':<5} {'KOTA':<16} {'KULIT':<16} {'STATUS':<16} {'LAHIR':<10}")
    
    for key, values in persons_data.items():
        print(f"{key:<3} {values['nama']:<25} {values['umur']:<5} {values['kota']:<16} {values['warna_kulit']:<16} {values['status']:16} {values['lahir']:<10}")
    

    condition1 = input("Mau hapus? y/n : ")
    if condition1 == 'y':
        key = input("Masukkan key data yang ingin dihapus : ")
        persons_data.pop(key)
    
    condition2 = input("Mau nambah? y/n : ")
    if condition2 == 'n':
        print("\n","="*40, "PROGRAM SELESAI", "="*40)
        break
=======
import datetime as dt
import os

os.system('cls')
persons_data = {}
inte = 0

while True:
    # Template dict
    inte += 1
    toSTR = str(inte)
    person_template = {
        'nama': 'nama', 
        'umur': 0,
        'kota': 'kota', 
        'warna_kulit': 'warna_kulit', 
        'status' : 'status',
        'lahir': dt.date(1111, 1, 11)
    }
    
    print("Masukkan Inputan\n") 
    person = dict.fromkeys(person_template.keys())

    person['nama'] = input("Masukkan Nama : ")
    person['umur'] = int(input("Masukkan Umur : "))
    person['kota'] = input("Masukkan Kota Asal : ")
    person['warna_kulit'] = input("Masukkan Warna Kulit : ")
    person['status'] = input("Masukkan Status : ")

    # Tanggal Lahir
    YEARS = int(input("Masukkan Tahun Lahir : "))
    MONTHS = int(input("Masukkan Bulan Lahir : "))
    DAYS = int(input("Masukkan Tanggal : ")) 

    birth = dt.date(YEARS, MONTHS, DAYS)
    birth_str = birth.strftime("%Y-%m-%d")
    person['lahir'] = birth_str
    persons_data[toSTR] = person
    print(persons_data)

    print("\n","="*40, "MINI DATABASE", "="*40)
    print(f"{'NO':<3} {'NAMA':<25} {'UMUR':<5} {'KOTA':<16} {'KULIT':<16} {'STATUS':<16} {'LAHIR':<10}")
    
    for key, values in persons_data.items():
        print(f"{key:<3} {values['nama']:<25} {values['umur']:<5} {values['kota']:<16} {values['warna_kulit']:<16} {values['status']:16} {values['lahir']:<10}")
    

    condition1 = input("Mau hapus? y/n : ")
    if condition1 == 'y':
        key = input("Masukkan key data yang ingin dihapus : ")
        persons_data.pop(key)
    
    condition2 = input("Mau nambah? y/n : ")
    if condition2 == 'n':
        print("\n","="*40, "PROGRAM SELESAI", "="*40)
        break
>>>>>>> cd1aaeb9d87aeb86de2fca0ed17417b15189fc16
    
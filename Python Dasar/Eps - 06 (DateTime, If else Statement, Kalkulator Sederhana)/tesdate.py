from datetime import datetime, date

# Tampilkan tanggal hari ini
today = date.today()
print(f"Hari ini : {today}")

# Input tanggal lahir
print("\nMasukkan Tanggal Lahir")
day = int(input("Hari : "))
month = int(input("Bulan : "))
years = int(input("Tahun : "))

# Buat objek tanggal dari inputan
date_of_birth = date(years, month, day)
print(f"Tanggal Lahir : {date_of_birth}")
print(f"Hari Lahir : {date_of_birth:%A}")

# Hitung umur
age = today - date_of_birth
print(f"\nUmur Anda : {age.days} hari")

# Konversi umur ke tahun, bulan, dan hari
years_birth = age.days // 365
month_birth = (age.days % 365) // 30
day_birth = (age.days % 365) % 30

# Tampilkan umur dalam tahun, bulan, dan hari
print(f"Umur Anda Secara Detail : \n{years_birth} Tahun, {month_birth} Bulan, {day_birth} Hari")

# Tampilkan waktu saat ini
current_time = datetime.now()
print(f"Jam Saat Ini : {current_time.strftime('%H:%M:%S')}")

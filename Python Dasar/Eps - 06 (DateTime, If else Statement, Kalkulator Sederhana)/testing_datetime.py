# Import Library Datetime
# Program Tanggal Sederhana
from datetime import datetime
import datetime as dt

today = dt.date.today()
print(f"Hari ini : {today}")

# Inputan
print("\nMasukkan Tanggal")
day = int(input("Hari : "))
month = int(input("Bulan : "))
years = int(input("Tahun : "))

date_dynamic = dt.date(years,month,day)
print(f"Tanggalnya : {date_dynamic}")
print(f"Harinya : {date_dynamic:%A}")

age = today - date_dynamic
print(f"\nUmur Anda : {age}")

years_birth = age.days // 365
month_birth = (age.days % 365) // 30
day_birth = age.days % 30

# Jam, Menit, Detik
current_time = datetime.now()
hours = int(current_time.strftime("%H")) 
hours = hours

time = current_time.strftime(f"{hours} Jam, %M Menit, %S Detik")
print(f"Umur Anda Secara Detail : \n{years_birth} Tahun, {month_birth} Bulan, {day_birth} Hari. {time}")

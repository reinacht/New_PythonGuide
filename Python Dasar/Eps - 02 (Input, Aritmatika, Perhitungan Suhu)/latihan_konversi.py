# latihan konversi satuan

# celcius ke lainnya
print("\n=======Celcius=======\n")
celcius = float(input('Masukkan derajat Celcius : '))


reamur = (4 / 5) * celcius
print('Dalam Reamur : ', reamur)

fahrenheit = (9 / 5) * celcius + 32
print('Dalam Fahrenheit : ', fahrenheit)

kelvin = celcius + 273
print('Dalam Kelvin : ', kelvin)



# reamur ke lainnya
print("\n=======Reamur=======\n")
reamur = float(input('Masukkan derajat Reamur : '))


celcius = (5 / 4) * reamur
print('Dalam Celcius : ', celcius)

fahrenheit = (9 / 4) * reamur + 32
print('Dalam Fahrenheit : ', fahrenheit)

kelvin = (5 / 4) * reamur + 273
print('Dalam Kelvin : ', kelvin)



# fahrenheit ke lainnya
print("\n=======Fahrenheit=======\n")
fahrenheit = float(input('Masukkan derajat Fahrenheit : '))


celcius = (5 / 9) * (fahrenheit - 32)
print('Dalam Celcius : ', celcius)

reamur = (4 / 9) * (fahrenheit - 32)
print('Dalam Reamur : ', reamur)

# ubah ke celcius dulu kalau kelvin
kelvin = (5 / 9) * (fahrenheit - 32)
kelvin = kelvin + 273
print('Dalam Kelvin : ', kelvin)



# kelvin ke lainnya
print("\n=======Kelvin=======\n")
kelvin = float(input('Masukkan derajat Kelvin : '))


celcius = kelvin - 273
print('Dalam Celcius : ', celcius)

reamur = (4 / 5) * (kelvin - 273)
print('Dalam Reamur : ', reamur)

# ubah ke celcius dulu kalau fahrenheit
fahrenheit = kelvin - 273 
fahrenheit = (9 / 5) * fahrenheit + 32

print('Dalam Fahrenheit : ', fahrenheit)

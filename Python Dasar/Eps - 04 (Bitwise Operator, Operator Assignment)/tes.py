<<<<<<< HEAD
""" a = 7
b = 7
c = a ^ b
print(a,"^",b,"=",c)
print(format(a,'08b'))
print(format(b,'08b'))
print('_______________ (^)')
print(format(c,'08b'))
 """

# kalkulator bitwise
print("\n======= Kalkulator Bitwise =======")
num_one = int(input("Masukkan Angka Pertama : "))
reg_o = str(input("Masukkan Operasi Biasa (+, -, , /, *, //, %) : "))
bit_o = str(input("Masukkan Operasi Bitwise (|, ^, &, ~, ^^) : "))
num_two = int(input("Masukkan Angka Kedua : "))

# logic

def regular_operations(num_one, num_two, reg_o):
    if reg_o == '+':
        result = num_one + num_two
    elif reg_o == '-':
        result = num_one - num_two
    elif reg_o == '*':
        result = num_one * num_two
    elif reg_o == '/':
        result = num_one / num_two
    elif reg_o == '**':
        result = num_one ** num_two
    elif reg_o == '//':
        result = num_one // num_two
    elif reg_o == '%':
        result = num_one % num_two
    print("Hasil Operasi Biasa dari", num_one, reg_o, num_two, "=", result)

def bit_operations(num_one, num_two, bit_o):
    if bit_o == '|':
        result = num_one | num_two
    elif bit_o == '^':
        result = num_one ^ num_two
    elif bit_o == '&':
        result = num_one & num_two
    elif bit_o == '~':
        result = ~num_one
    elif bit_o == '^^':
        x = 0b11111111
        result = num_one ^ x

    if bit_o == '~' or bit_o == '^^':
        print("Hasil Operasi Bitwise dari", bit_o, num_one, "=", result)
        print(format(num_one, '08b'))
        print("_________", "(", bit_o, ")")
        print(format(result, '08b'))
    else:
        print("Hasil Operasi Bitwise dari", num_one, bit_o, num_two, "=", result)
        print(format(num_one, '08b'))
        print(format(num_two, '08b'))
        print("_________", "(", bit_o, ")")
        print(format(result, '08b'))

if reg_o in ['+', '-', '', '/', '*', '//', '%']:
    regular_operations(num_one, num_two, reg_o)
if bit_o in ['|', '^', '&', '~', '^^']:
=======
""" a = 7
b = 7
c = a ^ b
print(a,"^",b,"=",c)
print(format(a,'08b'))
print(format(b,'08b'))
print('_______________ (^)')
print(format(c,'08b'))
 """

# kalkulator bitwise
print("\n======= Kalkulator Bitwise =======")
num_one = int(input("Masukkan Angka Pertama : "))
reg_o = str(input("Masukkan Operasi Biasa (+, -, , /, *, //, %) : "))
bit_o = str(input("Masukkan Operasi Bitwise (|, ^, &, ~, ^^) : "))
num_two = int(input("Masukkan Angka Kedua : "))

# logic

def regular_operations(num_one, num_two, reg_o):
    if reg_o == '+':
        result = num_one + num_two
    elif reg_o == '-':
        result = num_one - num_two
    elif reg_o == '*':
        result = num_one * num_two
    elif reg_o == '/':
        result = num_one / num_two
    elif reg_o == '**':
        result = num_one ** num_two
    elif reg_o == '//':
        result = num_one // num_two
    elif reg_o == '%':
        result = num_one % num_two
    print("Hasil Operasi Biasa dari", num_one, reg_o, num_two, "=", result)

def bit_operations(num_one, num_two, bit_o):
    if bit_o == '|':
        result = num_one | num_two
    elif bit_o == '^':
        result = num_one ^ num_two
    elif bit_o == '&':
        result = num_one & num_two
    elif bit_o == '~':
        result = ~num_one
    elif bit_o == '^^':
        x = 0b11111111
        result = num_one ^ x

    if bit_o == '~' or bit_o == '^^':
        print("Hasil Operasi Bitwise dari", bit_o, num_one, "=", result)
        print(format(num_one, '08b'))
        print("_________", "(", bit_o, ")")
        print(format(result, '08b'))
    else:
        print("Hasil Operasi Bitwise dari", num_one, bit_o, num_two, "=", result)
        print(format(num_one, '08b'))
        print(format(num_two, '08b'))
        print("_________", "(", bit_o, ")")
        print(format(result, '08b'))

if reg_o in ['+', '-', '', '/', '*', '//', '%']:
    regular_operations(num_one, num_two, reg_o)
if bit_o in ['|', '^', '&', '~', '^^']:
>>>>>>> cd1aaeb9d87aeb86de2fca0ed17417b15189fc16
    bit_operations(num_one, num_two, bit_o)
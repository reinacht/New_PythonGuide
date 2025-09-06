# bitwise operator : operasi khusus antara bilangan biner
# cara baca biner 

biner = 0b00001000
print("Nilai : ", biner, "merupakan biner dari : ", format(biner, '08b'))

# biner terdiri dari 8 angka atau lebih
# 00000000 
# 76543210 (indeks) dan merupakan bilangan pangkat 2 dimulai dari 2**0 (lihat angka 1)
# jika angka 1 lebih dari dua maka dijumlahkan



# Operator OR = (|)
# sama seperti OR, bedanya 0 dan 1 di biner mempresentasikan False dan True
print("========OR(|)========")
a = 10
b = 7
a_bin = format(a,'08b') 
b_bin = format(b,'08b') 

res = a | b
print(a, "|", b, "=", res)
print("Biner a : ", a_bin)
print("Biner b : ", b_bin)
print("_____________________ (|)")
print("Hasil   : ", format(res,'08b'))

# Operator XOR = (^)
# sama seperti XOR, bedanya 0 dan 1 di biner mempresentasikan False dan True
print("\n========XOR(^)========")
a = 10
b = 7
a_bin = format(a,'08b') 
b_bin = format(b,'08b') 

res = a ^ b
print(a, "^", b, "=", res)
print("Biner a : ", a_bin)
print("Biner b : ", b_bin)
print("_____________________ (^)")
print("Hasil   : ", format(res,'08b'))

# Operator AND = (&)
# sama seperti AND, bedanya 0 dan 1 di biner mempresentasikan False dan True
print("\n========AND(&)========")
a = 10
b = 7
a_bin = format(a,'08b') 
b_bin = format(b,'08b') 

res = a & b
print(a, "&", b, "=", res)
print("Biner a : ", a_bin)
print("Biner b : ", b_bin)
print("_____________________ (&)")
print("Hasil   : ", format(res,'08b'))

# Operator NOT = (~)
# sama seperti AND, bedanya 0 dan 1 di biner mempresentasikan False dan True
print("\n========NOT(~)========")
a = 10
a_bin = format(a,'08b') 

res = ~a # sedikit tricky, -11 hasilnya (dengan positif negatif)
print(a, "~", b, "=", res)
print("Biner a : ", a_bin)
print("_____________________(~)")
print("Hasil   : ", format(res,'08b'))

# cara agar bekerja seperti NOT asli (0 akan selalu menjadi 1 dan sebaliknya) dengan menggunakan XOR

x = 0b00001010
y = 0b11111111
res = x ^ y
print(x, "^", y, "=", res)
print("Biner x : ", format(x, '08b'))
print("Biner y : ", format(y, '08b'))
print("_____________________ (NOT^)")
print("Hasil   : ", format(res,'08b'))

<<<<<<< HEAD
# komparasi ada 8 : < , > , <= , >= , == ,!= , is , is not

# notes : is dan is not hanya bisa digunakan ketika membandingkan object id 
# (harus variabel yang punya value, tapi di py 3.10+ bisa)


# (<) : sama seperti di matematika [kurang dari]
print("====(<)====")
a = 3
b = 7
res1 = a < b # True
res2 = b < a # False
print(a, "<", b, ":", res1)
print(b, "<", a, ":", res2)

# (>) : sama seperti di matematika [lebih dari]
print("====(>)====")
a = 3
b = 7
res1 = a > b # False
res2 = b > a # True
print(a, ">", b, ":", res1)
print(b, ">", a, ":", res2)

# (<=) : sama seperti di matematika dan nilai minimal dibaca komputer [kurang dari sama dengan]
print("====(<=)====")
a = 3
b = 7
c = 3
res1 = a <= b # True
res2 = b <= a # False
res3 = a <= c # True
print(a, "<=", b, ":", res1)
print(b, "<=", a, ":", res2)
print(a, "<=", c, ":", res3)

# (>=) : sama seperti di matematika dan nilai minimal dibaca komputer [lebih dari sama dengan]
print("====(>=)====")
a = 3
b = 7
c = 3
res1 = a >= b # False
res2 = b >= a # True
res3 = a >= c # True
print(a, ">=", b, ":", res1)
print(b, ">=", a, ":", res2)
print(a, ">=", c, ":", res3)

# (==) : jika 2 variabel dibandingkan dengan value yang sama, maka akan menghasilkan True [sama dengan]
print("====(==)====")
a = 3
b = 7
c = 3
res1 = a == b # False
res2 = b == a # False
res3 = a == c # True
print(a, "==", b, ":", res1)
print(b, "==", a, ":", res2)
print(a, "==", c, ":", res3)

# (==) : jika 2 variabel dibandingkan dengan value yang tidak sama, maka akan menghasilkan True [tidak sama dengan]
print("====(!=)====")
a = 3
b = 7
c = 3
res1 = a != b # True
res2 = b != a # True
res3 = a != c # False
print(a, "!=", b, ":", res1)
print(b, "!=", a, ":", res2)
print(a, "!=", c, ":", res3)


# (is) : jika 2 variabel dibandingkan dengan value id yang sama, maka akan menghasilkan True [sama dengan].
# Dengan catatan bahwa yang dibandingkan adalah object/variabel bukan literal
print("====(is)====")
a = 3
b = 7
c = 3
res1 = a is b # False
res2 = b is a # False
res3 = a is c # True
print(a, "is", b, ":", res1)
print(b, "is", a, ":", res2)
print(a, "is", c, ":", res3)


# (is not) : jika 2 variabel dibandingkan dengan value id yang tidak sama, maka akan menghasilkan True [tidak sama dengan]. 
# Dengan catatan bahwa yang dibandingkan adalah object/variabel bukan literal
print("====(is not)====")
a = 3
b = 7
c = 3
res1 = a is not b # True
res2 = b is not a # True
res3 = a is not c # False
print(a, "is not", b, ":", res1)
print(b, "is not", a, ":", res2)
print(a, "is not", c, ":", res3)


print("Object Literal dan Object Variabel") 
var1 = 3
var2 = 9
var3 = 3
res1 = var2 is not 3 # True, Error (ada object literal) seharusnya. Tetapi di versi 3.10+ tetap bisa digabungkan
res2 = 3 != var2 # True
print(res1)
print(res2)

# cara cek id dan hex
# id
show1 = id(var1)
show2 = id(var2)
show3 = id(var3)
print(show1, "ini adalah id dari", var1)
print(show2, "ini adalah id dari", var2) 
print(show3, "ini adalah id dari", var3) 

# hex
show1 = hex(id(var1))
show2 = hex(id(var2))
show3 = hex(id(var3))
print(show1, "ini adalah hex dari", var1)
print(show2, "ini adalah hex dari", var2) 
print(show3, "ini adalah hex dari", var3) 

>>>>>>> cd1aaeb9d87aeb86de2fca0ed17417b15189fc16

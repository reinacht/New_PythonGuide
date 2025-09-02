<<<<<<< HEAD
# logika dalam python : or, and, not, xor

# logika or (or) : jika salah satu boolean bernilai True dari beberapa boolean 
# maka akan bernilai True
# [jika keduanya true akan true]
print("====OR====")
val1 = False
val2 = False
result = val1 or val2
print (val1, "OR", val2, ":", result)

val1 = False
val2 = True
result = val1 or val2
print (val1, "OR", val2, ":", result)

val1 = True
val2 = False
result = val1 or val2
print (val1, "OR", val2, ":", result)

val1 = True
val2 = True
result = val1 or val2
print (val1, "OR", val2, ":", result)


# logika and (and) : jika kedua boolean bernilai True dari beberapa boolean,
# maka akan bernilai True
print("====AND====")
val1 = False
val2 = False
result = val1 and val2
print (val1, "AND", val2, ":", result)

val1 = False
val2 = True
result = val1 and val2
print (val1, "AND", val2, ":", result)

val1 = True
val2 = False
result = val1 and val2
print (val1, "AND", val2, ":", result)

val1 = True
val2 = True
result = val1 or val2
print (val1, "AND", val2, ":", result)


# logika not (not) : jika nilai dari variabel tidak sama dengan nilai variabel yang dibandingkan, 
# maka akan menghasilkan True (False akan selalu menghasilkan True, begitu juga sebaliknya)
print("====NOT====") 
val1 = False
val2 = not val1
print (val1, "NOT : ", val2)

val1 = True
val2 = not val1
print (val1, "NOT : ", val2)


# logika or (or) : harus salah satu boolean bernilai True dari beberapa boolean 
# maka akan bernilai True
# [jika keduanya true akan false]
print("===XOR====")
val1 = False
val2 = False
result = val1 ^ val2
print (val1, "XOR", val2, ":", result)

val1 = False
val2 = True
result = val1 ^ val2
print (val1, "XOR", val2, ":", result)

val1 = True
val2 = False
result = val1 ^ val2
print (val1, "XOR", val2, ":", result)

val1 = True
val2 = True
result = val1 ^ val2
print (val1, "XOR", val2, ":", result)

>>>>>>> cd1aaeb9d87aeb86de2fca0ed17417b15189fc16

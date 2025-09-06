# Cara menduplikat list yang benar adalah menggunakan list.copy()
# Cara yang salah

x = [0, 0, 1, 10, 224, 4]
y = x

print(f"x : {x}")
print(f"y : {y}")

print(f"addres x :  {hex(id(x))}")
print(f"addres y :  {hex(id(y))}")


# Cara yang benar
z = x.copy()

print(f"x : {x}")
print(f"y : {y}")
print(f"z : {z}")

print(f"addres x :  {hex(id(x))}")
print(f"addres y :  {hex(id(y))}")
print(f"addres y :  {hex(id(z))}")

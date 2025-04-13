<<<<<<< HEAD
# List yang bersarang
# Nested - List harus menggunakan .deepcopy()
name = ['Ghua', 'Lubi', 'Yuji', 'Rwuga', 'Vierra']
age = [9, 11, 45, 23, 18]
nest_list = [name, age]

print(nest_list)

# .deepcopy() = meng-copy secara menyeluruh
from copy import deepcopy
dc_list = deepcopy(nest_list)

print(dc_list)
print(f"identity dc : {hex(id(dc_list))} ")
print(f"identity nest : {hex(id(nest_list))} ")

print(f"identity elemen 0 dc : {hex(id(dc_list[0]))} ")
=======
# List yang bersarang
# Nested - List harus menggunakan .deepcopy()
name = ['Ghua', 'Lubi', 'Yuji', 'Rwuga', 'Vierra']
age = [9, 11, 45, 23, 18]
nest_list = [name, age]

print(nest_list)

# .deepcopy() = meng-copy secara menyeluruh
from copy import deepcopy
dc_list = deepcopy(nest_list)

print(dc_list)
print(f"identity dc : {hex(id(dc_list))} ")
print(f"identity nest : {hex(id(nest_list))} ")

print(f"identity elemen 0 dc : {hex(id(dc_list[0]))} ")
>>>>>>> cd1aaeb9d87aeb86de2fca0ed17417b15189fc16
print(f"identity elemen 0 nest : {hex(id(nest_list[0]))} ")
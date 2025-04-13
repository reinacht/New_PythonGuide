<<<<<<< HEAD
# seperti looping pada umumnya, bisa di looping key, value, atau bahkan key dan value
# .items()  .keys() .values()
peoples_infos = {
    'name' : 'Nadhira',
    'age' : 17,
    'school' : 'MAN 1 Medan'
}

for key in peoples_infos: #key saja
    print(key)      

for key in peoples_infos.keys(): #key saja
    print(f"Kuncinya adalah : {key}")   

for value in peoples_infos.values(): #value saja
    print(f"Valuenya adalah : {value}")     

for key, value in peoples_infos.items(): #key dan value
    print(f"{key} : {value}")

for info in peoples_infos:  #value saja dengan index key
=======
# seperti looping pada umumnya, bisa di looping key, value, atau bahkan key dan value
# .items()  .keys() .values()
peoples_infos = {
    'name' : 'Nadhira',
    'age' : 17,
    'school' : 'MAN 1 Medan'
}

for key in peoples_infos: #key saja
    print(key)      

for key in peoples_infos.keys(): #key saja
    print(f"Kuncinya adalah : {key}")   

for value in peoples_infos.values(): #value saja
    print(f"Valuenya adalah : {value}")     

for key, value in peoples_infos.items(): #key dan value
    print(f"{key} : {value}")

for info in peoples_infos:  #value saja dengan index key
>>>>>>> cd1aaeb9d87aeb86de2fca0ed17417b15189fc16
    print(peoples_infos[info])
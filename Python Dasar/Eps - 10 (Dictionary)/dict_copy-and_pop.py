<<<<<<< HEAD
# ada 2 cara copy dict

# pertama dengan .copy()
dict1 = {
    'nama' : 'Grunge',
    'kulit' : 'Hitam',
    'umur' : '19'
}
print(f"Ini adalah origin : {dict1}")

new_dict = dict1.copy()
print(f"Ini adalah dict1.copy() : {new_dict}")

# kedua dengan fungsi dict(dict)
newest_dict = dict(dict1)
print(f"Ini adalah dict(dict1) : {newest_dict}")


# pop adalah menghapus satu key dan value dict
dictpop = dict1.pop('umur')
print(dict1)

dict1.pop('kulit')
print(dict1)

=======
# ada 2 cara copy dict

# pertama dengan .copy()
dict1 = {
    'nama' : 'Grunge',
    'kulit' : 'Hitam',
    'umur' : '19'
}
print(f"Ini adalah origin : {dict1}")

new_dict = dict1.copy()
print(f"Ini adalah dict1.copy() : {new_dict}")

# kedua dengan fungsi dict(dict)
newest_dict = dict(dict1)
print(f"Ini adalah dict(dict1) : {newest_dict}")


# pop adalah menghapus satu key dan value dict
dictpop = dict1.pop('umur')
print(dict1)

dict1.pop('kulit')
print(dict1)

>>>>>>> cd1aaeb9d87aeb86de2fca0ed17417b15189fc16

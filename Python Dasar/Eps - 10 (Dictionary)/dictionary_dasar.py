# dictionary adalah data collections yang populer di python
# dapat menyimpan banyak jenis data

# bentuk umum dictionary
dict_o = {
    'key' : 'value'
}

print(dict_o)


# dict berisi list
list_hewan = ['anjing', 'babi', 'biawak']
hewan = {
    'kat1' : list_hewan,
    'kat2' : 'kudanil, berang berang, hiu'
}

print(hewan)
print(f'Kategori 1 : {hewan['kat1']}')

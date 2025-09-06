# .len(data_name)         = mengukur panjang list
# .insert(i, data)        = menambahkan data sesuai posisi
# .append(data)           = menambah data di bagian akhir list
# .extend(list)           = menggabungkan 2 list
# .remove(data)           = menghapus data di list
# .pop()                  = menghapus data terakhir list
# data[]                  = memeriksa data di index tertentu

print('Sebelum dimanipulasi')
waifus = ['yuga', 'asuka', 'cinnamon', 'higana']
other_waifus = ['nizu', 'miya', 'fuba']
print(waifus)

length = len(waifus)
print(length)

print('Setelah dimanipulasi')
waifus.insert(0, 'rei')
print("\n",waifus)

waifus.append('Shiroko')
print("\n",waifus)

waifus.extend(other_waifus)
print("\n",waifus)

waifus.remove('cinnamon')
print("\n",waifus)

waifus.pop()
print("\n",waifus)

first = waifus[0]
print("\n",first)

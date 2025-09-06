# sets adalah salah satu data collections py yang valuenya otomatis diurutkan dan tidak ada index, 
# tetapi hanya bisa add and remove

sets_data = {9, 5, 2, 6, 0}
print(sets_data)

sets_data.add(17)
print(sets_data)

sets_data.remove(17)
print(sets_data)

# valuenya bisa semua, tapi ga boleh duplikat (akan dianggap 1)
mix_sets = {12, 'erin', 89, False, True, 'tyon', 'erin'}
print(mix_sets)

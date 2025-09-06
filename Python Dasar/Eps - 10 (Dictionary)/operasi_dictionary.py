# operasi sama seperti list, len(), KEY in dict

# CRUD
# Create
fruits = {
    'manis' : 'mangga, semangka',
    'asam' : 'jeruk, anggur',
    'pahit' : 'kesemak, sawo'
}
print(fruits)

print('\n')
# Read dengan .get()
print(fruits['pahit'])
print(fruits.get('asam'))
print(fruits.get('pedas', 'tidak ada key itu'))


print('\n')
# Update dengan .update()
fruits['pedas'] = 'cabai, paprika'
print(fruits)
fruits.update({'manis' : 'mangga, semangka, apel'})
print(fruits)
fruits.update({'pahit' : 'kesemak, sawo, jambu'})
print(fruits)


print('\n')
# Delete
del fruits['pedas']
print(fruits)


# panjang dan pengecekan
LEN_FRUITS = len(fruits)
print(LEN_FRUITS)

KEY = 'manis'
CHECK_KEY = KEY in fruits
print(f"Apakah {KEY} ada di fruits : {CHECK_KEY} ")

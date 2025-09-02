<<<<<<< HEAD
# for --> digunakan untuk looping range(), list dan str
# kondisi
# aksi

# range() = fungsi yg berisi angka 
print('\n',15*'=','Tes',15*'=')
for i in range(10):
    i += 1
    print(i)



numb = []
print('\n',15*'=','Tes',15*'=')
for i in range(50,100):
    i += 1
    numb.append(i)

print(numb)

count = sum(numb)
many_nums = len(numb)
print(f"Banyak Angka : {many_nums}")
print(f"Penambahan Angka : {count}")

# regular 
nums = [0,2,3,5,6,7,8,9,89,55,44]
print('\n',15*'=','Tes',15*'=')
for x in nums:
    print(x)


# while --> digunakan untuk looping variabel yang lebih bermacam dan lebih dinamis
# kondisi 
# aksi

print('\n',15*'=','Tes',15*'=')
x = 0
while x <= 70:
    x += 7
    if x == 49:
        print(f"Angka {x} adalah kuadrat dari 7!")
        continue
    print(x)

>>>>>>> cd1aaeb9d87aeb86de2fca0ed17417b15189fc16

<<<<<<< HEAD
## cek prima dari x ke y
# def var
min = 1
max = 1000
d_min = min

list_oddNum = [2]
list_totalP = []

# list all odd nums and 2
while min <= max:
  min += 1
  if min % 2 != 0:
    list_oddNum.append(min)

# looping for each odd nums
for eachNum in list_oddNum:
  dnum = 0
  list_all = []

  for x in range(1, eachNum + 1):
    list_all.append(x)

  for z in list_all:
    if eachNum % z == 0:
      dnum += 1

  if dnum <= 2:
    list_totalP.append(eachNum)

# print
print(f"Bilangnya : {list_totalP}")
many_nums = len(list_totalP)
print("\n",10*":","Bilangan Prima",10*":")
print(f"Banyaknya angka prima dari {d_min} ke {max} adalah : {many_nums}")



## cek prima
numP = int(input("\nCek : "))
list_allNum = []
divided_num = 0
list_dnum = []

for x in range(1, numP + 1):
  list_allNum.append(x)

for j in list_allNum:
  if numP % j == 0:
    list_dnum.append(j)
    divided_num += 1

if divided_num > 2:
  print(f"\nAda {len(list_dnum )} bilangan yg bisa dibagi, yaitu : {list_dnum}")
  print("Bukan Prima!!")

else:
  print("Prima!")
>>>>>>> cd1aaeb9d87aeb86de2fca0ed17417b15189fc16


# .count()      = menghitung banyak suatu karakter di dalam sebuah list
# .index()      = menampilkan value dengan index tertentu
# .sort()       = menyusun values of list secara berurutan dari depan / nilai terkecil (0,1,2,3... / a,b,c,d...)
# .reverse()    = menyusun values of list secara berurutan dari belakang / nilai terbesar (3,2,1,0... / d,c,b,a...)


# SORT AND REVERSE
group = [100, 3, 78, 99, -11, 1, 0, 'z', 'x', 't', 'a', 'b']
print(f"List biasa :{group}")

nums = [num for num in group if isinstance(num, (int, float))]
stri = [char for char in group if isinstance(char, str)]

nums.sort()
stri.sort()

group_sf = nums + stri
print(f"\nList sort :{group_sf}")

group_sf.reverse()
print(f"\nList reverse :{group_sf}")


# COUNT 
mixed_value = [2, 2, 2, 4, 4, 5, 6, 1, 3, 2, 9, 10, 'a', 'y', 'o', 'o', 'o', 'o']

count_int = mixed_value.count(2)
count_char = mixed_value.count('o')
count_a = mixed_value.count('a')

print(count_int)
print(count_char)
print(count_a)


# INDEX
waifus = ['Asuka', 'Rei', 'Kanao', 'Elaina', 'Yukino']
print(waifus)

waifus.sort()
print(waifus)

waifus.reverse()
index_1 = waifus.index('Rei')
print(index_1)

## .index(3, 1, 6) = val, start, end
numbers = [3, 5, 7, 77, 88, 3, 2, 1]

print(waifus.index('Rei'))
print(numbers.index(77)) # index dari element 77
print(numbers.index(3, 4)) # mencari index dari elemen/value 3 yang dimulai dari index ke-4 (yang pertama ketemu)
print(numbers.index(3, 0, 7)) # mencari index dari elemen 3 yang dimulai dari index ke-0 sampai ke-7 (yang pertama ketemu)

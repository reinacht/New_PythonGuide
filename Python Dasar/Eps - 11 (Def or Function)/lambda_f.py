# mirip seperti arrow function di js
# digunakan sebagai fungsi sementara dgn hanya 1 expression
# dan fungsi lambda akan otomatis me-return valuenya

'''LAMBDA FUNCTION'''
nama_variabel_fungsi = lambda argument1, argument2, argument3 : print(argument1, argument2, argument3) # di akhiri hanya dgn satu statement/expression fungsi

# calc akan menjadi function
calc = lambda a, b, c : print(f"Hasilnya adalah = {a*b*c}") # hanya boleh satu expression
print(calc(4,5,6))

def triple(n):
    return lambda a : a * n

myTriple = triple(3)
print(myTriple(11)) # argumen 11 akan menjadi a di dalam fungsi lambda


# sorted list
nums = [3, 4, 6, 7, 11, 100, 45, 77]
nums.sort()

print(nums)

# fungsi biasa
def kurang_10(n):
    return n < 10

hasil = list(filter(kurang_10, nums))
print(hasil)

# fungsi anynomous / lambda
hasil = list(filter(lambda x: x<10, nums))
print(hasil)

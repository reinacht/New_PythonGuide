<<<<<<< HEAD
# *args dan **kwargs
# adalah argumen yang berisi banyak data sekaligus, jika "*args" akan menghasilkan "tuple", maka **kwargs menghasilkan " dict"


# *args
def withArgs(*args): #namanya bebas, menghasilkan tuple dan argumennya dinamis (bisa banyak tanpa batas)
    name = args[0]
    age = args[1]
    gender = args[2]
    skin = args[3]
    
    return print(f"nama : {name},umur : {age}, kelamin : {gender} dan kulit {skin}")

withArgs("Guid", 99, "Non-Binary"," Dark")    
    
    
def countNum(*nums):
    output = 0
    for num in nums:
        output += num 
    return output
    
print(countNum(3,9,6,1,3,3,8,9))


# **kwargs
def withKwargs(**kwargs): #namanya bebas, menghasilkan dict dan argumennya harus dgn key (bisa banyak tanpa batas)
    for key, value in kwargs.items():
        hasil = print(f"{key}, yg berisi {value}")

    return hasil

print(withKwargs(name='ryu', number=89, genda='undefined'))


# argss dan kwargs bisa digabung 
def operations(*nums, **operasis):
    operasi = operasis['operasi']

    if operasi == '-':
        hasil = 0
        for num in nums:
            hasil -= num

    elif operasi == '+':
        hasil = 0
        for num in nums:   
            hasil += num

    elif operasi == '*':
        hasil = 1
        for num in nums:
            hasil *= num

    elif operasi == '/':
        hasil = 1
        for num in nums:
            hasil /= num
    
    return hasil  
        
result = print(operations(2,3,4,1,2,3,4,5,6,7,7, operasi='*'))

=======
# *args dan **kwargs
# adalah argumen yang berisi banyak data sekaligus, jika "*args" akan menghasilkan "tuple", maka **kwargs menghasilkan " dict"


# *args
def withArgs(*args): #namanya bebas, menghasilkan tuple dan argumennya dinamis (bisa banyak tanpa batas)
    name = args[0]
    age = args[1]
    gender = args[2]
    skin = args[3]
    
    return print(f"nama : {name},umur : {age}, kelamin : {gender} dan kulit {skin}")

withArgs("Guid", 99, "Non-Binary"," Dark")    
    
    
def countNum(*nums):
    output = 0
    for num in nums:
        output += num 
    return output
    
print(countNum(3,9,6,1,3,3,8,9))


# **kwargs
def withKwargs(**kwargs): #namanya bebas, menghasilkan dict dan argumennya harus dgn key (bisa banyak tanpa batas)
    for key, value in kwargs.items():
        hasil = print(f"{key}, yg berisi {value}")

    return hasil

print(withKwargs(name='ryu', number=89, genda='undefined'))


# argss dan kwargs bisa digabung 
def operations(*nums, **operasis):
    operasi = operasis['operasi']

    if operasi == '-':
        hasil = 0
        for num in nums:
            hasil -= num

    elif operasi == '+':
        hasil = 0
        for num in nums:   
            hasil += num

    elif operasi == '*':
        hasil = 1
        for num in nums:
            hasil *= num

    elif operasi == '/':
        hasil = 1
        for num in nums:
            hasil /= num
    
    return hasil  
        
result = print(operations(2,3,4,1,2,3,4,5,6,7,7, operasi='*'))

>>>>>>> cd1aaeb9d87aeb86de2fca0ed17417b15189fc16
    
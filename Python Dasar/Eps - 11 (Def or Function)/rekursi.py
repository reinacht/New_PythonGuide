<<<<<<< HEAD
def fib(x):
    if x < 2:
        return x
    return fib(x-1) + fib(x-2)

num = int(input("\nMasukkan urutannya : "))
fibonaci_ke = fib(num)
=======
def fib(x):
    if x < 2:
        return x
    return fib(x-1) + fib(x-2)

num = int(input("\nMasukkan urutannya : "))
fibonaci_ke = fib(num)
>>>>>>> cd1aaeb9d87aeb86de2fca0ed17417b15189fc16
print(f"Bilangan fibonacci ke-{num} adalah {fibonaci_ke}\n")
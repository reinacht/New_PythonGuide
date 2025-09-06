def fib(x):
    if x < 2:
        return x
    return fib(x-1) + fib(x-2)

num = int(input("\nMasukkan urutannya : "))
fibonaci_ke = fib(num)
print(f"Bilangan fibonacci ke-{num} adalah {fibonaci_ke}\n")

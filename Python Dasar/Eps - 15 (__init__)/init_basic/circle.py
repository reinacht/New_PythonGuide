def circle(equation):
    a = int(input("\nMasukkan Nilai a : "))
    b = int(input("Masukkan Nilai b : "))
    r = int(input("Masukkan Nilai r : "))
    print(f"\n{equation}")
    print("Jawaban : ")

    pers1 = f"x² - {2*a}x + {a**2} + y² - {2*b}y + {b**2} = {r**2}"
    pers2 = f"x² + y² - {2*a}x - {2*b}y + {a**2} + {b**2} = {r**2}"
    pers3 = f"x² + y² - {2*a}x - {2*b}y + {(a**2) + (b**2)} = {r**2}"
    pers4 = f"x² + y² - {2*a}x - {2*b}y = {r**2 - ((a**2) + (b**2))}"
    print(pers1)
    print(pers2)
    print(pers3)
    print(pers4)
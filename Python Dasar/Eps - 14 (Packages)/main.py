# packages adalah modules modules file .py
# cara importnya

## 1. import
import packages_basic.adv_calc # <-- regular expression import
import packages_basic.calcnums 
import packages_basic.fisika.formula

fisika1 = packages_basic.fisika.formula.resistant2(1.68e-8, 2, 10e-6)
print(fisika1)

## 2. as
import packages_basic.adv_calc as adv # <-- membuat alias atau nama lain dari nama variabel datanya
import packages_basic.calcnums as calc
import packages_basic.fisika.formula as formula


## 3. from
from packages_basic.calcnums import times # <-- langsung mengambil fungsinya/datanya dari file calcnums.py

num1 = calc.times(3, 90)
print(num1)

num2 = adv.floor_division(10, 6)
print(num2)

num3 = calc.plus(3, 90)
print(num3)

square5 = adv.square(5)
num4 = square5(10)
print(num4)

num5 = times(3, 90)
print(num5)

## 4. Fisika pack
hambatan1 = formula.resistant1(12, 0.5)
print(hambatan1)

hambatan2 = formula.resistant2(1.68e-8, 2, 10e-6)
print(hambatan2)

pressure = formula.pressure(75, 25)
print(pressure)

weight = formula.weight(62)
print(weight)

force = formula.force(250, 5)
print(force)
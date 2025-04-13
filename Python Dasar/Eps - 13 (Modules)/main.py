# modules adalah file yg berisi bnyk file or data dlm file .py
# cara importnya

## 1. import
import modules_basic.adv_calc # <-- regular expression import
import modules_basic.calcnums 

## 2. as
import modules_basic.adv_calc as adv # <-- membuat alias atau nama lain dari nama variabel datanya
import modules_basic.calcnums as calc

## 3. from
from modules_basic.calcnums import times # <-- langsung mengambil fungsinya/datanya dari file calcnums.py

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

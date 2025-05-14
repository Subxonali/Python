# 1.Given a side of square. Find its perimeter and area. 
# kvardratning tomoni
a=float(input('Kvadratning tomonini kiriting: '))
perimetr=4*a
Yuzasi=a**2
print(f"Perimetri: {perimetr}")
print(f"Yuzasi: {Yuzasi}")

#2.Given diameter of circle. Find its length
# Aylananing diametri
import math
b=float(input('Aylananing diametrini kiriting: '))
Aylana_uzunligi=b*(math.pi)
print(f"Aylana_uzunligi: {Aylana_uzunligi}")

#3.Given two numbers a and b. Find their mean.
a=float(input('Birinchi sonni kiriting: '))
b=float(input('Ikkinchi sonni kiriting: '))
Mean=(a+b)/2
print(F"Mean:{Mean}")

# Foydalanuvchidan ikki sonni kiritishni so‘raymiz
a = float(input("Birinchi sonni kiriting (a): "))
b = float(input("Ikkinchi sonni kiriting (b): "))

# Hisoblashlar
yigindi = a + b
kopaytma = a * b
a_kvadrat = a ** 2
b_kvadrat = b ** 2

# Natijalarni chiqaramiz
print(f"Yig'indisi: {yigindi}")
print(f"Ko‘paytmasi: {kopaytma}")
print(f"a ning kvadrati: {a_kvadrat}")
print(f"b ning kvadrati: {b_kvadrat}")

import math

--1
a = float(input("Kvadratning tomonini kiriting: "))
kvadrat_perimetr = 4 * a
kvadrat_yuza = a * a
print("Kvadratning perimetri:", kvadrat_perimetr)
print("Kvadratning yuzasi:", kvadrat_yuza)

--2
d = float(input("Doiraning diametrini kiriting: "))
doira_uzunligi = math.pi * d
print("Doiraning uzunligi:", doira_uzunligi)

--3

a = float(input("Birinchi sonni kiriting: "))
b = float(input("Ikkinchi sonni kiriting: "))
ortalacha = (a + b) / 2
print("O‘rtacha qiymat:", ortalacha)



--4
yigindi = a + b
kopaytma = a * b
a_kvadrat = a ** 2
b_kvadrat = b ** 2
print("Yig‘indi:", yigindi)
print("Ko‘paytma:", kopaytma)
print("a ning kvadrati:", a_kvadrat)
print("b ning kvadrati:", b_kvadrat)

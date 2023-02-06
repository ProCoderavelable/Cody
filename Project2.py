#This program calculates the area of a scalene triangle
import math

a = float(input("First side: "))
b = float(input("Second side: "))
c = float(input("Third side: "))

perimeter = a + b + c
calculation = perimeter/ 2 * (perimeter / 2 - a) * (perimeter / 2 - b) * (perimeter / 2 - c)
if calculation > 0:
    area = math.sqrt(calculation)
    print("This area of the triangle is ", round(area, 2))
else:
    print("This sides that you gave don't create a triangle")
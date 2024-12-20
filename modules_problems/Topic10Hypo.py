import math


def calculate_hypotenuse(base, height):
   
    hypotenuse = math.sqrt(base**2 + height**2)
    return hypotenuse


base = float(input("Enter the length of the base: "))
height = float(input("Enter the length of the height: "))

hypotenuse = calculate_hypotenuse(base, height)
print(f"The length of the hypotenuse is: {hypotenuse}")

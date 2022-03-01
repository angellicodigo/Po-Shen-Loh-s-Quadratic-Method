import math
import cmath
from fractions import Fraction
#start
print(
    "This is a calculator for Po-Shen Loh's approach on\nsolving quadratic equations, without using the quadratic formula.\n\nGiven: (ax^2 + bx^2 + c)\nSolve: (-B/2 + z)(-B/2 - z) = C as B = b/a and C = c/a"
)


def solve():
    exit = ""
    #loops till user says no
    while 'n' not in exit.lower():
        #inputs
        a = float(input("\nEnter the number for a: "))
        b = float(input("Enter the number for b: "))
        c = float(input("Enter the number for c: "))
        #showcase the equation
        print(f"\nSolving for: ({a})x^2+({b})x+({c})")
        #actual math stuff
        B = (-1 * (b/a)) / 2
        C = c / a
        z = -1 * (C - B**2)
        try:
            z = math.sqrt(z)
            #in case there are fractions
            B = Fraction(B).limit_denominator(100)
            C = Fraction(C).limit_denominator(100)
            z = Fraction(z).limit_denominator(100)
            #steps
            if a != 1:
                print(f"(-({b})/{a})/2 + z)(-({b})/{a})/2 - z) = {c}/{a}")
            print(
                f"({B} + z)({B} - z) = {C}\n({B})^2 - (z)^2 = {C}\n{B**2} - z^2 = {C}\n-z^2 = {C} - {B**2}")
            #in case it is square rooting a fraction
            if z != 0 and z != int(z):
              numerator = abs((C - B**2).numerator)
              denominator = math.sqrt(abs((C - B**2).denominator))
              print(f"√(z)^2 = √({numerator}/{(C - B**2).denominator})\nz = √{numerator}/{denominator}\nx = {B} + √{numerator}/{denominator}, x = {B} - √{numerator}/{denominator}")
            else:
              print(f"√(z)^2 = √({z})\nz = {z}\nx = ({B} + ({z})), x = ({B} - ({z}))\nx = {B + z}, x = {B - z}")
        #imagery numbers
        except:
            z = cmath.sqrt(Fraction(z).limit_denominator(100))
            B = Fraction(B).limit_denominator(100)
            C = Fraction(C).limit_denominator(100)
            #steps for imagery roots
            if a > 1:
                print(f"(-({b})/{a})/2 + z)(-({b})/{a})/2 - z) = {c}/{a}")
            print(
                f"({B} + z)({B} - z) = {C}\n({B})^2 - (z)^2 = {C}\n{B**2} - z^2 = {C}\n-z^2 = {C} - {B**2}\n√(z)^2 = √({-1*(C-B**2)})"
            )
            if (C - B**2) != 0 and (C - B**2) != int((C - B**2)):
              numerator = (C - B**2).numerator
              denominator = math.sqrt((C - B**2).denominator)
              print(f"z = √{numerator}/{denominator}j\nx = {B} + √{numerator}/{denominator}j, x = {B} - √{numerator}/{denominator}j")
            else:
              print(f"z = {z}\nx = {B} + {z}, x = {B} - {z}")
        exit = input("\nAgain? ")


solve()
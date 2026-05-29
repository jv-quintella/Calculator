import math
from fractions import Fraction

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def prod(a, b):
    return a * b

def div(a, b):
    if b != 0:
        return a/b
    else: 
        return "Math error"

def sqrt(a):
    if a >= 0:
        return math.sqrt(a)
    else:
        return "Math error"

def square(a):
    return a * a

def percent(a, b):
    if b is not None:
        return (a * b) / 100
    else:
        return a / 100

def fraction(a, b):
    try:
        if b is not None:

            result = Fraction(a, b)
        else:
            result = Fraction(a)
            
        return str(result.limit_denominator())
        
    except ValueError:
        return "Syntax error"

def Menu():
    pass

def main():
    pass
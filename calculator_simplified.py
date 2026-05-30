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
        return a / b
    else: 
        return "Math Error"

def sqrt(a):
    if a >= 0:
        return math.sqrt(a)
    else:
        return "Math Error"

def square(a):
    return a * a

def percent(a, base=None):
    if base is not None:
        return (a * base) / 100
    else:
        return a / 100

def fraction(a, b=None):
    try:
        if b is not None:
            result = Fraction(a, b)
        else:
            result = Fraction(a)
            
        return str(result.limit_denominator())
        
    except ValueError:
        return "Error"

def main():
    while True:
        print() 
        op = input("Operator (+, -, *, /, sqrt, sq, %, frac) or 'q' to quit: ")
        
        if op == 'q':
            break
            
        if op not in ['+', '-', '*', '/', 'sqrt', 'sq', '%', 'frac']:
            print("Invalid operator.")
            continue

        try:
            if op in ['sqrt', 'sq', 'frac']:
                a = float(input("Number: "))
                
                if op == 'sqrt':
                    print(sqrt(a))
                elif op == 'sq':
                    print(square(a))
                elif op == 'frac':
                    print(fraction(a))
                    
            else:
                a = float(input("First number: "))
                
                if op == '%':
                    has_base = input("Relative to a base? (y/n): ")
                    if has_base.lower() == 'y':
                        b = float(input("Base number: "))
                        print(percent(a, b))
                    else:
                        print(percent(a))
                    continue

                b = float(input("Second number: "))
                
                if op == '+':
                    print(add(a, b))
                elif op == '-':
                    print(sub(a, b))
                elif op == '*':
                    print(prod(a, b))
                elif op == '/':
                    print(div(a, b))
                    
        except ValueError:
            print("Error: Invalid number format.")

if __name__ == "__main__":
    main()
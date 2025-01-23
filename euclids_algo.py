# type 1
def gcd_recursive(a, b):
    if b == 0:
        return a
    return gcd_recursive(b, a%b)

a,b = 56,98
print(f"GCD of {a} and {b} is {gcd_recursive(a,b)}")


# type 2
def gcd_iterative(a, b):
    while b:
        a,b = b, a%b
    return a

print(f"gcd of {a} and {b} is {gcd_iterative(a,b)}")
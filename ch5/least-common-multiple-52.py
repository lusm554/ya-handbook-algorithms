"""
Для двух чисел a и b найдите их наименьшее общее кратное.
"""
a, b = map(int, input().split())
def gcd(a, b):
    "greater common divisor"
    if a <= 0 or b <= 0:
        return max(a, b)
    else:
        return gcd(b, a%b)
def lcm(a, b):
    "least common multiple"
    return (a*b)//gcd(a, b)
print(lcm(a, b))

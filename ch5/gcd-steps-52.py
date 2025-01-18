def find_fibonacci_pair(n):
    fib1, fib2 = 1, 1
    while fib1 + fib2 <= n:
        fib1, fib2 = fib2, fib1 + fib2
    return fib2, fib1

def gcd_steps(a, b):
    steps = 0
    while b != 0:
        a, b = b, a % b
        steps += 1
    return steps

def find_max_gcd_steps_combined(n):
    fib_a, fib_b = find_fibonacci_pair(n)
    max_steps = gcd_steps(fib_a, fib_b)
    best_a, best_b = fib_a, fib_b
    for a in range(n, max(n - 1000, 1), -1):
        b = a // 2
        for delta in range(-2, 3):
            b_candidate = b + delta
            if b_candidate > 0 and b_candidate < a:
                steps = gcd_steps(a, b_candidate)
                if steps > max_steps:
                    max_steps = steps
                    best_a, best_b = a, b_candidate
    return best_a, best_b

n = int(input())
a, b = find_max_gcd_steps_combined(n)
print(b, a)

import math

def gcd(a, b):
    while a * b != 0:
        if a > b:
            a %= b
        else:
            b %= a
    return a + b

def digit_sum(a):
    total = 0
    while a > 0:
        total += a % 10
        a //= 10
    return total

def is_prime(a):
    if a < 2:
        return False
    for i in range(2, int(math.sqrt(a)) + 1):
        if a % i == 0:
            return False
    return True

def main():
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        if is_prime(digit_sum(gcd(n, m))):
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    main()

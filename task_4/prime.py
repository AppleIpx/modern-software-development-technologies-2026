# Дополнительно: простота числа перебором делителей, пока divisor * divisor <= n.
n = int(input("n (>= 2): "))

is_prime = True
divisor = 2
while divisor * divisor <= n:
    if n % divisor == 0:
        is_prime = False
        break
    divisor += 1

if is_prime:
    print("простое")
else:
    print("составное")

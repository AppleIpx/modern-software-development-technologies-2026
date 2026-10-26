a = int(input("a: "))
b = int(input("b: "))

if a < b:
    for number in range(a, b + 1):
        print(number)
elif a > b:
    for number in range(a, b - 1, -1):
        print(number)
else:
    print(a)

def F(n):
    if n < 3:
        return n + 3
    elif n >= 3 and n % 3 == 0:
        return (n + 2) * F(n - 4)
    else:
        return n + F(n - 1) + 2 * F(n - 2)

result = F(20)
print("Значение функции F(20):", result)

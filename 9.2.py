def find_numbers_with_4_divisors(start, end):
    for num in range(start, end + 1):
        divisors = []
        for i in range(1, int(num ** 0.5) + 1):
            if num % i == 0:
                divisors.append(i)
                if i != num // i:
                    divisors.append(num // i)
        if len(divisors) == 4:
            print("Число", num, "имеет 4 делителя:", sorted(divisors))

find_numbers_with_4_divisors(338472, 338494)

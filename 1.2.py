def count_even_multiples_of_9():
    count = 0
    while True:
        num = int(input())
        if num == 0:
            break
        if num % 2 == 0 and num % 9 == 0:
            count += 1
    return count

print(count_even_multiples_of_9())

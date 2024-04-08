def count_numbers_ending_with_6():
    count = 0
    n = int(input())
    for _ in range(n):
        num = int(input())
        if num % 10 == 6:
            count += 1
    return count

print(count_numbers_ending_with_6())

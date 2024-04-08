def find_min_number_ending_with_4():
    min_num = float('inf')
    n = int(input())
    for _ in range(n):
        num = int(input())
        if num % 10 == 4 and num < min_num:
            min_num = num
    return min_num

print(find_min_number_ending_with_4())

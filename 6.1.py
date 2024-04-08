def count_max_occurrences(arr):
    max_element = max(arr)  # Находим максимальный элемент в массиве
    count = arr.count(max_element)  # Считаем количество элементов, равных максимальному
    return count

def main():
    arr = [int(input()) for _ in range(30)]
    print(count_max_occurrences(arr))

if __name__ == "__main__":
    main()

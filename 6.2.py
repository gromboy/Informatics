def count_min_occurrences(arr):
    min_element = min(arr)  # Находим минимальный элемент в массиве
    count = arr.count(min_element)  # Считаем количество элементов, равных минимальному
    return count

def main():
    arr = [int(input()) for _ in range(30)]
    print(count_min_occurrences(arr))

if __name__ == "__main__":
    main()

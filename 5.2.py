def count_min_elements(arr):
    min_element = min(arr)  # Находим минимальный элемент в массиве
    count = arr.count(min_element)  # Считаем количество элементов, равных минимальному
    return count

def main():
    n = int(input("Введите количество элементов в массиве: "))
    arr = []
    for i in range(n):
        arr.append(int(input("Введите элемент {}: ".format(i + 1))))
    
    print("Число элементов, равных минимальному:", count_min_elements(arr))

if __name__ == "__main__":
    main()

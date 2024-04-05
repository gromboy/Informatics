def count_max_elements(arr):
    max_element = max(arr)  # Находим максимальный элемент в массиве
    count = arr.count(max_element)  # Считаем количество элементов, равных максимальному
    return count

def main():
    n = int(input("Введите количество элементов в массиве: "))
    arr = []
    for i in range(n):
        arr.append(int(input("Введите элемент {}: ".format(i + 1))))
    
    print("Число элементов, равных максимальному:", count_max_elements(arr))

if __name__ == "__main__":
    main()

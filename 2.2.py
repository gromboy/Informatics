def solve_task2():
    num1 = int(input())
    num2 = int(input())
    
    product = num1 * num2
    
    if product < 0:
        result = product * (-5)
    else:
        result = product * 2
    
    return result

print(solve_task2())

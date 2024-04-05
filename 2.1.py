def solve_task1():
    num1 = int(input())
    num2 = int(input())
    
    if (num1 + num2) % 2 == 0:
        result = num1 * num2
    else:
        result = num1 / num2
    
    return result

print(solve_task1())

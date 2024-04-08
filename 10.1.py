def check_same_quarter(x1, y1, x2, y2):
    if (x1 > 0 and x2 > 0) or (x1 < 0 and x2 < 0):
        if (y1 > 0 and y2 > 0) or (y1 < 0 and y2 < 0):
            return "YES"
    return "NO"

x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
print(check_same_quarter(x1, y1, x2, y2))

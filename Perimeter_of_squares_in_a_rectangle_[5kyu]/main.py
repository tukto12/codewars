def perimeter(n):
    a = 0
    b = 1

    sum = 1
    for i in range(n):
        a, b = b, a + b
        sum += b

    return 4 * sum


print(perimeter(5))
print(perimeter(7))

def sum_of_squares(n):
    return sum(i ** 2 for i in range(1, n + 1))

n = 6
print(f"Sum = {sum_of_squares(n)}")

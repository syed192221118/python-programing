def sum_of_multiples(n):
    return sum(i for i in range(n) if i % 3 == 0 or i % 5 == 0)

n = 200
result = sum_of_multiples(n)
print(f"The sum of all multiples of 3 and 5 below {n} is {result}")

def squares_in_range(lower, upper):
    return [(i, i ** 2) for i in range(lower, upper + 1)]

lower = int(input("Enter lower range: "))
upper = int(input("Enter upper range: "))
print(squares_in_range(lower, upper))

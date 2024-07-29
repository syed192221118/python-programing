def perfect_squares_in_range(lower, upper):
    perfect_squares = []
    for i in range(lower, upper + 1):
        if i ** 0.5 == int(i ** 0.5) and sum(int(digit) for digit in str(i)) < 10:
            perfect_squares.append(i)
    return perfect_squares

lower = int(input("Enter lower range: "))
upper = int(input("Enter upper range: "))
print(perfect_squares_in_range(lower, upper))

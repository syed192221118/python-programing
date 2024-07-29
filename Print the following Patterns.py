def print_pattern(n):
    for i in range(1, n + 1):
        print(' '.join(str(j) for j in range(1, i + 1)))

print_pattern(5)

def print_pattern2(n):
    for i in range(1, n + 1):
        print(' '.join(str(i) * i))

print_pattern2(5)

def print_pattern3(n):
    for i in range(1, n + 1):
        print(' '.join(str(i * 10) for i in range(1, i + 1)))

print_pattern3(5)

def print_pattern4(n):
    for i in range(1, n + 1):
        print(' '.join(str(i * 0.1) for i in range(1, i + 1)))

print_pattern4(5)

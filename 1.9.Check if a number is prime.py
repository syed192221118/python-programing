def check_prime(num):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True
    else:
        return False

num = 7
print(check_prime(num))  # Output: True

def check_armstrong(num):
    sum = 0
    for i in str(num):
        sum += int(i) ** len(str(num))
    if sum == num:
        return True
    else:
        return False

num = 371
print(check_armstrong(num))  # Output: True

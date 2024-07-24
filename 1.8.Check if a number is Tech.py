def check_tech(num):
    sum = 0
    for i in str(num):
        sum += int(i)
    if sum == 10:
        return True
    else:
        return False

num = 19
print(check_tech(num))  # Output: True

def remove_k_digits(num, k):
    num = list(num)
    while k > 0:
        for i in range(len(num) - 1):
            if num[i] > num[i + 1]:
                num.pop(i)
                k -= 1
                break
        else:
            num.pop()
            k -= 1
    return "".join(num)

num = "1432219"
k = 3
print(remove_k_digits(num, k))

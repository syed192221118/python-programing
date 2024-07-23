def max_binary(a, b, c):
    max_val = max(int(a, 2), int(b, 2), int(c, 2))
    return bin(max_val)[2:]

a = "1101"
b = "1011"
c = "1001"
print(f"Maximum Number: {max_binary(a, b, c)}")

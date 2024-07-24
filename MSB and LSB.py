def msbAndLsb(n):
    msb = n.bit_length() - 1
    lsb = n & 1
    return msb, lsb

n = 1267899
print(msbAndLsb(n))  # Output: (19, 1)

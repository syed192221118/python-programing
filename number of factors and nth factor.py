def factors(n):
    factors = []
    for i in range(1, n + 1):
        if n % i == 0:
            factors.append(i)
    return factors

n = 100
nth = 4
factors_list = factors(n)
print(f"Number of factors = {len(factors_list)}")
print(f"{nth}th factor of {n} = {factors_list[nth - 1]}")

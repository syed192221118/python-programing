def count_matches(s1, s2):
    return sum(1 for c1, c2 in zip(s1, s2) if c1 == c2)

s1 = "what"
s2 = "watch"
print(count_matches(s1, s2))  # Output: 1

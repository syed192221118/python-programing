def is_isomorphic(s, t):
    if len(s) != len(t):
        return False

    s_to_t = {}
    t_to_s = {}

    for c_s, c_t in zip(s, t):
        if c_s not in s_to_t and c_t not in t_to_s:
            s_to_t[c_s] = c_t
            t_to_s[c_t] = c_s
        elif s_to_t.get(c_s) != c_t or t_to_s.get(c_t) != c_s:
            return False

    return True

s = "egg"
t = "add"
print(is_isomorphic(s, t))  # Output: True

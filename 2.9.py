def remove_common_words(S1, S2):
    words_S1 = set(S1.split())
    words_S2 = set(S2.split())

    common_words = words_S1 & words_S2

    result_S1 = ' '.join(word for word in S1.split() if word not in common_words)
    result_S2 = ' '.join(word for word in S2.split() if word not in common_words)

    return result_S1, result_S2

S1 = "sky is blue in color"
S2 = "Raj likes sky blue color"

result_S1, result_S2 = remove_common_words(S1, S2)

print(result_S1)  # Output: is in
print(result_S2)  # Output: Raj likes

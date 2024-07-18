word = input("Enter the word: ")

# Convert the word to a list of characters
chars = list(word)

# Sort the characters in alphabetical order (normal)
chars.sort()
normal_order = ' '.join(chars)
print(f"Alphabetical Order Normal: {normal_order}")

# Sort the characters in alphabetical order (reverse)
chars.sort(reverse=True)
reverse_order = ' '.join(chars)
print(f"Alphabetical Order Reverse: {reverse_order}")

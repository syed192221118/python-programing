def count_vowels_and_consonants(statement):
    vowels = 'aeiou'
    statement = statement.lower()
    vowel_count = 0
    consonant_count = 0
    for char in statement:
        if char.isalpha():
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1
    print(f"Number of vowels = {vowel_count}")
    print(f"Number of Consonants = {consonant_count}")
    if vowel_count > consonant_count:
        print("Vowels are maximum")
    elif consonant_count > vowel_count:
        print("Consonants are maximum")
    else:
        print("Both are equal")

statement = input("Enter a statement: ")
count_vowels_and_consonants(statement)

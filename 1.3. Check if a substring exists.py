def check_substring(main_str, sub_str):
    if sub_str in main_str:
        return True
    else:
        return False

main_str = "Hello World"
sub_str = "World"
print(check_substring(main_str, sub_str))  # Output: True

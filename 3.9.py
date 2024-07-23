def convert_case(s):
    return s.upper(), s.lower()

s = "PYTHON IS VERY SIMPLE"
uppercase, lowercase = convert_case(s)
print("Uppercase String:", uppercase)
print("Lowercase String:", lowercase)

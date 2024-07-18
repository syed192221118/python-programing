num = input("Enter the number: ")
mirror = num[::-1]
if num == mirror:
    print("The number is a mirror number.")
else:
    print("Mirror image:", mirror)

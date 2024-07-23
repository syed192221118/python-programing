def calculate_ticket_price(age):
    if age <= 3:
        return "Free"
    elif age <= 12:
        return "Rs 10"
    else:
        return "Rs 20"

age = int(input("Enter your age: "))
print("Your ticket price is:", calculate_ticket_price(age))

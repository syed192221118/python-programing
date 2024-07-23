def km_to_miles(km):
    return km * 0.621371

km = float(input("Enter kilometers: "))
print(f"{km} kilometers is equal to {km_to_miles(km)} miles")

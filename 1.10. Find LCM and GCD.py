import math

def find_lcm_gcd(num1, num2):
    lcm = (num1 * num2) // math.gcd(num1, num2)
    gcd = math.gcd(num1, num2)
    return lcm, gcd

num1 = 12
num2 = 15
lcm, gcd = find_lcm_gcd(num1, num2)
print("LCM:", lcm)  # Output: 60
print("GCD:", gcd)  # Output: 3

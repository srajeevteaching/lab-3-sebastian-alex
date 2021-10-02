# Programmers: Jonathan, Alex, Sebastian
# Course: CS151, Dr. Rajeev
# Date: September 30th, 2021
# Lab Number: 3
# Program Inputs: Weight of package, Distance it needs to be shipped
# Program Outputs: Output total charge for shipping package
import math

# Ask user input
weight = float(input("Enter the weight of package in kg: "))
distance = float(input("Enter the distance the package needs to be shipped in miles: "))

# Determine rate for shipping package based on weight and Validate Input
if weight <= 2 and weight > 0:
    rate = 1.10 / 500
    is_valid = True
elif weight > 2 and weight <= 6:
    rate = 2.20 / 500
    is_valid = True
elif weight > 6 and weight <= 10:
    rate = 3.70 / 500
    is_valid = True
elif weight > 10 and weight <= 20:
    rate = 4.8 / 500
    is_valid = True
elif weight > 20:
    print("\nWeight Exceeds shipping limit! (Please enter between 0kg - 20kg)")
    is_valid = False
elif weight <= 0:
    print("\nWeight does not meet shipping requirements! (Please enter between 1kg - 20kg)")
    is_valid = False

# Determine if distance is valid and total shipping calculation
if is_valid == True:
    if distance >= 10 and distance <= 3000:
        # Total Shipping Calculation
        shipping_total = rate * distance
        math.ceil(shipping_total)
        print("\nYour total for shipping this package is: $" + str(shipping_total) + " Dollars ")
    else:
        print("\nYour package cannot be shipped! Does not meet distance requirements.")
else:
    print("\nYour package cannot be shipped!")

print("Thanks for using our code!")
"""
Project Name: Lab2
Author: Micah M Tinife
Description: This week, you have studied additional Python language syntax including functions The Lab for this week demonstrates your knowledge of this additional Python functionality. 
Date: 1/25/2022
"""

import datetime
import math
import random
import string
import sys

def generate_secure_password():
    """Generates secure password based on the users input"""
    length = int(input("Enter Password length: "))
    upper = input("Use Uppercase? y/n: ")
    lower = input("Use Lowercase? y/n: ")
    nums = input("Use Numbers? y/n: ")
    sp_characters = input("Use Special Characters? y/n: ")

    uppercase_letters = string.ascii_uppercase
    lowercase_letters = string.ascii_lowercase
    numbers = string.digits
    special_chars = string.punctuation
    all_characters = string.ascii_uppercase + \
        string.ascii_lowercase + string.digits + string.punctuation
    user_input = (upper + lower
                  + nums + sp_characters)

    def all_password_type(password_type):
        """Generates secure password if user wants full complexity"""
        password = "".join(random.sample(password_type, length))
        print("Generated Password: " + password)

    def one_password_type(password_type1):
        """Generates secure password if user wants 1 level of complexity"""
        password = "".join(random.sample(password_type1, length))
        print("Generated Password: " + password)

    def two_password_type(password_type1, password_type2):
        """Generates secure password if user wants 2 level of complexity"""
        password_group_2 = password_type1 + password_type2
        password = "".join(random.sample(password_group_2, length))
        print("Generated Password: " + password)

    def three_password_type(password_type1, password_type2, password_type3):
        """Generates secure password if user wants 3 level of complexity"""
        password_group_3 = password_type1 + password_type2 + password_type3
        password = "".join(random.sample(password_group_3, length))
        print("Generated Password: " + password)

    if user_input == "yyyy":
        all_password_type(all_characters)
    elif user_input == "ynnn":
        one_password_type(uppercase_letters)
    elif user_input == "nynn":
        one_password_type(lowercase_letters)
    elif user_input == "nnyn":
        one_password_type(numbers)
    elif user_input == "nnny":
        one_password_type(special_chars)
    elif user_input == "yynn":
        two_password_type(uppercase_letters, lowercase_letters)
    elif user_input == "ynyn":
        two_password_type(uppercase_letters, numbers)
    elif user_input == "ynny":
        two_password_type(uppercase_letters, special_chars)
    elif user_input == "nyyn":
        two_password_type(lowercase_letters, numbers)
    elif user_input == "nyny":
        two_password_type(lowercase_letters, special_chars)
    elif user_input == "nnyy":
        two_password_type(numbers, special_chars)
    elif user_input == "yyyn":
        three_password_type(uppercase_letters, lowercase_letters, numbers)
    elif user_input == "nyyy":
        three_password_type(lowercase_letters, numbers, special_chars)
    elif user_input == "yyny":
        three_password_type(uppercase_letters,
                            lowercase_letters, special_chars)
    elif user_input == "ynyy":
        three_password_type(uppercase_letters, numbers, special_chars)


def to_percentage():
    """Calculate and Format a Percentage given 2 integer and a decimal place inputs """
    first_decimal_input = int(input("First Decimal Number: "))
    second_decimal_input = int(input("Second Decimal Number: "))
    decimal_places = int(input("Decimal places: "))
    final_decimal = (first_decimal_input / second_decimal_input) * 100
    deciaml_place_converter = '{:.{prec}f}'.format(
        final_decimal, prec=decimal_places)
    print("The Percentage between " + str(first_decimal_input)
          + " and " + str(second_decimal_input) +
          " within " + str(decimal_places)
            + " decimal place " + "is: " + str(deciaml_place_converter))

def days_to_go():
    """Calculate the number of days to go from July 4, 2025"""
    current_date = datetime.date.today()
    future_date = datetime.date(2025, 6, 4)
    current_to_future_date = future_date - current_date
    print("We are " + '{:,}'.format(current_to_future_date.days) +
          " days away from July 4, 2025.")

def law_of_cosines_calculation():
    """Uses the Law of Cosines to calculate the leg of a triangle"""
    side_a = float(input("Enter Side a's value: "))
    side_b = float(input("Enter Side b's value: "))
    angle = float(input("Enter Angle: "))
    angle_rad = math.radians(angle)
    cosins_answer = math.sqrt(
        (side_a**2) + (side_b**2) - (2*side_a*side_b*(math.cos(angle_rad))))
    print("The leg of the Triangle is: " + str(cosins_answer))

def circular_cylinder_volume_calculation():
    """Calculate the volume of a Right Circular Cylinder"""
    radius = float(input("Enter Radius: "))
    height = float(input("Enter Height: "))
    circular_cylinder_volume = (math.pi * radius**2) * height
    print("Volume: " + str(circular_cylinder_volume))

def main():
    """Front-end Layer of the program, asks the user for what actions they wish to take"""
    def message():
        """Displays the messages"""
        print("What operation would you like to do?")
        print("""a. Generate Secure Password \nb. Calculate and Format a Percentage \nc. How many days from today until July 4, 2025? \nd. Use the Law of Cosines to calculate the leg of a triangle. \ne. Calculate the volume of a Right Circular Cylinder \nf. Exit program""")
    while True:
        message()
        user_input = input()
        can_containue = "y"
        if can_containue == "y":
            if user_input == "a":
                generate_secure_password()
                can_containue = input("Do you want to continue? y/n: ")
            elif user_input == "b":
                to_percentage()
                can_containue = input("Do you want to continue? y/n: ")
            elif user_input == "c":
                days_to_go()
                can_containue = input("Do you want to continue? y/n: ")
            elif user_input == "d":
                law_of_cosines_calculation()
                can_containue = input("Do you want to continue? y/n: ")
            elif user_input == "e":
                circular_cylinder_volume_calculation()
                can_containue = input("Do you want to continue? y/n: ")
            elif user_input == "f":
                print("Thank you for using my application! \nGoodbye!")
                sys.exit()
            elif user_input not in ["a", "b", "c", "d", "e", "f"]:
                print("Invalid input, please try again.")
                can_containue = input("Do you want to continue? y/n: ")
        elif can_containue == "n":
            print("Thank you for using my application! \nGoodbye!")
            sys.exit()

if __name__ == "__main__":
    main()

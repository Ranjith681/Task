import re
number = input("Enter your Phone number:")
pattern =re.compile("^(\+\d{1,2}\s)?\(?\d{3}\)?[\s.-]\d{3}[\s.-]\d{4}$")
if pattern.match(number):
    print(f"{number} is valid moblie number.")
else:
    print(f"{number} is not valid moblie number.")
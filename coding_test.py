# 55. Write a Python program to check if a string is a valid hexadecimal number.

# Get input from the user
str = input("Enter a string: ").strip()  # Remove extra spaces

# Remove '0x' or '0X' so that it start from index 2 
if str.startswith("0x") or str.startswith("0X"):
    str = str[2:]

# Initialize validity as True
is_valid = True

# Checking the string is not empty
if len(str) > 0:
    # Loop through each character in the string
    for char in str:
        # If character is not a valid hexadecimal character, set is_valid to False
        if char not in "0123456789abcdefABCDEF":
            is_valid = False
            break
else:
    # If the string is empty, it's not a valid hexadecimal number
    is_valid = False

# Print the result
if is_valid:
    print("It's a valid hexadecimal number.")
else:
    print("It's NOT a valid hexadecimal number.")



# Input: 0x1A3F
# Output: It's a valid hexadecimal numbe

# Input: XYZ123
# Output: It's NOT a valid hexadecimal number.


# Input: 1234
# Output: It's a valid hexadecimal number.
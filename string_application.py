# feature/hw/ex_2
# HW-2: Fedor_xp28@student.itstep.org

try:
    string = input("Enter a string: ")
    letters = 0
    digits = 0

    for char in string:
        if char.isalpha():
            letters += 1
        elif char.isdigit():
            digits += 1

    print("Number of letters:", letters)
    print("Number of digits:", digits)

except Exception as e :
    print("Error: ", e)
finally:
    print("Program terminated")
    exit()

# Path: string_application.py




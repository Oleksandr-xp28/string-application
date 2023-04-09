# feature/hw/ex_3
# HW-2: Fedor_xp28@student.itstep.org
try:
    string = input("Enter a string: ")
    char = input("Enter a character to search for: ")
    count = 0

    for c in string:
        if c == char:
            count += 1

    print(f"Character '{char}' Appears {count}.")
except Exception as e :
    print("Error: ", e)
finally:
#    print("Program terminated")
    exit()

# Path: string_application.py

# feature/hw/ex_1
# HW-1: Write a program that asks the user for a string and prints out whether this string is a palindrome or not. (A palindrome is a string that reads the same forwards and backwards.)
try:
    text = input("Enter a string: ")
    result = ""
    for i in range(len(text) -1,-1,-1):
        result += text[i]
    print(result)
except Exception as e :
    print("Error: ", e)
finally:
#    print("Program terminated")
    exit()

# Path: string_application.py

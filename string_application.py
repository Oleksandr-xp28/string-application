# feature/hw/ex_1
# HW-2: Fedor_xp28@student.itstep.org

try:
    text = input("Enter a string: ")
    result = ""
    for i in range(len(text) -1,-1,-1):
        result += text[i]
    print(result)
except Exception as e :
    print("Error: ", e)
finally:
    print("Program terminated")
    exit()

# Path: string_application.py



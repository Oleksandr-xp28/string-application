# feature/hw/ex_3
# HW-2: Fedor_xp28@student.itstep.org

try:
    string = input("Enter a string: ")
    search_word = input("Search for: ")
    replace_word = input("Replace: ")

    words = string.split()
    for i in range(len(words)):
        if words[i] == search_word:
            words[i] = replace_word

    new_string = " ".join(words)
    print(new_string)
except Exception as e :
    print("Error: ", e)
finally:
#    print("Program terminated")
    exit()

# Path: string_application.py

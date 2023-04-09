# feature/hw/ex_4
# HW-2: Fedor_xp28@student.itstep.org

string = input("Enter a string: ")
word = input("Enter a word to search for: ")
count = 0

words = string.split()
for w in words:
    if w == word:
        count += 1

print(f"Word '{word}' Appears {count}.")

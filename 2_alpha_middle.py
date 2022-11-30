letter1 = input("1st letter: ")
letter2 = input("2nd letter: ")
letter3 = input("3rd letter: ")

middle = "a"

if letter1 > letter2 and letter1 > letter3:
    if letter3 > letter2:
            middle = letter3

if letter1 < letter2 and letter1 < letter3:
    if letter3 < letter2:
            middle = letter3

if letter1 < letter2 and letter1 < letter3:
    if letter3 > letter2:
            middle = letter2

if letter1 > letter2 and letter2 > letter3:
    middle = letter2

if letter1 < letter2 and letter1 > letter3:
    middle = letter1

if letter1 > letter2 and letter1 < letter3:
    middle = letter1

print(f"The letter in the middle is {middle}.")

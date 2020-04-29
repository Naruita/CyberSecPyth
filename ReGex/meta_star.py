import re

text = r"eggs(bacon)*"
user_input = input("Enter the text : ")

if re.match(text, user_input):
    print("Huh. You're right.")
else:
    print("DO IT JIM, KILL HIM")
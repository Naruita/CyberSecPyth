import re

pattern = r"bacon(eggs)*life"
user_input = input("Enter some text : ")

if re.match(pattern, user_input):
    print("You're right.")
else:
    print("PULL THE GODDAMN TRIGGER")
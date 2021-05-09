import re

pattern = r"^[A-Z][ABCD][0-9]$"
user_input = input("Do you live here? ")
if re.match(pattern, user_input):
    print("insane, you're right, you do live here.")
else:
    print("Hands UP")
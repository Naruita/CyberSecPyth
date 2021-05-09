import re

pattern = r"^gr.y$"
word = input("Enter text to test : ")
if re.match(pattern, word):
    print('match')
else:
    print('no match')

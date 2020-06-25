import re

sample_text = "Hey, this is adithya"
print(sample_text)
text_to_replace = input("Replace what? ")
replaced_text = input("With what? ")

newString = re.sub(text_to_replace, replaced_text, sample_text)
print(newString)

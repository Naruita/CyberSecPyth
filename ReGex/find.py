import re

pattern = r"eggs"
text = r"bacon, beggs, engs, and eddy engs."
if re.match(pattern, text):
    print('Match found')
else:
    print('No eggs')

if re.search(pattern, text):
    print('match gotten, search success')
else:
    print('search fail')

print(re.findall(pattern, text))



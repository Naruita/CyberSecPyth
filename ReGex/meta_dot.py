import re

pattern = r"gr.y"
if re.match(pattern, 'grayyyyasdfasdf'):
    print('Match found')
else:
    print('You didn\'t find it. Your\'e a loser.')

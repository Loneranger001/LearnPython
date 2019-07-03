import re

patterns = ['term1', 'term2']
text = 'This is a string with term1, but not with other term'

for pattern in patterns:
    print("Searching for pattern %s in string \n %s" % (pattern, text))
    match = re.search(pattern, text)
    if match :
        print('Matched object found')
    else:
        print('Not Found')


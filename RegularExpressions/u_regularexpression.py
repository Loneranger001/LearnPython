import re

patterns = ['term1', 'term2']
text = 'This is a string with term1, but not with other term'

for pattern in patterns:
    print("Searching for pattern %s in string \n %s" % (pattern, text))
    match = re.search(pattern, text)
    if match:
        print('Matched object found')
        print('Match started at position %d' % (match.start()))
    else:
        print('Not Found')


# findall

l_match = re.findall('match', 'This is First match and this is second match')
print(l_match)

# multi pattern find


def multi_re_find(patterns, phrase):
    '''
    :param pattern:
    :param phrase:
    :return:
    '''
    for pattern in patterns:
        print('Searching the phrase using the re check: %r' % pattern)
        print(re.findall(pattern, phrase))
        print('\n')




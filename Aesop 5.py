import re


def palindrome(phrase):
    phrase = re.sub('\s', '', phrase)
    phrase_list = re.findall('\w+', phrase)
    clean_phrase = ''.join(x for x in phrase_list)
    clean_phrase = clean_phrase.lower()

    number = 0
    for i in range(len(clean_phrase)):
        if clean_phrase[i] == clean_phrase[(-1 - i)]:
            # or phrase[i] == phrase[-1 - (-1 * i)]
            number += 1
        else:
            number += 0
    if number == len(clean_phrase):
        print('true')
    else:
        print('false')


palindrome('A man, a plan, a canal: Panama')
palindrome('race a car')
palindrome(' ')
palindrome('dad')



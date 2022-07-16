def palindrome(word):
    number = 0
    for i in range(len(word)):
        if word[i] == word[(-1 - i)]:
            # or word[i] == word[-1 - (-1 * i)]
            number += 1
        else:
            number += 0
    if number == len(word):
        print('This is a Palindrome')
    else:
        print('Not a Palindrome')


palindrome('dad')
palindrome('dar')
palindrome('civic')
palindrome('rotator')
palindrome('rubber')

def palindrome(file):
    length = int(input("Enter the length of the palindromes you desire: "))
    wordnum = 0
    for word in file:
        word = word.strip().lower()
        if len(word) == length:
            forward = word
            reverse = word
            forward = list(forward)
            reverse = list(reverse)
            reverse.reverse()
            if forward == reverse:
                print(word)
                wordnum += 1


    if wordnum > 0:
        print('There are ' + str(wordnum) + ' words that can fit this criteria.')
    if wordnum == 0:
        print('There are no words that fit this criteria.')

if __name__ == "__main__":
    my_file = open("dictionary.txt","r")
    palindrome(my_file)
    my_file.close()

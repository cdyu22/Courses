def onevowel(file):
    length = int(input("Please enter the word length you are looking for: "))
    letter = input("Please enter the letter you'd like to exclude: ")
    wordnum = 0
    for word in file:
        word = word.strip()
        if len(word) == length:
            count = 0
            for char in word:
                if (char=='a' or char=='e' or char=='i' or char=='o' or char=='u'):
                    count += 1
            if count == 1:
                flag = 1
                word_str = ""
                for char in word:
                    if char == letter:
                        flag = 0
                    else:
                        word_str += char
                if flag == 1:
                    print (word_str)
                    wordnum += 1
    if wordnum == 0:
        print ("There are no words that fit this criteria.")

if __name__ == "__main__":
    my_file = open("dictionary.txt","r")
    onevowel(my_file)
    my_file.close()

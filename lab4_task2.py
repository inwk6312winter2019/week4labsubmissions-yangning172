"""This function is for total numbers of words in the book"""


def count_words(file):
    f = open(file)
    mylist = list()
    count = 0
    import string

    for line in f:
        mylist.append(line)

    for word in mylist:
        word = word.strip(string.punctuation + string.whitespace)
        word = word.lower()
        for punc in string.punctuation:
            word = word.replace(punc, ' ')
        count += len(word.split(' '))
    print(count)


if __name__ == '__main__':
    count_words('c:\\users\\yn806\\desktop\\python course\\pycharm code\\projects\\word.txt')


"""This function is the number of times each word is used"""


def each_word(file):
    f = open(file)
    mylist = list()
    mylist2 = list()
    mydic = dict()
    import string

    for line in f:
        mylist.append(line)

    for word in mylist:
        word = word.strip(string.whitespace)
        word = word.lower()

        for punc in string.punctuation:
            word = word.replace(punc, ' ')

        for i in word.split(' '):
            mylist2.append(i)

    for key in mylist2:
        if key not in mydic:
            mydic[key] = 1
        else:
            mydic[key] = mydic[key] + 1
    print(mydic)
    return mydic


if __name__ == '__main__':
    count_words('c:\\users\\yn806\\desktop\\python course\\pycharm code\\projects\\word.txt')

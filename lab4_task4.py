def read_word(file1,file2):
    f = open(file1)
    mylist = list()

    for line in f:
        line = line.strip()

        import string
        for punc in string.punctuation:
            line = line.replace(punc, ' ')
        for i in line.split(' '):
            mylist.append(i)

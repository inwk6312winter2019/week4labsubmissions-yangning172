def file_read(file):
    f = open(file)
    mylist = list()
    for line in f:
        mylist.append(line)
    for word in mylist:
        import string
        word = word.strip(string.punctuation + string.whitespace)
        word = word.lower()
        print(word)


if __name__ == '__main__':
    file_read('c:\\users\\yn806\\desktop\\python course\\pycharm code\\projects\\word.txt')

"""Another way to do above purpose
def file_read(file):
    f = open(file)
    for line in f:
        line = line.strip()
        import string
        line = line.strip((string.punctuation + string.whitespace))
        line = line.lower()
        print(line)
"""

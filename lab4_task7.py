def sed(str1, str2, file1, file2):
    try:
        f1 = open(file1, 'r+')
        f2 = open(file2, 'a+')
        s1 = f1.read()
        f2.write(s1)
        f2.close()
        for line1 in f1:
            if str1 in line1:
                line1 = line1.replace(str1, str2)
        for line2 in f2:
            if str1 in line2:
                line2 = line2.replace(str1, str2)

    except:
        print('Error')

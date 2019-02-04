def search_duplicates(mp3_file):
    import os
    for name in os.listdir(mp3_file):
        for n in os.listdir(name):
            path = os.path.join(name, n)
            if path == name:
                print('duplicates')
            else:
                print('None')

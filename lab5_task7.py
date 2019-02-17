class Kangaroo:
    def __init__(self):
        self.pouch_contents = []

    def put_in_pouch(self, other):
        self.pouch_contents.append(other)
        return self.pouch_contents

    def __str__(self):
        return 'this is Kangaroo object: %s' % ''.join(self.pouch_contents)



kanga = Kangaroo()
roo = Kangaroo()

kanga.put_in_pouch('roo')
print(kanga)


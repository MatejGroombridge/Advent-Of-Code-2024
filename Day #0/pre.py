with open ('Day #0/text.txt', 'r') as f:
    data = f.read()
    for line in data:
        a = line.split()
        print(a)

class TextFile:
    def __init__(self, path):
        self.path = path
        with open (self.path, 'r') as f:
            self.data = f.read()
        print(self.data)

    def __repr__(self):
        return self.data
    
    def __str__(self):
        return self.data
    
    def __iter__(self):
        return iter(self.data)
    
    def __next__(self):
        return next(self.data)
    
    def __len__(self):
        return len(self.data)
    
    def __getitem__(self, index):
        return self.data[index]

newData = TextFile('Day #0/text.txt')
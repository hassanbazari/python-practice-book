class yrange:
    def __init__(self, n):
        self.i = 0
        self.n =  n[::-1]
    def __iter__(self):
        return self
    def next(self):
        if self.i < len(self.n):
            i = self.i
            self.i += 1
            print self.n[i]
        else:
            raise StopIteration()

class ExampleIterator:
    def __int__(self,data):
        self.index = 0
        self.data = data
        print(self.index)


    def __iter__(self):
        return self


    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration()

        rslt = self.data[self.index]
        self.index += 1
        return rslt

if __name__ == "__main__":
        i = ExampleIterator("[1,2,3]")
        next(i)

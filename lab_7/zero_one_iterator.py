# 7.6 a)
class ZeroOneIterator:
    def __iter__(self):
        self.value = 0
        return self

    def __next__(self):
        result = self.value
        self.value = (self.value + 1) % 2
        return result

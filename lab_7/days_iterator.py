# 7.6 c)
class DaysIterator:
    def __iter__(self):
        self.day = 0
        return self

    def __next__(self):
        result = self.day
        self.day = (self.day + 1) % 7
        return result

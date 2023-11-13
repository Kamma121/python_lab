# 7.6 b)
import random


class RandomIterator:
    def __iter__(self):
        return self

    def __next__(self):
        values = ["N", "E", "S", "W"]
        return random.choice(values)

L = [1, 2, 15, 30, 8, 21, 49, 120, 98, 777, 113]
with_zeros = [str(number).zfill(3) for number in L]
line = ''.join(with_zeros)
print(line)

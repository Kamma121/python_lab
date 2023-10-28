line = "consectetur adipiscing elit pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis"
words = line.split()
line_alpha = sorted(words)
print('Sorted alphabetically: ', line_alpha)
line_length = sorted(words, key=len)
print('Sorted by length: ', line_length)

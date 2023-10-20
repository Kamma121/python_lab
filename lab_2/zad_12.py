line = "consectetur adipiscing elit pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis"
words = line.split()
first_letter_word = ''.join(word[0] for word in words)
last_letter_word = ''.join(word[-1] for word in words)
print('First letters: ', first_letter_word)
print('Last letters: ', last_letter_word)

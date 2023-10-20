line = "consectetur adipiscing elit pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis"
words = line.split()
longest_word = max(words, key=len)
longest_word_length = len(longest_word)
print(f"Longest word: {longest_word}\nLength: {longest_word_length}")

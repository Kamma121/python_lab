line = "consectetur adipiscing elit pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis"
words = line.split()
final_length = sum(len(word) for word in words)
print("Final length is: ", final_length)

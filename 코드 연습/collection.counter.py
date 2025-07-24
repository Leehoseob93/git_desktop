from collections import defaultdict

# words_by_length = defaultdict(list)
words = ['hi','me','no','dog','cat','run','hello','hey','apple','aaabb']

words_by_length ={}
words_by_length = {}
for word in words:
    length = len(word)
    if length not in words_by_length:
        words_by_length[length] = []
    words_by_length[length].append(word)

# for word in words:
#     words_by_length[len(word)].append(word)

print(words_by_length)
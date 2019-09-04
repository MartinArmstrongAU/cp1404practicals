word_to_counts = {}

user_text = input("Text: ")
words = user_text.split()

for word in words:
    frequency = word_to_counts.get(word, 0)
    word_to_counts[word] = frequency + 1

words = list(word_to_counts.keys())
words.sort()

max_length = max(len(word) for word in words)
for word in words:
    print("{:{}} : {}".format(word, max_length, word_to_counts[word]))
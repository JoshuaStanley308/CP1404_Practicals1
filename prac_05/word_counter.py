
words_collection = {}

text = input("Text: ")
words = text.split()

for word in words:
    try:
        words_collection[word] += 1
    except KeyError:
        words_collection[word] = 1

word_list = list(words_collection)
word_list.sort()

max_length = max(len(word) for word in words)

for word in word_list:
    print("{:{}}: {}".format(word,max_length, words_collection[word]))

"""
A program for counting word frequencies in a document, and
reporting the most frequent word. We use Python’s dict class for the map. We
convert the input to lowercase and ignore any nonalphabetic characters.
"""
filename = 'skip-list-perf.html'
freq = {}

for piece in open(filename).read().lower().split():
    word = ''.join(c for c in piece if c.isalpha())
    if word:
        freq[word] = 1 + freq.get(word, 0)

max_word = ''
max_count = 0

for (w, c) in freq.items():
    if c > max_count:
        max_word = w
        max_count = c

print("The most frequent word is", max_word)
print("Its number of occurrences is", max_count)



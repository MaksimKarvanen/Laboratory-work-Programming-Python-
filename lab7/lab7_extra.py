import sys
    
text = sys.stdin.read()
clean_text = text.translate(str.maketrans('', '', '.'))
words = clean_text.split()

first = {}
for i, word in enumerate(words, start=0):
    if word not in first and word.istitle():
        first[word] = i

sorted_first = dict(sorted(first.items(), key=lambda item: item))

for i in sorted_first:
    print(f'{sorted_first[i]} - {i}')
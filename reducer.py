import sys
word_count = {}
for line in sys.stdin:
    line = line.strip()
    word, count = line.split('\t', 1)
    try:
        count = int(count)
    except ValueError:
        continue

   try:
        word_count[word] = word_count[word] + count
    except:
        word_count[word] = count


for word in word_count.keys():
    print '%s\t%s' % (word, word_count[word])

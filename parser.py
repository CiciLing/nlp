
from collections import Counter
from nltk.corpus import stopwords


def txt_parser(filename):
    f = open(filename)
    text = f.read()
    words = text.split()
    wc = Counter(words)
    num = len(words)

    bigrams = Counter(map(''.join, zip(words, words[1:])))

    #print(bigrams)


    f.close()
    return {'wordcount':wc, 'numwords':num}


print(txt_parser('trump.txt'))

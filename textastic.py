from collections import defaultdict, Counter
import matplotlib.pyplot as plt
import sankey as sk
import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from heapq import nlargest



class Textastic:

    def __init__(self):
        """ Constructor """
        self.data = defaultdict(dict) # extracted data (state)

    def _save_results(self, label, results):
        for k, v in results.items():
            self.data[k][label] = v


    @staticmethod
    def _default_parser(filename):
        f = open(filename, encoding = 'utf-8')
        text = f.read()
        words= text.split()
        stop_words = stopwords.words('english')
        stop_words.append('—')
        # put in lower case
        filtered_words = []
        words = [word.lower() for word in words]
        for word in words:
            if word not in stop_words:
                filtered_words.append(word)

        wc = dict(Counter(filtered_words))
        num = len(filtered_words)

        #bigrams = Counter(map(''.join, zip(filtered_words, words[1:])))

        #print(bigrams)
        f.close()
        return {'wordcount': wc, 'numwords': num}


    def load_text(self, filename, label=None, parser=None):
        """Registers the text file with the NLP framework"""

        if parser == None:
            results = Textastic._default_parser(filename)
        else:
            results = parser(filename)

        if label is None:
            label = filename

        self._save_results(label, results)

    def compare_num_words(self):
        num_words = self.data['numwords']
        for label, nw in num_words.items():
            plt.bar(label, nw)
        plt.show()

    # def _top10_words(self):
    #     top10_list = []
    #     wdict = Counter(self.data['wordcount'])
    #     for k,v in wdict.items():
    #         top = nlargest(15, v, key=v.get)
    #         top10_list.append(top)
    #     return top10_list


    def create_sankey(self,file1,file2,file3,file4):
        count_dict = self.data['wordcount']
        df = pd.DataFrame(count_dict[file1].items)


        print(df)
        #sk.make_sankey(wc_df, wc_df[''], wc_df[''])







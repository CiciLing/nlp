from collections import defaultdict, Counter
import matplotlib.pyplot as plt
import pandas as pd
from nltk.corpus import stopwords
import hw1 as hw
import nltk

# check update

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
        words = [word.strip('.') for word in words]
        words = [word.strip(':') for word in words]
        words = [word.strip(',') for word in words]
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

    def extract_local_data(self,file1,file2,file3,file4):
        count_dict = self.data['wordcount']
        df1 = pd.DataFrame(list(count_dict[file1].items()),columns=['word','frequency'])
        df1.insert(0, 'Name', file1)
        df2 = pd.DataFrame(list(count_dict[file2].items()),columns=['word','frequency'])
        df2.insert(0, 'Name', file2)
        df3 = pd.DataFrame(list(count_dict[file3].items()),columns=['word','frequency'])
        df3.insert(0, 'Name', file3)
        df4 = pd.DataFrame(list(count_dict[file4].items()), columns=['word', 'frequency'])
        df4.insert(0, 'Name', file4)

        df = pd.concat([df1, df2, df3, df4], ignore_index=True)
        return df

    def execute_sankey(self, df, col, val, word_list = None, k = None, **kwargs):
        '''
        :param df: original dataframe that contains selected data
        :param col: the targets and sources of the sankey diagram
        :param val: the name of grouped count column
        :return: a sankey diagram showing the connections
        '''
        if word_list == None and k != None:
            df2 = df.sort_values([val], ascending=False).groupby(col[0]).head(k)
        elif k == None and word_list != None:
            df2 = df[df['word'].isin(word_list)]
        else:
            min_val = kwargs.get('min_val', 7)
            df2 = df[df[val] >= min_val]
        hw.show_sankey(df2, col[0], col[1], vals=val)

    '''
    - tokenizing (splitting text into words) *which we already did* 
    - find unique words by converting to set 
    - # unique words/# total words so we need list of both to plot 
    '''
    def heaps_law(self, filename):
        # total words
        f = open(filename, encoding='utf-8')
        text = f.read()
        words = text.split()
        words = [word.lower() for word in words]

        total_word = []
        unique_word = []
        uniq = set()
        for i, token in enumerate(words):
            uniq.add(token)
            total_word.append(i)
            unique_word.append(len(uniq))
        return total_word, unique_word

    def plot_heaps(self, filename, label):
        all_data = []
        for i in range(len(filename)):
            file_data = []
            total_word, unique_word = Textastic.heaps_law(filename[i])
            file_data.append(total_word)
            file_data.append(unique_word)
            all_data.append(file_data)
            plt.plot(all_data[i][0], all_data[i][1], label=label)
        plt.title('Heaps Law')
        plt.legend()
        plt.show()








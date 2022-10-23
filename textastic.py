from collections import defaultdict, Counter
import matplotlib.pyplot as plt
import pandas as pd
from nltk.corpus import stopwords
import hw1 as hw
from nltk import tokenize
from textblob import TextBlob

class Textastic:
    def __init__(self):
        """ Constructor """
        self.data = defaultdict(dict) # extracted data (state)

    def _save_results(self, label, results):
        '''save results to data'''
        for k, v in results.items():
            self.data[k][label] = v

    @staticmethod
    def _load_stop_words(words, stop_file):
        '''
        Filter the stop words from file
        :param words: total words in a file
        :param stop_file: stop words that should get excluded
        :return: words in a file excluding the stop words
        '''
        # initializing empty list to store all words once filtered
        filtered_words = []
        # filtering out stop words
        for word in words:
            if word not in stop_file:
                filtered_words.append(word)
        return filtered_words
    @staticmethod
    def _default_parser(filename):
        '''
        Reads in the text files and does pre-processing to clean up the data and then returns some stats on the text.
        :param filename (str): the name of the file to be processed
        :return: a dictionary storing the file information including a dict counting each time a word is repeated,
        number of words, and a list of sentences
        '''

        # opening file and reading data
        f = open(filename, encoding='utf-8')
        text = f.read()

        # splitting text by words, converting to lowercase, and removing unnecessary characters
        words = text.split()
        stop_words = stopwords.words('english')
        stop_words.append('—')
        words = [word.lower() for word in words]
        words = [word.strip('.') for word in words]
        words = [word.strip(':') for word in words]
        words = [word.strip(',') for word in words]

        # remove stop words
        filtered_words = Textastic._load_stop_words(words,stop_words)

        # calling tokenize to seperate text into sentences
        sentences = tokenize.sent_tokenize(text)

        # count words counts and number of words
        wc = dict(Counter(filtered_words))
        num = len(filtered_words)
        f.close()

        return {'wordcount': wc, 'numwords': num, 'sentences': sentences}


    def load_text(self, filename, label=None, parser=None):
        """
        Registers the text file with the NLP framework"
        :param filename: the name of the file to be processed
        :param label: the dictionary keys that represent the name of files
        :param parser: parser that get basic information from files
        """

        if parser == None:
            results = Textastic._default_parser(filename)
        else:
            results = parser(filename)

        if label is None:
            label = filename

        self._save_results(label, results)

    def extract_local_data(self,file):
        '''
        :param file: the list of files a user input
        :return: a concat dataframe containing the name of file, words in file, and frequency of these words
        '''
        count_dict = self.data['wordcount']
        df = pd.DataFrame()
        for i in range(len(file)):
            df_file = pd.DataFrame(list(count_dict[file[i]].items()),columns=['word','frequency'])
            df = pd.concat([df, df_file], ignore_index=True)
        return df

    def wordcount_sankey(self, df, col, val, word_list = None, k = None, **kwargs):
        '''
        :param df: original dataframe that contains selected data
        :param col: the targets and sources of the sankey diagram
        :param val: the name of grouped count column
        :param word_list: users' specified list of words
        :param k: an integer using to retrieve k most common words
        :param kwargs: optional parameters eg. minimum values
        :return: a sankey diagram showing the connections
        '''
        if k == None and word_list != None:
            df2 = df[df[col[1]].isin(word_list)]
        elif word_list == None and k != None:
            df2 = df.sort_values([val], ascending=False).groupby(col[0]).head(k)
        else:
            min_val = kwargs.get('min_val', 7)
            df2 = df[df[val] >= min_val]
        hw.show_sankey(df2, col[0], col[1], vals=val)

    def sentiment_subplot(self):
        '''
        Creates a figure that renders subplots plotting the polarity and subjectivity values by sentences for each text.
        '''

        # pulls dictionary of sentences from data
        sentences_dict = self.data['sentences']
        # defining number of rows/cols based on number of text files in dict
        n = len(sentences_dict)
        cols = int(n ** .5)
        rows = n // cols
        if n % cols != 0:
            rows += 1

        # creates list going thru range of number of subplots to use for position
        position = range(1, n + 1)

        # initializing figure
        fig = plt.figure(1)

        # outer for loop: loops through position list to add subplots one by one
        # loops thru keys/values of sentences dict, creates list to store subjectivity/polarity values and graphs points
        # inner for loop: loops thru every sentence in sentences list, gets subjectivity/polarity values to add to list
        for i in range(n):
            for k, v in sentences_dict.items():
                polarity_list = []
                subjectivity_list = []
                for sentence in v:
                    text = TextBlob(sentence)
                    polarity_list.append(text.sentiment.polarity)
                    subjectivity_list.append(text.sentiment.subjectivity)
                ax = fig.add_subplot(rows, cols, position[list(sentences_dict).index(k)])
                ax.set_xlim([-1, 1])
                ax.set_ylim([0, 1])
                ax.scatter(polarity_list, subjectivity_list, s=5)
                ax.set(xlabel='Polarity', ylabel='Subjectivity')
                ax.set_title(k)

        # adding title/layout and displaying plot
        fig.suptitle('Sentiment Analysis')
        plt.tight_layout()
        plt.show()
    @staticmethod
    def heaps_law(filename):
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
            file_data = Textastic.heaps_law(filename[i])
            all_data.append(file_data)
            plt.plot(all_data[i][0], all_data[i][1], label=label[i])
        print(all_data)
        plt.title('Heaps Law')
        plt.xlabel('Total number of words')
        plt.ylabel('Unique number of words')
        plt.legend()
        plt.show()









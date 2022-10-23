from textastic import Textastic
import pprint as pp


def main():
    tt = Textastic()
    # the files that include president farewell addresses and their labels
    files = ['trump.txt', 'bush.txt', 'carter.txt', 'clinton.txt']
    labels = ['trump', 'bush', 'carter', 'clinton']

    # load files through parser
    for i in range(len(files)):
        tt.load_text(files[i], labels[i])
        # create dataframe for constructing sankey diagrams
        df = tt.extract_local_data(labels[i])

    #df = tt.extract_local_data('bush','carter','clinton','trump')
    # create and show sankey using name as target and word as source
    tt.wordcount_sankey(df, ['Name', 'word'], 'frequency', k = 5)

    # second viz: create subplots for each file showing the sentiments anaylsis
    tt.sentiment_subplot()

    # third viz: testing heaps law
    tt.plot_heaps(files, labels)


if __name__ == '__main__':
    main()
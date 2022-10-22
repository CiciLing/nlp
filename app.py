from textastic import Textastic
import pprint as pp


def main():
    tt = Textastic()
    tt.load_text('trump.txt', 'trump')
    tt.load_text('bush.txt', 'bush')
    tt.load_text('carter.txt', 'carter')
    tt.load_text('clinton.txt', 'clinton')
    df = tt.extract_local_data('bush','carter','clinton','trump')
    #tt.execute_sankey(df, ['Name', 'word'], 'frequency')
    files = ['trump.txt', 'bush.txt', 'carter.txt', 'clinton.txt']
    labels = ['trump','bush','carter','clinton']
    #tt.plot_heaps(files, labels)
    tt.sentiment_subplot()


if __name__ == '__main__':
    main()
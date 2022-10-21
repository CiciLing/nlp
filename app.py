from textastic import Textastic
import pprint as pp


def main():
    tt = Textastic()
    tt.load_text('trump.txt', 'trump')
    tt.load_text('bush.txt', 'bush')
    tt.load_text('carter.txt', 'carter')
    tt.load_text('clinton.txt', 'clinton')
    df = tt.extract_local_data('bush','carter','clinton','trump')
    #tt.execute_sankey(df, ['Name', 'word'], 'frequency', word_list = ['nuclear'])
    file_name = ['trump.txt', 'bush.txt', 'carter.txt', 'clinton.txt']
    label = ['trump','bush','carter','clinton']
    tt.plot_heaps(file_name, label)


if __name__ == '__main__':
    main()
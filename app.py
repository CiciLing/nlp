from textastic import Textastic
import pprint as pp


def main():
    tt = Textastic()
    tt.load_text('trump.txt', 'trump')
    tt.load_text('bush.txt', 'bush')
    tt.load_text('carter.txt', 'carter')
    tt.load_text('clinton.txt', 'clinton')
    df = tt.extract_local_data('bush','carter','clinton','trump')

    #tt.execute_sankey(df, ['Name', 'word'], 'frequency', k=10)


if __name__ == '__main__':
    main()
from textastic import Textastic
import pprint as pp
import sankey as sk
import hw1 as hw

def main():
    tt = Textastic()
    tt.load_text('trump.txt', 'trump')
    tt.load_text('bush.txt', 'bush')
    tt.load_text('carter.txt', 'carter')
    tt.load_text('clinton.txt', 'clinton')
    #pp.pprint(tt.data)
    #print(tt.top10_words())
    df = tt.create_sankey('bush','carter','clinton','trump')
    print(df)
    hw.execute_sankey(df, ['Name', 'word'], 'frequency')



if __name__ == '__main__':
    main()
from textastic import Textastic
import pprint as pp
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
    #hw.execute_sankey(df, ['Name', 'word'], 'frequency')
    # check pus
    df2 = hw.k_most_frequent(df, ['Name','frequency'])
    print(df2)
    hw.execute_sankey(df2, ['Name', 'word'], 'frequency')



if __name__ == '__main__':
    main()
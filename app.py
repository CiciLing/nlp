from textastic import Textastic
import pprint as pp

def main():
    tt = Textastic()
    tt.load_text('trump.txt', 'trump')
    tt.load_text('bush.txt', 'bush')
    tt.load_text('carter.txt', 'carter')
    tt.load_text('clinton.txt', 'clinton')
    #pp.pprint(tt.data)
    #print(tt.top10_words())
    tt.create_sankey('trump','bush','carter','clinton')



if __name__ == '__main__':
    main()
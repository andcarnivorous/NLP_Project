import nltk
from nltk import word_tokenize
from nltk.util import ngrams
import pickle
import argparse
import spacy


parser = argparse.ArgumentParser()
#Change the Defaults to your preference.
parser.add_argument('-f', '--file', default="/home/main/Documents/NLPProject/natives.tok") # CHANGE DEFAULT DIRECTORY TO FILE LOCATION
parser.add_argument("-p", "--pickle", default=False)
parser.add_argument("-k", "--keyword", default="plumber")
parser.add_argument("-g", "--grams", default=2)
args = parser.parse_args()

final_set = set()

def find_keyword(keyword, _list):
    # finds a keyword in any output from tokenize or ngrams.
    for x in _list:
        if isinstance(x, list):
            find_keyword(keyword, x)

        elif isinstance(x, str):
            if keyword in x:
                final_set.add(tuple(_list))

        else:
            for y in x:
                if keyword in y:
                    final_set.add(tuple(_list))

    return None

with open("%s" % args.file, "r") as f:
    f = f.readlines()
    
sentences = [word_tokenize(x) for x in f]



n_grams = [list(nltk.ngrams(x, args.grams)) for x in sentences]



#Define keyword and grams. 
find_keyword(args.keyword, n_grams)

print(final_set)

if args.pickle == True:
    with open('ngrams.pickle', 'wb') as handle:
        pickle.dump(n_grams, handle, protocol=pickle.HIGHEST_PROTOCOL)

    with open('keywordmatches.pickle', 'w') as handle:
        pickle.dump(final_set, handle, protocol=pickle.HIGHEST_PROTOCOL)
    

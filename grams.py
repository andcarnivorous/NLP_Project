import nltk
from nltk import word_tokenize
from nltk.util import ngrams
import pickle
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file', default="/home/main/Documents/NLPProject/natives.tok") # CHANGE DEFAULT DIRECTORY TO FILE LOCATION
parser.add_argument("-p", "--pickle", default=False)
parser.add_argument("-k", "--keyword", default="plumber")
args = parser.parse_args()


def find_keywordgrams(keyword, _list):

    for x in _list:
        if isinstance(x, list):
            find_keyword(keyword, x)

        else:
            for y in x:
                if keyword in y:
                    print(_list, "\n\n")


with open("%s" % args.file, "r") as f:
    f = f.readlines()

sentences = [word_tokenize(x) for x in f]

#bigrams = [list(nltk.bigrams(x)) for x in sentences]
trigrams = [list(nltk.trigrams(x)) for x in sentences]
#quadragrams = [list(nltk.ngrams(x, 4)) for x in sentences]

print(find_keywordgrams(args.keyword, trigrams))


if args.pickle == True:
    with open('bigrams.pickle', 'wb') as handle:
        pickle.dump(bigrams, handle, protocol=pickle.HIGHEST_PROTOCOL)

    with open('trigrams.pickle', 'wb') as handle:
        pickle.dump(trigrams, handle, protocol=pickle.HIGHEST_PROTOCOL)

    with open('quadragrams.pickle', 'wb') as handle:
        pickle.dump(quadragrams, handle, protocol=pickle.HIGHEST_PROTOCOL)

import spacy
import numpy as np
import en_core_web_md
from scipy import spatial
import scipy
import argparse

parser = argparse.ArgumentParser()
#Change the Defaults to your preference.
parser.add_argument('-f', '--file', default="natives.txt")
parser.add_argument("--POS", default="")
parser.add_argument("-k", "--keyword", default="")
parser.add_argument("-s", "--sentence", default="plumbers are workers")
parser.add_argument("-N", "--N", default=30)
args = parser.parse_args()

#print(args.keyword)
#print(type(args.keyword))

print("starting")

def get_closest(sent, _list, n):
    """
    Gets N closest sentences
    """ 
    distances = dict()

    for y,x in enumerate(_list):
        distance = scipy.spatial.distance.cosine(sent, x)
        distances[y] = distance
                
    distances = sorted(distances.items(), key=lambda kv: kv[1])
    return distances[:n]

def result(_list, f, keyword=False, PoS=False):
    """
    Rearrange and Filter sentences found by get_closest() by keyword and PoS if specified
    """
    sents = []
    vals = []
    for x in range(len(_list)):
        sents.append(f[_list[x][0]])
        vals.append(_list[x][1])

    result = list(zip(sents,vals))

    if keyword:
        result = [(x,y) for x,y in result if keyword in x.lower()]
                
    if PoS:
        posresult = list()
        for x,y in result:
            counter = 0
            x = nlp(x)
            for w in x:
                if PoS == w.pos_:
                    counter += 1
            if counter != 0:
                posresult.append((x,y))
            
        return posresult
    
    else:
        return result

    
with open("natives.txt", "r") as f:
    f = f.readlines()

nlp = spacy.load('en_core_web_md')

print("loaded")

vectors = [nlp(x) for x in f[:15000]] 

vectors = [x.vector for x in vectors] 

test_sent = nlp(args.sentence)

print("vectors extracted")

dis = get_closest(test_sent.vector, vectors, args.N)

if len(args.POS) < 1:
    args.POS = False
    
if len(args.keyword) < 1:
    args.keyword = False
    
print(result(dis, f,PoS= args.POS, keyword=args.keyword))

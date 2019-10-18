import spacy
import numpy as np
import en_core_web_md
from scipy import spatial
import scipy
print("starting")



with open("natives.txt", "r") as f:
    f = f.readlines()

nlp = spacy.load('en_core_web_md')

print("loaded")


vectors = [nlp(x) for x in f[:1000]]

vectors = [x.vector for x in vectors] 

test_sent = nlp("This is one area in which I believe the Commission can be a very great friend to Wales")

print("vectors extracted")


def get_closest(sent, _list, n):
    """
    Gets N closest sentences, they must include keyword or PoS if you want to
    """
    distances = dict()

    for y,x in enumerate(_list):
        distance = scipy.spatial.distance.cosine(sent, x)
        distances[y] = distance

    distances = sorted(distances.items(), key=lambda kv: kv[1])
    return distances[:n]

print("ok")

dis = get_closest(test_sent.vector, vectors, 10)

def result(_list, f):

    sents = []
    vals = []
    for x in range(len(_list)):
        sents.append(f[_list[x][0]])
        vals.append(_list[x][1])
    return list(zip(sents,vals))


print(result(dis, f))

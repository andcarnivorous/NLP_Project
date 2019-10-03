import nltk
from nltk import sent_tokenize
import os

path1 = 'native'
path2 = 'non-native'
paths = [path1,path2]

for x in paths:
    for f in os.listdir(x):
        with open(f, 'r') as _file:
            _file = _file.read()
            text = sent_tokenize(_file)
            with open(x+'.txt', 'w') as o:
                for s in text:
                    o.write(" ".join(o)+'\n')
                o.close()

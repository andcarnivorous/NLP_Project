# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 10:46:22 2019

@author: Tijev
"""

#%%
import gzip
import logging
import gensim
import os

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

os.chdir("C:\\Users\\Tijev\\OneDrive\\Documenten\\School\\Natural Language Processing\\data")
input_file = 'DA.txt.gz'
with gzip.open(input_file, 'rb') as f:
        for i,line in enumerate (f):
            print(line)
            break
        
def read_input(input_file):
    """This method reads the input file which is in gzip format"""
 
    logging.info("reading file {0}...this may take a while".format(input_file))
    with gzip.open(input_file, 'rb') as f:
        for i, line in enumerate(f):
 
            if (i % 10000 == 0):
                logging.info("read {0} reviews".format(i))
            # do some pre-processing and return list of words for each review
            # text
            yield gensim.utils.simple_preprocess(line)
            
test = read_input(input_file)
my_iterator = [x for x in test]


# build vocabulary and train model
"""
explanation about parameter settings:
size: the size of the dense vector to represent each token or word. If we have limited data, size should be smaller
window: maximum distance between target word and neighboring word
min_count: minimum frequency count of words.
workers: how many threads behind the scenes?
iter: number of epochs
"""
model = gensim.models.Word2Vec(my_iterator,size=150, window=10, min_count=2,workers=10,iter=10)


# test top6 words for similarity
w1 = "president"
model.wv.most_similar(positive=w1, topn=6)      

#similarity between two words
model.wv.similarity(w1='president', w2='woman')
model.wv.similarity(w1='president', w2='man')





    
    
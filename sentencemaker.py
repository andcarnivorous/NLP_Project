import nltk
from nltk import sent_tokenize
import os
import spacy

nlp = spacy.load('en_core_web_md')

nlp.vocab["he"].is_stop = False
nlp.vocab["she"].is_stop = False
nlp.vocab["his"].is_stop = False
nlp.vocab["her"].is_stop = False
nlp.vocab["it"].is_stop = False
nlp.vocab["him"].is_stop = False
nlp.vocab["hers"].is_stop = False
nlp.vocab["himself"].is_stop = False
nlp.vocab["herself"].is_stop = False

path1 = 'natives'
path2 = 'non-natives'
path3 = "nativestok"
paths = [path1,path2, path3]


def remove_stopwords(sents):
    new_sentences = []
    for sent in sents:
        doc = nlp(sent)
        sent = [token.text for token in doc if not token.is_stop and not token.is_punct]
        new_sentences.append(" ".join(sent))
    return new_sentences



for x in paths:
    for f in os.listdir(x):
        try:
            with open(x+"/"+f, 'r') as _file:
                _file = _file.read()

                text = sent_tokenize(_file)
                text = remove_stopwords(text)

                with open(x+'.txt', 'a') as o:
                    for s in text:
                        o.write(s+'\n')
                    o.close()
        except:
            continue
        
print("Ran")

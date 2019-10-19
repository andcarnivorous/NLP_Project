# Read me

To replicate the results of the paper, you need:

1. Download the British Academic Written English Corpus (BAWE). The dataset is freely available on http://ota.ahds.ac.uk/headers/2539.xml
2. Extract the dataset into the main directory 
3. Run the scripts in the following order:
- sorter.py 
- preprocessbawe.py
- sentencemaker.py
- sent_vec.py

N.B.: You need to have the en_core_web_md model from spacy installed. To install it run:

```
python3 -m spacy download en_core_web_md
```


### To filter by keyword, the following command is used:
```
python3 sent_vec.py --keyword="your_keyword_here"
```

### To filter by POS, the following command is used:
```
python3 sent_vec.py --POS="your_pos_here"
```

### To filter by sentence (your sentence), use:
```
python3 sent_vec.py --sentence="your_sentence_here"
```

### To run the script on a different input file, use:
```
python3 sent_vec.py --file="your_file"
```

### The complete description of options can be checked by using the `-h` option like:
```
python3 sent_vec.py -h
```

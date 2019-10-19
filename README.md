# Read me

To replicate the results of the paper, you need:

1. Download the British Academic Written English Corpus (BAWE). The dataset is freely available on http://ota.ahds.ac.uk/headers/2539.xml
2. Extract the dataset into the main directory 
3. Run the scripts in the following order:
- sorter.py 
- preprocessbawe.py
- sentencemaker.py
- sent_vec.py

Filter by keyword

```
python3 sent_vec.py --keyword="your_keyword_here"
```

Filter by sentence (your sentence)

```
python3 sent_vec.py --sentence="your_keyword_here"
```

Filter by POS

```
python3 sent_vec.py --POS="your_pos_here"
```
Input file

```
python3 sent_vec.py --file="your_file"
```

The complete description of options can be checked by using the `-h` option like:

```
python3 sent_vec.py -h
```


**Need to:** 

**- add instructions on how to run the system from the command line,** 

**- explain what variables can be changed/how to do that.** 

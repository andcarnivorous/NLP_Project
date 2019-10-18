# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 14:06:20 2019

@author: Tijev
"""

#%%
import os
import pandas as pd
import shutil

os.chdir("/home/main/Downloads/2539/")


doc = pd.read_excel("BAWE.xls")

directory = os.chdir('download/CORPUS_TXT')

doc.iloc[0][25]

for index, filename in enumerate(os.listdir(directory)):
    if doc.iloc[index][25] == 'English':
        print("ok")
        newPath = shutil.copy(filename, '/home/main/Documents/natives/')
    else:
        print("not ok")
        newPath2 = shutil.copy(filename, '/home/main/Documents/non-natives/')

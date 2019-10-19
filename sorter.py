# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 14:06:20 2019

@author: Tijev
"""

#%%
import os
import pandas as pd
import shutil

os.chdir("2539/")


doc = pd.read_excel("download/documentation/BAWE.xls")

directory = os.chdir('download/CORPUS_TXT')

doc.iloc[0][25]

for index, filename in enumerate(os.listdir(directory)):
    if doc.iloc[index][25] == 'English':
        newPath = shutil.copy(filename, '/natives/')
    else:
        newPath2 = shutil.copy(filename, '/non-natives/')

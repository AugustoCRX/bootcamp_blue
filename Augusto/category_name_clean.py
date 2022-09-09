import numpy as np
import re
import sys
from bootcamp_main_dataframe import test, train

# Remove special caracters from a list and return itself
def remove_especial_caracters(dataframe_column):
    complete_array = []
    for n in range(len(dataframe_column)):
        array = re.split('/|&', str(dataframe_column[n]))
        for i in range(len(array)):
            x = str(array[i])
            y = re.findall('\w', x)
            sentence = ''.join(y)
            complete_array.append(sentence)
    return complete_array

train_frame = remove_especial_caracters(train['category_name'])
test_frame = remove_especial_caracters(test['category_name'])

unique, counts = np.unique(test_frame, return_counts=True)
frame = np.stack((unique, counts), axis = 1)
import pandas as pd
import numpy as np
import os

from pandas.core.indexes.base import Index


new_data = pd.read_excel('C:\\Users\iori_\Documents\webauto_python\output.xlsx')
new_data.dropna(inplace=True)
#new_data.set_index('#',inplace=True)
#
print(new_data)
new_data.to_excel('C:\\Users\iori_\Documents\webauto_python\output.xlsx', index=False,sheet_name='Youtube names scrapping')
#
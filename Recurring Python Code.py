# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 21:23:55 2018

@author: jlhobson
"""

# <codecell>
#Import everything
import numpy as np
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
import os
pd.set_option('display.max_rows', 2000)
pd.set_option('display.max_columns', 300)

# <codecell>
# Import Excel
df1 = pd.read_excel(
'C:\\Users\\jlhobson\\Documents\\_Research\\Alumni Lists\\CPAAlums_121317.xlsx', 
#converters={'columnname':str}
)

# <codecell>

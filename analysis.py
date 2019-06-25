import pandas as pd

# import numpy as np

data = pd.read_csv('data.csv')

data.sort_values(by='Company')
print(data)
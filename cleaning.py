import numpy as np
import pandas as pd

# Import data
df = pd.read_csv('data_export_2021-06-09.csv')

# Cleaning
df.City = 'Iligan'

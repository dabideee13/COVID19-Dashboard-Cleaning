import numpy as np
import pandas as pd

# Import data
df = pd.read_csv('data_export_2021-06-09.csv')

# Cleaning: 'City' and 'Province'
df.City = 'Iligan'
df.Province = 'Lanao del norte'

# Cleaning: 'Exposure'
df.Exposure = (
    df.Exposure
    .apply(
        lambda x: 'COVID-19 POSITIVE'
        if str(x).startswith('COVID')
        else x
    )
    .apply(
        lambda x: str(x).replace('IC', 'IC-')
        if (str(x).startswith('IC') and str(x)[2] != '-')
        else x
    )
    .replace(
        'Work Cross Contamination',
        'Workplace Cross Contamination'
    )
    .apply(
        lambda x: np.nan
        if str(x) == 'nan'
        else x
    )
    .replace(
        'IC-1746 IC-1747',
        'IC-1746, IC-1747'
    )
)

# Unique values checker without the 'IC' patterns
# df.Exposure = df.Exposure.apply(lambda x: np.nan if not str(x).startswith('IC') else x)

# FIXME: Age (0.25, 0.4, 0.8)
# FIXME: Workplace Contamination, Facility Cross Contamination, Cross Contamination

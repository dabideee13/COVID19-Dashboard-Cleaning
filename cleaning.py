import re

import numpy as np
import pandas as pd


def change(x: str, old_word: str, new_word: str) -> str:
    return re.sub(rf'\b{old_word}\b', new_word, x)


def main():

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

    # Cleaning 'Remarks'
    df.Remarks = (
        df.Remarks
        .apply(
            lambda x: str(x).title()
            if 'sector' in str(x)
            else x
        )
        .apply(
            lambda x: 'Travel History: ' + x[24:]
            if str(x).startswith('Has')
            else x
        )
        .apply(
            lambda x: 'Medical Sector'
            if str(x).startswith('Medical')
            else x
        )
        .apply(
            lambda x: change(str(x), 'Kauswagan', 'Kauswagan, LDN')
            if 'Kauswagan' in str(x) and 'LDN' not in str(x)
            else x
        )
    )


if __name__ == '__main__':
    main()

# string = str(x).split(sep=', ')
# lambda x: change(str(x), string[0], string)


# Unique values checker without the 'IC' patterns
# df.Exposure = df.Exposure.apply(lambda x: np.nan if not str(x).startswith('IC') else x)

# FIXME: Age (0.25, 0.4, 0.8)
# FIXME: Workplace Contamination, Facility Cross Contamination, Cross Contamination
# FIXME: Does 'From Cebu' mean 'COVID-19 POSITIVE from Cebu' or 'Travel History: Cebu', similarly with others


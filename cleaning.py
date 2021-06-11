import re

import numpy as np
import pandas as pd


def change(x: str, old_word: str, new_word: str) -> str:
    return re.sub(rf'\b{old_word}\b', new_word, x)


def change_word(x: str):
    try:
        if 'LDN' in str(x):
            return change(
                str(x),
                get_word(x) + ', LDN',
                get_word(x)
            )
        if 'LDS' in str(x):
            return change(
                str(x),
                get_word(x) + ', LDS',
                get_word(x)
            )
        else:
            return x
    except Exception:
        return x


def get_list(x: str) -> list:
    return str(x).split(sep=' ')


def get_index(x: str) -> int:
    if 'LDN' in str(x):
        return get_list(x).index('LDN') - 1
    if 'LDS' in str(x):
        return get_list(x).index('LDS') - 1


def get_word(x: str) -> str:
    return (
        get_list(x)[get_index(x)]
        .strip()
        .replace(',', '')
    )


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
        .apply(
            lambda x: str(x)[:3] + '000' + str(x)[3:]
            if str(x).startswith('IC') and len(str(x)[3:7]) == 1
            else x
        )
        .apply(
            lambda x: str(x)[:3] + '00' + str(x)[3:]
            if str(x).startswith('IC') and len(str(x)[3:7]) == 2
            else x
        )
        .apply(
            lambda x: str(x)[:3] + '0' + str(x)[3:]
            if str(x).startswith('IC') and len(str(x)[3:7]) == 3
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

    # Cleaning: `Case Number`
    df['Case Number'] = (
        df['Case Number']
        .apply(
            lambda x: str(x)[:3] + '000' + str(x)[3:]
            if str(x).startswith('IC') and len(str(x)[3:7]) == 1
            else x
        )
        .apply(
            lambda x: str(x)[:3] + '00' + str(x)[3:]
            if str(x).startswith('IC') and len(str(x)[3:7]) == 2
            else x
        )
        .apply(
            lambda x: str(x)[:3] + '0' + str(x)[3:]
            if str(x).startswith('IC') and len(str(x)[3:7]) == 3
            else x
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
        .apply(change_word)
        .apply(
            lambda x: change(
                str(x),
                'Cagayan de Oro',
                'CDO'
            )
        )
        .replace(
            'Travel History; CDO',
            'Travel History: CDO'
        )
    )

    # Export data to csv
    df.to_csv('data_cleaned.csv', index=False)


if __name__ == '__main__':
    main()


# Unique values checker without the 'IC' patterns
# df.Exposure = df.Exposure.apply(lambda x: np.nan if not str(x).startswith('IC') else x)

# FIXME: Workplace Contamination, Facility Cross Contamination, Cross Contamination
# FIXME: Does 'From Cebu' mean 'COVID-19 POSITIVE from Cebu' or 'Travel History: Cebu', similarly with others




(
    df.Exposure
    .apply(
        lambda x: str(x).split(', ')[0]
        if str(x).startswith('IC') and len(str(x)) > 7
        else x
    )


def pre_zero(x):
    if str(x).startswith('IC') and len(str(x)[3:7]) == 1:
        return str(x)[:3] + '000' + str(x)[3:]
    elif str(x).startswith('IC') and len(str(x)[3:7]) == 2:
        return str(x)[:3] + '00' + str(x)[3:]

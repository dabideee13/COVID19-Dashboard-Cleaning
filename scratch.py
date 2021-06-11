


(
    df.Exposure
    .apply(
        lambda x: str(x).split(', ')[0]
        if str(x).startswith('IC') and len(str(x)) > 7
        else x
    )
)


def clean_two_expose(x: str) -> str:

    if str(x).startswith('IC') and len(str(x)) > 7:
        return list(str(x).split(', ')[0])

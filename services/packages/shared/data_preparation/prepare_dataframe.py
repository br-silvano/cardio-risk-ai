import pandas as pd


def prepare_dataframe(data) -> pd.DataFrame:
    df = pd.DataFrame(data)
    df['genero'] = df['genero'].map({'M': 0, 'F': 1, 'O': 2})
    df['historico_familiar'] = df['historico_familiar'].map({'S': 1, 'N': 0})
    df['historico_tabagismo'] = df['historico_tabagismo'].map({'S': 1, 'N': 0})
    df['consumo_alcool'] = df['consumo_alcool'].map({'S': 1, 'N': 0})
    df['hipertensao'] = df['hipertensao'].map({'S': 1, 'N': 0})
    return df

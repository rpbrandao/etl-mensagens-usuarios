import pandas as pd

def extract_data(path):
    try:
        df = pd.read_csv(path)
        print("Dados extraídos com sucesso.")
        return df
    except Exception as e:
        print(f"Erro na extração: {e}")
        raise

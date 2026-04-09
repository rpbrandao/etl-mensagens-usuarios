def load_data(df, path):
    try:
        df.to_csv(path, index=False)
        print("Dados carregados com sucesso.")
    except Exception as e:
        print(f"Erro no carregamento: {e}")
        raise

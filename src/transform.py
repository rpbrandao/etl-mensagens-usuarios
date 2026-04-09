def create_message(row):
    return f"Olá {row['nome']}, sua conta {row['conta']} está ativa! Aproveite seus benefícios do cartão {row['cartao']}."

def transform_data(df):
    df['mensagem'] = df.apply(create_message, axis=1)
    print("Dados transformados com sucesso.")
    return df

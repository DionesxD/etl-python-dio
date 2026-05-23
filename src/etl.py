import pandas as pd
from pathlib import Path


CAMINHO_ENTRADA = Path("data/usuarios.csv")
CAMINHO_SAIDA = Path("data/usuarios_com_mensagens.csv")


def extrair_dados(caminho_arquivo):
    """
    Etapa de Extração:
    Lê os dados dos usuários a partir de um arquivo CSV.
    """
    return pd.read_csv(caminho_arquivo)


def gerar_mensagem_personalizada(usuario):
    """
    Etapa de Transformação:
    Gera uma mensagem personalizada para cada usuário.

    Neste projeto, a mensagem é gerada por lógica em Python,
    simulando uma etapa de personalização que poderia ser feita por IA.
    """
    nome = usuario["nome"]
    conta = usuario["conta"]
    cartao = usuario["cartao"]

    mensagem = (
        f"Olá, {nome}! Sua conta {conta} está pronta para receber novas soluções digitais. "
        f"Aproveite os benefícios disponíveis no seu cartão {cartao} e continue evoluindo "
        f"sua vida financeira com segurança e praticidade."
    )

    return mensagem


def transformar_dados(df):
    """
    Aplica a transformação nos dados, criando uma nova coluna com mensagens.
    """
    df["mensagem_personalizada"] = df.apply(gerar_mensagem_personalizada, axis=1)
    return df


def carregar_dados(df, caminho_saida):
    """
    Etapa de Carregamento:
    Salva o resultado final em um novo arquivo CSV.
    """
    df.to_csv(caminho_saida, index=False, encoding="utf-8-sig")


def executar_pipeline():
    print("Iniciando pipeline ETL...")

    print("Extraindo dados...")
    usuarios = extrair_dados(CAMINHO_ENTRADA)

    print("Transformando dados...")
    usuarios_transformados = transformar_dados(usuarios)

    print("Carregando dados transformados...")
    carregar_dados(usuarios_transformados, CAMINHO_SAIDA)

    print(f"Pipeline finalizado com sucesso!")
    print(f"Arquivo gerado em: {CAMINHO_SAIDA}")


if __name__ == "__main__":
    executar_pipeline()
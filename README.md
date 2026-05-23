# Pipeline ETL com Python

Projeto desenvolvido como parte de um desafio prático de Ciência de Dados com Python, com foco no entendimento do fluxo ETL: Extração, Transformação e Carregamento.

## Objetivo

O objetivo deste projeto é simular um pipeline ETL utilizando Python, sem depender de APIs externas. A proposta original utilizava uma API pública, mas como ela pode ficar indisponível, foi adotada uma solução alternativa com arquivo CSV.

## Fluxo ETL

### 1. Extração

Os dados dos usuários são extraídos a partir do arquivo CSV:

[usuarios.csv](data/usuarios.csv)

O arquivo contém informações fictícias como:

- ID
- Nome
- Conta
- Cartão

### 2. Transformação

Durante a transformação, o script gera uma mensagem personalizada para cada usuário com base nos dados disponíveis.

Essa etapa simula o uso de IA ou lógica de personalização para criação de mensagens automáticas.

### 3. Carregamento

Após a transformação, os dados enriquecidos são salvos em um novo arquivo CSV:

[usuarios_com_mensagens.csv](data/usuarios_com_mensagens.csv)

## Estrutura do Projeto

```txt
etl-python-dio/
│
├── data/
│   ├── usuarios.csv
│   └── usuarios_com_mensagens.csv
│
├── src/
│   └── etl.py
│
├── README.md
├── requirements.txt
└── .gitignore

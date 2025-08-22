import pandas as pd
from pathlib import Path

# Leitura dos dados
data_path = Path('../data/clientes-v2.csv')
df = pd.read_csv(data_path)
print(df.head().to_string())
print(df.tail().to_string())

# Converte a coluna data para o tipo datetime
df['data'] = pd.to_datetime(df['data'], format='%d/%m/%Y', errors='coerce')

# Verificação inicial
print('Verificação Inicial: ')
print(df.info())

# Análise de valores nulos
print('Análise de dados nulos: \n', df.isnull().sum().sum())
print('% de dados nulos: \n', df.isnull().mean() * 100)

# Remove todas as linhas que possuem qualquer valor nulo.
df.dropna(inplace=True)
print('Confirmar remoção de dados nulos:\n', df.isnull().sum().sum())

print('Análise de dados duplicados: \n ', df.duplicated().sum())
print('Análise de dados únicos: \n', df.nunique())

#  Estatísticas descritivas
print('Estatísticas dos dados: \n', df.describe())

# Mantém apenas as colunas que serão utilizadas para a análise.
df = df[['idade', 'data', 'estado', 'salario', 'nivel_educacao',
         'numero_filhos', 'estado_civil', 'area_atuacao']]
print(df.head().to_string())

# Salvando o DataFrame tratado
df.to_csv('clientes-v2-tratados.csv', index=False)
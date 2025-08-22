import pandas as pd
import numpy as np
from scipy import stats
from pathlib import Path

# Leitura dos Dados
pd.set_option('display.width', None)
data_path = Path('../data/clientes-v2-tratados.csv')
df = pd.read_csv(data_path)
print(df.head())

# Transformação Logarítmica
df['salario_log'] = np.log1p(df['salario']) # log1p é usado para evitar problemas com valores zero
print("\nDataFrame após transformação logarítmica no 'salario':\n", df.head())

# Transformação Box-Cox
df['salario_boxcox'], _ = stats.boxcox(df['salario'] + 1)
print("\nDataFrame após transformação Box-Cox no 'salario':\n", df.head())

# Codificação de Frequência para 'estado'
estado_freq = df['estado'].value_counts() / len(df)
df['estado_freq'] = df['estado'].map(estado_freq)
print("\nDataFrame após codificação de frequência para 'estado':\n", df.head())

# Interações
df['interacao_idade_filhos'] = df['idade'] * df['numero_filhos']
print("\nDataFrame após criação de interações entre 'idade' e 'numero_filhos':\n", df.head())

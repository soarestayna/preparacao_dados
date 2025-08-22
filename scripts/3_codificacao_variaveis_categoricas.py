import pandas as pd
from sklearn.preprocessing import LabelEncoder
from pathlib import Path

# Leitura dos dados
pd.set_option('display.width', None)
data_path = Path('../data/clientes-v2-tratados.csv')
df = pd.read_csv(data_path)
print(df.head())

# Codificação one-hot
df = pd.concat([df, pd.get_dummies(df['estado_civil'], prefix='estado_civil')],axis=1)
print("\nDataFrame após codificação one-hot para 'estado_civil':\n", df.head())

# Codificação ordinal
educacao_ordem = {'Ensino Fundamental': 1, 'Ensino Médio': 2, 'Ensino Superior': 3, 'Pós-graduação': 4}
df['nivel_educacao_ordinal'] = df['nivel_educacao'].map(educacao_ordem)
print("\nDataFrame após codificação ordinal para 'nivel_educacao':\n", df.head())

# Transformar em categorias codificadas
df['area_atuacao_cod'] = df['area_atuacao'].astype('category').cat.codes
print("\nDataFrame após transformar 'area_atuacao' em códigos numéricos:\n", df.head())

# LabelEncoder
label_encoder = LabelEncoder()
df['estado_cod'] = label_encoder.fit_transform(df['estado'])
print("\nDataFrame após aplicar LabelEncoder em 'estado':\n", df.head())
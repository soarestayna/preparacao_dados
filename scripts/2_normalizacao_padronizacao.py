import pandas as pd
from sklearn.preprocessing import RobustScaler, MinMaxScaler, StandardScaler
from pathlib import Path

# Leitura dos dados
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

data_path = Path('../data/clientes-v2-tratados.csv')
df = pd.read_csv(data_path)
print(df.head())
print('\n')

# Seleção das variáveis
df = df[['idade', 'salario']]

# Normalização - MinMaxScaler
scaler = MinMaxScaler()
df['idadeMinMaxScaler'] = scaler.fit_transform(df[['idade']])
df['salarioMinMaxScaler'] = scaler.fit_transform(df[['salario']])

min_max_scaler = MinMaxScaler(feature_range=(-1, 1))
df['idadeMinMaxScaler_mm'] = min_max_scaler.fit_transform(df[['idade']])
df['salarioMinMaxScaler_mm'] = min_max_scaler.fit_transform(df[['salario']])

# Padronização - StandartScaler
scaler = StandardScaler()
df['idadeStandardScaler'] = scaler.fit_transform(df[['idade']])
df['salarioStandardScaler'] = scaler.fit_transform(df[['salario']])

# Padronização - RobustScaler
scaler = RobustScaler()
df['idadeRobustScaler'] = scaler.fit_transform(df[['idade']])
df['salarioRobustScaler'] = scaler.fit_transform(df[['salario']])

print(df.head(15))


# Resultados
print('MinMaxScaler (De 0 a 1):')

print('Idade - Min: {:.4f} Max: {:.4f} Mean: {:.4f} Std: {:.4f}'.format(
    df['idadeMinMaxScaler'].min(),
    df['idadeMinMaxScaler'].max(),
    df['idadeMinMaxScaler'].mean(),
    df['idadeMinMaxScaler'].std()
))

print('Salário - Min: {:.4f} Max: {:.4f} Mean: {:.4f} Std: {:.4f}'.format(
    df['salarioMinMaxScaler'].min(),
    df['salarioMinMaxScaler'].max(),
    df['salarioMinMaxScaler'].mean(),
    df['salarioMinMaxScaler'].std()
))

print('\n MinMaxScaler (De -1 a 1):')

print('Idade - Min: {:.4f} Max: {:.4f} Mean: {:.4f} Std: {:.4f}'.format(
    df['idadeMinMaxScaler_mm'].min(),
    df['idadeMinMaxScaler_mm'].max(),
    df['idadeMinMaxScaler_mm'].mean(),
    df['idadeMinMaxScaler_mm'].std()
))

print('Salário - Min: {:.4f} Max: {:.4f} Mean: {:.4f} Std: {:.4f}'.format(
    df['salarioMinMaxScaler'].min(),
    df['salarioMinMaxScaler_mm'].max(),
    df['salarioMinMaxScaler_mm'].mean(),
    df['salarioMinMaxScaler_mm'].std()
))

print('\n StandardScaler (Ajuste a média a 0 e desvio padrão a 1):')

print('Idade - Min: {:.4f} Max: {:.4f} Mean: {:.18f} Std: {:.4f}'.format(
    df['idadeStandardScaler'].min(),
    df['idadeStandardScaler'].max(),
    df['idadeStandardScaler'].mean(),
    df['idadeStandardScaler'].std()
))

print('Salário - Min: {:.4f} Max: {:.4f} Mean: {:.18f} Std: {:.4f}'.format(
    df['salarioStandardScaler'].min(),
    df['salarioStandardScaler'].max(),
    df['salarioStandardScaler'].mean(),
    df['salarioStandardScaler'].std()
))

print('\nRobustScaler (Ajuste a mediana e IQR):')

print('Idade - Min: {:.4f} Max: {:.4f} Mean: {:.4f} Std: {:.4f}'.format(
    df['idadeRobustScaler'].min(),
    df['idadeRobustScaler'].max(),
    df['idadeRobustScaler'].mean(),
    df['idadeRobustScaler'].std()
))

print('Salário - Min: {:.4f} Max: {:.4f} Mean: {:.4f} Std: {:.4f}'.format(
    df['salarioRobustScaler'].min(),
    df['salarioRobustScaler'].max(),
    df['salarioRobustScaler'].mean(),
    df['salarioRobustScaler'].std()
))
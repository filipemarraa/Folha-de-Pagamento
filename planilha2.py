import pandas as pd

# Caminho para o seu arquivo CSV
caminho_do_arquivo = 'atividade-implementacao-dados.csv'

# Lendo o arquivo CSV de dados bruto
df = pd.read_csv(caminho_do_arquivo)

# Filtrando e renomeando as colunas desejadas do dado bruto
colunas_desejadas = ['CargoS', 'Salário']
df_filtrado = df[colunas_desejadas]
df_filtrado.rename(columns={'CargoS': 'cargo', 'Salário': 'salario'}, inplace=True)

# Salvando o arquivo final
df_filtrado.to_csv('planilha_cargo_salario.csv', index=False)
print("A planilha foi filtrada e salva como 'planilha_cargo_salario.csv'.")
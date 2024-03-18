import pandas as pd

# Caminho para o seu arquivo CSV
caminho_do_arquivo = 'atividade-implementacao-dados.csv'

# Lendo o arquivo CSV de dados bruto
df = pd.read_csv(caminho_do_arquivo)

# Filtrando e renomeando as colunas desejadas do dado bruto
colunas_desejadas = ['Funcionários', 'Banco', 'Cargo', 'Salário', 'Dias trabalhados em abril', 'Salário família']
df_filtrado = df[colunas_desejadas]
df_filtrado.rename(columns={'Funcionários': 'colaborador', 'Dias trabalhados em abril': 'dias_trab', 'Banco': 'banco', 'Salário família': 'salario_fami', 'Cargo': 'cargo'}, inplace=True)

# Lendo CSV separado de cargos x salarios
df_cargo_sal = pd.read_csv('planilha_cargo_salario.csv')

# Mesclando a planilha filtrada com a de cargos x salarios
df_mesclado = pd.merge(df_filtrado, df_cargo_sal, on='cargo', how='left')

# Filtrando e renomeando colunas da tabela definitiva
filtrando_definitivo = ['colaborador', 'salario', 'dias_trab', 'salario_fami', 'banco']
df_final = df_mesclado[filtrando_definitivo]
df_final.rename(columns={'salário': 'cargo_salario'}, inplace=True)

# Salvando o arquivo final
df_final.to_csv('planilha_final.csv', index=False)
print("A planilha foi filtrada e salva como 'planilha_final.csv'.")
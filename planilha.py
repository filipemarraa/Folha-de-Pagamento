import pandas as pd

# Caminho para o seu arquivo CSV
caminho_do_arquivo = '/Users/filipemarra/Downloads/atividade-implementacao-dados.csv'

# Lendo o arquivo CSV
df = pd.read_csv(caminho_do_arquivo)

# Filtrando as colunas desejadas
colunas_desejadas = ['Funcionários', 'Banco', 'Cargo', 'Salário', 'Dias trabalhados em abril', 'Salário família']
df_filtrado = df[colunas_desejadas]
df_filtrado.rename(columns={'Funcionários': 'colaborador', 'Dias trabalhados em abril': 'dias_trab', 'Banco': 'banco', 'Salário família': 'salario_fami'}, inplace=True)


# Salvando o dataframe filtrado em um novo arquivo CSV
df_filtrado.to_csv('planilha_limpa.csv', index=False)

print("A planilha foi filtrada e salva como 'planilha_limpa.csv'.")

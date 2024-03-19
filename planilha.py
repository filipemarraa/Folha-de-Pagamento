import pandas as pd

# Caminho para o seu arquivo CSV
caminho_do_arquivo = 'atividade-implementacao-dados.csv'

# Lendo o arquivo CSV de dados bruto
df = pd.read_csv(caminho_do_arquivo)

# Primeira filtragem do CSV original
colunas_desejadas = ['Funcionários', 'Cargo', 'Salário', 'Dias trabalhados em abril', 'Salário família', 'Banco']
df_csv1 = df[colunas_desejadas]
df_csv1.rename(columns={'Funcionários': 'colaborador', 'Cargo': 'cargo', 'Dias trabalhados em abril': 'dias_trab', 'Salário família': 'salario_fami', 'Banco': 'banco'}, inplace=True)

# Renomeando profissões 
df_csv1.loc[:, 'cargo'] = df_csv1['cargo'].str.replace('Programadora júnior', 'Programador júnior')
df_csv1.loc[:, 'cargo'] = df_csv1['cargo'].str.replace('Programadora plena', 'Programador pleno')
df_csv1.loc[:, 'cargo'] = df_csv1['cargo'].str.replace('Programadora sênior', 'Programador sênior')

# Criando outra tabela Cargo/Salario para mesclar
colunas_desejadas_2 = ['Cargos', 'Salário']
df_csv2 = df[colunas_desejadas_2]
df_csv2.rename(columns={'Cargos': 'cargo', 'Salário': 'salario'}, inplace=True)

# Mesclagem
df_mesclado = pd.merge(df_csv1, df_csv2, on='cargo', how='left')
colunas_desajadas_final = ['colaborador', 'salario', 'dias_trab', 'salario_fami', 'banco']
df_final = df_mesclado[colunas_desajadas_final]
df_final.rename(columns={'salário': 'cargo_salario'}, inplace=True)
df_final.to_csv('planilha_final.csv', index=False)
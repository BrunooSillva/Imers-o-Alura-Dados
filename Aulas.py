import pandas as pd
import pycountry
import numpy as np
import matplotlib.pyplot  as plt
import seaborn as sns
import plotly.express as px

df = pd.read_csv("https://raw.githubusercontent.com/guilhermeonrails/data-jobs/refs/heads/main/salaries.csv")

df.head(20)

df.info()

df.describe()

df.shape

linhas, colunas = df.shape[0], df.shape[1]
print(linhas)
print(colunas)

df = df.rename(columns={
    'work_year': 'ano_trabalho',
    'experience_level': 'experiencia',
    'employment_type': 'emprego',
    'job_title': 'titulo_cargo',
    'salary': 'salario',
    'salary_currency': 'moeda_salario',
    'salary_in_usd': 'salario_em_usd',
    'employee_residence': 'residencia_empregado',
    'remote_ratio': 'remoto',
    'company_location': 'local_empresa',
    'company_size': 'tamanho'
})

df.columns


df["experiencia"].value_counts()

df["emprego"].value_counts()

df["remoto"].value_counts()

df["tamanho"].value_counts()

contrato = {
    "FT": "Tempo Integral",
    "PT": "Meio Periodo",
    "FL": "Freelance",
    "CT": "Contrato"
}

df['emprego'] = df['emprego'].replace(contrato)
df["emprego"].value_counts()

nivel_cargo = {
    "SE": "Senior",
    "MI": "Pleno",
    "EN": "Junior",
    "EX": "Executivo"
}

df['experiencia'] = df['experiencia'].replace(nivel_cargo)
df['experiencia'].value_counts()

tam_emp = {
    "M": "Media",
    "L": "Grande",
    "S": "Pequena",
}

df['tamanho'] = df['tamanho'].replace(tam_emp)
df['tamanho'].value_counts()

tipo_tra = {
    0: "Presencial",
    50: "Hibrido",
    100: "Remoto",
}

df['remoto'] = df['remoto'].replace(tipo_tra)
df['remoto'].value_counts()

df.head()

df.describe(include='object')

# Aula 2 - Limpeza e Manipulação de Dados


df.isnull() #verificar os dados

df.isnull().sum()

df['ano_trabalho'].unique()

df.columns

df[df.isnull().any(axis=1)] #verifica quais as linhas que estão em branco


#criação de uma tabela com dados nulos
df_salarios = pd.DataFrame({
    "Nome": ["Bruno", "Guilherme", "Carlos", "Fabiana", "Gab"],
    "Salario": [4000, np.nan, 3000, np.nan, 10000],
    })

#criação de uma nova coluna chamada salario_media
#round2 arredonda o numero para duas casas decimais
df_salarios["salario_media"] = df_salarios["Salario"].fillna(df_salarios["Salario"].mean().round(2))
df_salarios

#criando nova coluna de mediana entre os salários
df_salarios["salario_mediana"] = df_salarios["Salario"].fillna(df_salarios["Salario"].median())
df_salarios

df_temperaturas = pd.DataFrame({
    "Dia_Semana" : ["Segunda", "Terça", "Quarta", "Quinta", "Sexta"],
    "Temperatura": [30, np.nan, np.nan, 28, 27],
})

#criando nova coluna
#ffill serve para completar valores nulos com os valores anteriores aos nulos
df_temperaturas["preenchido_ffill"] = df_temperaturas["Temperatura"].ffill()
df_temperaturas

#bfill preenche os nulos com os valores posteriores
df_temperaturas["preenchido_bfill"] = df_temperaturas["Temperatura"].bfill()
df_temperaturas

df_cidades = pd.DataFrame({
    "Nome": ["Fernanda", "Laysa", "Bruno", "Gab", "Kay"],
    "Cidade": ["SP", np.nan, "RJ", np.nan, "PA"]
})

#fillna serve para preencher valores nulos com um dado especificado
df_cidades["Cidades_preenchidas"] = df_cidades["Cidade"].fillna("Não Informada")
df_cidades

df[df.isnull().any(axis=1)]

#criação do novo data frame sem os dados em branco
df_limpo = df.dropna()
df_limpo.isnull().sum()

df_limpo
df_limpo.info()

#alterando o tipo de dado do campo ano_trabalho, antes estava como float e agora está em int
df_limpo = df_limpo.assign(ano_trabalho = df_limpo['ano_trabalho'].astype('int64'))
df_limpo.info()

df_limpo.head()

# Aula 3 - Criar Gráficos

df_limpo.head()

df_limpo["experiencia"].value_counts().plot(kind="bar", title="distribuição cargos")



sns.barplot(data=df_limpo, x='experiencia', y='salario_em_usd') #criando gráfico

plt.figure(figsize=(8, 5)) #definindo o tamanho da figura
sns.barplot(data=df_limpo, x='experiencia', y='salario_em_usd') #criando gráfico
plt.title("Salário Médio por Serionidade")
plt.xlabel("Serionidade")
plt.ylabel("Média Salário Anual(USD)")
plt.show()

grafico_serionidade = df_limpo.groupby('experiencia')['salario_em_usd'].mean().sort_values(ascending=False).index
grafico_serionidade

plt.figure(figsize=(8, 5)) #definindo o tamanho da figura
sns.barplot(data=df_limpo, x='experiencia', y='salario_em_usd', order=grafico_serionidade) #criando gráfico
plt.title("Salário Médio por Serionidade")
plt.xlabel("Serionidade")
plt.ylabel("Média Salário Anual(USD)")
plt.show()

plt.figure(figsize=(10,5))
sns.histplot(df_limpo["salario_em_usd"], bins=50, kde=True)
plt.title("Distribuição Salarial")
plt.xlabel("Salário Anual(USD)")
plt.ylabel("Frequencia")
plt.show()

plt.figure(figsize=(8,5))
sns.boxplot(x=df_limpo["salario_em_usd"])
plt.title("distribuição salarial")
plt.xlabel("Salario")
plt.show()

ordem_serionidade = ["Junior", "Pleno", "Senior", "Executivo"]
plt.figure(figsize=(8,5))
sns.boxplot(x="experiencia", y="salario_em_usd", data=df_limpo, order = ordem_serionidade,)
plt.title("Distribuição Salarial por Serionidade")
plt.xlabel("Serionidade")
plt.show()

ordem_serionidade = ["Junior", "Pleno", "Senior", "Executivo"]
plt.figure(figsize=(8,5))
sns.boxplot(x="experiencia", y="salario_em_usd", data=df_limpo, order = ordem_serionidade, palette="Set2", hue="experiencia")
plt.title("Distribuição Salarial por Serionidade")
plt.xlabel("Serionidade")
plt.show()



df_media_salario_senioridade = df_limpo.groupby('experiencia')['salario_em_usd'].mean().reset_index().sort_values(by='salario_em_usd', ascending=False)

fig = px.bar(
    df_media_salario_senioridade,
    x='experiencia',
    y='salario_em_usd',
    title='Média Salarial por Nível de Experiência (Plotly)',
    labels={'experiencia': 'Nível de Experiência', 'salario_em_usd': 'Média Salarial Anual (USD)'},
    color='experiencia' # Add color based on experience level
)

fig.show()

remoto_contagem = df_limpo["remoto"].value_counts().reset_index()
remoto_contagem.columns = ["Tipo_trabalho", "quantidade"]

fig = px.pie(
    remoto_contagem,
    names="Tipo_trabalho",
    values="quantidade",
    title='Proporção dos tipos de trabalho',

)

fig.show()

remoto_contagem = df_limpo["remoto"].value_counts().reset_index()
remoto_contagem.columns = ["Tipo_trabalho", "quantidade"]

fig = px.pie(
    remoto_contagem,
    names="Tipo_trabalho",
    values="quantidade",
    title='Proporção dos tipos de trabalho',
    hole=0.5
)

fig.update_traces(textinfo='percent+label')
fig.show()

# Aula 4

df_limpo.head()


# Função para converter ISO-2 para ISO-3
def iso2_to_iso3(code):
    try:
        return pycountry.countries.get(alpha_2=code).alpha_3
    except:
        return None

# Criar nova coluna com código ISO-3
df_limpo['residencia_iso3'] = df_limpo['residencia_empregado'].apply(iso2_to_iso3)

# Calcular média salarial por país (ISO-3)
df_ds = df_limpo[df_limpo['titulo_cargo'] == 'Data Scientist']
media_ds_pais = df_ds.groupby('residencia_iso3')['salario_em_usd'].mean().reset_index()

# Gerar o mapa
fig = px.choropleth(media_ds_pais,
                    locations='residencia_iso3',
                    color='salario_em_usd',
                    color_continuous_scale='rdylgn',
                    title='Salário médio de Cientista de Dados por país',
                    labels={'salario_em_usd': 'Salário médio (USD)', 'residencia_iso3': 'País'})

fig.show()

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('.\covid_19_data.csv')

#verificando estrutura do dataset
print('-'*100)
print(df.head())
print('-'*100)
print(df.tail())
print('-'*100)
print(df.describe())
print('-'*100)
print(df.columns)
print('-'*100)
print(df.shape)
print('-'*100)
print(df.info)
###################################

#verificando valores nulos
print(df.isna().sum())
province_razao_nulos = (df.isna().sum()/len(df['ObservationDate'])) * 100
print('-'*100)
print('Proporção de valores nulos (na) no dataset \n')
print(province_razao_nulos)

#Tratamento de dados
df['Province/State'] = df['Province/State'].fillna('Unknow')
print(df.isna().sum())

#dropando variável SNO
df = df.drop('SNo', axis = 1)

df['Confirmed'][df['Confirmed'] < 0]
print(df[147524:147525])

print(df[:][(df['Country/Region'] == 'Colombia') & (df['ObservationDate'] == '11/01/2020')])
print(df[:][(df['Country/Region'] == 'Colombia') & (df['ObservationDate'] == '11/03/2020')])
print(df[:][(df['Country/Region'] == 'Colombia') & (df['ObservationDate'] == '11/02/2020')])

df = df.drop(147524)
df = df.drop(118363)
df = df.drop(141534)

index = df['Recovered'][df['Recovered'] < 0].index
df = df.drop(index)

#Estatísticas
brasil = df[df['Country/Region'] == 'Brazil']
mundo = df[df['Country/Region'] != 'Brazil']



fig = plt.figure()
spec = fig.add_gridspec(2, 2)
ax0 = fig.add_subplot(spec[0, :])
ax1 = fig.add_subplot(spec[1, 0])
ax2 = fig.add_subplot(spec[1, 1])

ax2.plot(mundo['Deaths'])
ax1.plot(brasil['Deaths'], color = 'r')
ax0.scatter(brasil['Deaths'][:], brasil['ObservationDate'][:], color='g')


sns.displot(
    data=brasil[:100],
    x='ObservationDate',
    y='Deaths'

)

plt.show()







import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
%matplotlib inline
sns.set()


df = pd.read_csv("DS_Property_Price.csv",sep=',') #carga del dataset junto con sus cinco primeras instancias
datapd = pd.DataFrame(df)
dataf = df.insert(2, "Count", 1, True)
datapd


datapd.shape


datapd.dtypes


datapd.count()


Missing = datapd.count() - 146660 #There are 146660 records
print(Missing)

print('There are 10 property types', 'and Instances')
pd.value_counts(datapd['property_type'])


plt.figure(figsize=(18,5))
plt.xlim(0,108000)
sns.countplot(data = datapd, y = "property_type", palette="coolwarm")



import matplotlib.pyplot as plt

# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = 'Departamento', 'Casa', 'PH', 'Lote', 'Oficina', 'Otro', 'Local comercial', 'Casa de campo', 'Deposito', 'Cochera'

sizes = [107326, 21521, 14298, 1312, 658, 374, 325, 322, 265, 259]
explode = (0,0,0,0.5, 0.7, 3, 4, 5, 7, 9) 

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', radius = 5, startangle=90, )
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()


#SHAPES

#ZONA: CAPITAL FEDERAL
dcaba = df[df.property_type.isin(['Departamento', 'Casa' , 'PH', 'Lote', 'Oficina', 'Otro','Local comercial', 'Casa de campo', 'Depósito', 'Cochera']) & df.l2.isin(['Capital Federal'])]
dcaba.shape

#ZONA: NORTE
dnorte = df[df.property_type.isin(['Departamento', 'Casa' , 'PH', 'Lote', 'Oficina', 'Otro','Local comercial', 'Casa de campo', 'Depósito', 'Cochera']) & df.l2.isin(['Bs.As. G.B.A. Zona Norte'])]
dnorte.shape

#ZONA: SUR
dsur = df[df.property_type.isin(['Departamento', 'Casa' , 'PH', 'Lote', 'Oficina', 'Otro','Local comercial', 'Casa de campo', 'Depósito', 'Cochera']) & df.l2.isin(['Bs.As. G.B.A. Zona Sur'])]
dsur.shape

#ZONA: OESTE
doeste = df[df.property_type.isin(['Departamento', 'Casa' , 'PH', 'Lote', 'Oficina', 'Otro','Local comercial', 'Casa de campo', 'Depósito', 'Cochera']) & df.l2.isin(['Bs.As. G.B.A. Zona Oeste'])]
doeste.shape


#ZONAS: ALL

plt.figure(figsize=(40,25))
plt.style.use('ggplot')
plt.subplot(3,1,1)
sns.countplot(data = datapd, y = 'l2', color='#069AF3')
plt.xlabel('inmuebles', fontsize = 40)
plt.xticks(fontsize = 40)
plt.ylabel('zona', fontsize = 50)
plt.yticks(rotation = -5, size = 25)
plt.title('Distribution of properties by zones',fontsize = 60, loc='center')
plt.grid()
plt.show()

#ZONA: CAPITAL FEDERAL
plt.figure(figsize=(200,80), dpi = 30)
plt.style.use('fast')
plt.subplot(2,2,1)
sns.countplot(data = dcaba, x = 'l3', color='#069AF3')
xlim=(0,100)
plt.ylabel('Inmuebles', fontsize = 80)
plt.yticks(fontsize = 50)
plt.xlabel('Localidad/Barrio', fontsize = 60)
plt.xticks(rotation = 90, fontsize = 60)
plt.title('Zona: Capital Federal',fontsize = 100, loc='right')
plt.grid()
plt.show() 

#ZONA: NORTE
plt.figure(figsize=(200,30), dpi = 30)
plt.style.use('fast')
plt.subplot(3,3,1)
sns.countplot(data = dnorte, x = 'l3', color='#069AF3')
xlim=(0,100)
plt.ylabel('Inmuebles', fontsize = 60)
plt.yticks(fontsize = 50)
plt.xlabel('Localidad/Barrio', fontsize = 50)
plt.xticks(rotation = 40, fontsize = 40)
plt.title('Zona: Norte',fontsize = 70, loc='right')
plt.grid()
plt.show() 

#ZONA: SUR
plt.figure(figsize=(200,30), dpi = 30)
plt.style.use('fast')
plt.subplot(3,3,2)
sns.countplot(data = dsur, x = 'l3', color='#069AF3')
xlim=(0,100)
plt.ylabel('Inmuebles', fontsize = 60)
plt.yticks(fontsize = 50)
plt.xlabel('Localidad/Barrio', fontsize = 50)
plt.xticks(rotation = 40, fontsize = 40)
plt.title('Zona: Sur',fontsize = 70, loc='right')
plt.grid()
plt.show() 

#ZONA: OESTE
plt.figure(figsize=(200,30), dpi = 30)
plt.style.use('fast')
plt.subplot(3,3,3)
sns.countplot(data = doeste, x = 'l3', color='#069AF3')
xlim=(0,100)
plt.ylabel('Inmuebles', fontsize = 60)
plt.yticks(fontsize = 50)
plt.xlabel('Localidad/Barrio', fontsize = 50)
plt.xticks(rotation = 40, fontsize = 40)
plt.title('Zona: Oeste',fontsize = 70, loc='right')
plt.grid()
plt.show() 

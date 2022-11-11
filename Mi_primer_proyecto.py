#!/usr/bin/env python
# coding: utf-8

# ## Mi primer proyecto
# Volvemos a encontrarnos con el conjunto de datos de pingüinos `PalmerPenguins`. Esta vez trabajaremos con ellos desde `Python`, para ello instalaremos el paquete que nos permitirá cargarlo:
# 

# In[2]:


get_ipython().system('pip install palmerpenguins')


# En segundo lugar, importaremos las librerías necesarias:

# In[49]:


import pandas as pd
from palmerpenguins import load_penguins


# Ahora ya estamos en posición de empezar a trabajar con los datos.
# 
# 1. Vamos a cargar el conjunto de datos. Muestra por pantalla el número de observaciones y sus características. Mira el tipo de datos de cada una de sus columnas.

# In[50]:


penguins = load_penguins()
penguins.shape


# In[51]:


penguins.info


# In[52]:


penguins.columns


# 2. Ya sabemos que este conjunto de datos tiene observaciones `NA`. Vamos a eliminarlas y a verificar que efectivamente no queda ninguno:

# In[53]:


penguins.isna()


# In[54]:


penguins = penguins.dropna()
print(penguins.columns[penguins.isna().any()])
print(penguins.isna().any)


# In[55]:


penguins.notna().sum()


# 3. ¿Cuántos individuos hay de cada sexo? Puedes obtener la longitud media del pico según el sexo:

# In[76]:


sexo = penguins.groupby('sex')
sexo.describe()


# In[78]:


conteo = penguins.groupby(['sex'])["sex"].count()
conteo # Hay 165 mujeres y 168 hombres.


# In[80]:


longpico_sex = penguins.groupby(['sex'])["bill_length_mm"].mean()
longpico_sex # Longitud media pico: mujeres 42 mm, hombres 45.85 mm


# 4. Vamos a añadir una columna, vamos a realizar una estimación (muy grosera) del área del pico de los pingüinos (bill) tal como si esta fuese un rectángulo. Esta nueva columnas se llama `bill_area` y debe encontrarse en la última posición. Verifica que es correcto.

# In[46]:


penguins['bill_area'] = penguins["bill_length_mm"]*penguins["bill_depth_mm"]


# 5. Hagamos algo un poco más elaborado, vamos a realizar una agrupación en función del sexo y de la especie de cada observación. Queremos obtener solamente la información referente al sexo Femenino.

# In[115]:


gr_sex_species = penguins.groupby(['sex'])['species']
f_species = penguins.loc[gr_sex_species.groups['female'].values]
f_species.sex.describe()


# 6. Como ya sabemos, la variable peso, se encuentra en gramos, la pasaremos a kg. Para ello crearemos una nueva columna llamada `body_mass_kg` y eliminaremos `body_mass_g`.

# In[108]:


body_mass_kg = penguins['body_mass_g']/1000


# In[111]:


penguins_add = penguins.assign(body_mass_kg = penguins['body_mass_g']/1000)
print(penguins_add)


# In[112]:


final_penguins = penguins_add.drop(['body_mass_g'], axis=1)
print(final_penguins)


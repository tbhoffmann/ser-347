#!/usr/bin/env python
# coding: utf-8

# In[6]:

#Tania Beatriz - exercicio 01

#séries

import numpy as np

s1 = np.array ((168, 398, 451, 337, 186, 232, 262, 349, 189, 204, 220, 220, 207, 239, 259, 258, 242, 331, 251, 323, 106, 1055, 170))

s2 = np.array ((168, 400, 451, 300, 186, 200, 262, 349, 189, 204, 220, 220, 207, 239, 259, 258, 242, 331, 251, 180, 106, 1055, 200))

#calcular a euclidiana entre as séries

deuclid = np.linalg.norm(s1 - s2)
print("A distância euclidiana é igual a", deuclid)


# In[11]:


#calcular a série temporal com os valores médios 

med = np.mean(np.array([s1,s2]), axis=0)

print('A série temporal com os valores médios é igual a' , med)


# In[14]:


#calcular a série temporal com os valores máximos de cada instante entre s1 e s2

#criando uma nova série

smax = []

for i in range (0, len (s1)):
    s3 = np.array ([s1[i], s2[i]])
    x = np.max(s3)
    smax.append(x)
    
print('A série temporal com os valores máximos é:',smax)


# In[17]:


#calcular a série temporal com os valores minímos de cada instante entre s1 e s2

#criando uma nova série

smin = []

for i in range (0, len (s1)):
    s3 = np.array ([s1[i], s2[i]])
    y = np.min(s3)
    smin.append(y)
    
print('A série temporal com os valores mínimos é:', smin)


# In[ ]:





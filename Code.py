#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
data = pd.read_excel("D:\\sample_input.xlsx",index_col=0)
df = pd.DataFrame(data)
df1 = pd.DataFrame(df.groupby("Name")["Age"].apply(list))
df1['Net_Bal'] = df.groupby('Name')['Balance'].sum() - df.groupby('Name')['Credit'].sum()
df1.to_excel('D:\Output.xlsx')


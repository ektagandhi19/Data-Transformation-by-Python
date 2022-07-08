#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
data = pd.read_excel("D:\\sample_input.xlsx",index_col=0)
df = pd.DataFrame(data)
Name = pd.DataFrame(list(df['Name'].drop_duplicates()))
Andrew_age = df.loc[df['Name'] == 'Andrew', 'Age']
James_age = df.loc[df['Name'] == 'James', 'Age']
Kylie_age = df.loc[df['Name'] == 'Kylie', 'Age']
Age = [list(Andrew_age), list(James_age), list(Kylie_age)]
balance = [df.loc[df['Name'] == 'Andrew', 'Balance'].sum(), df.loc[df['Name'] == 'James', 'Balance'].sum(), df.loc[df['Name'] == 'Kylie', 'Balance'].sum()]
credit = [df.loc[df['Name'] == 'Andrew', 'Credit'].sum(), df.loc[df['Name'] == 'James', 'Credit'].sum(), df.loc[df['Name'] == 'Kylie', 'Credit'].sum()]
Net_bal = pd.DataFrame(balance)-pd.DataFrame(credit)
df1=pd.DataFrame()
df1['Name']=Name
df1['Age']=Age
df1['Net (Balance-Credit)']=Net_bal
df1.to_excel('D:\Output.xlsx')


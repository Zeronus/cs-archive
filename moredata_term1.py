# Pandas Demo

import matplotlib.pyplot as plt
import pandas as pd

def read_one_year(yr):
    path = 'D:\\names\\'
    filename = 'yob{}.txt'.format(yr)
    f = pd.read_csv(path+filename,header=None,names=['name','gender','count'])
    f['year'] = int(yr)
    return f

start_year,finish_year = 1880,2016
all_years = pd.concat([read_one_year(y) for y in range(start_year,finish_year+1)])

m_counts = all_years[all_years['gender'] == 'M'].groupby(by='year').sum()
f_counts = all_years[all_years['gender'] == 'F'].groupby(by='year').sum()
years = m_counts.index.tolist()
plt.plot(years,f_counts,years,m_counts)
plt.legend(['Female','Male'])
def trendy(name):
    counts = all_years[all_years['name']==name]
    counts.groupby(by='year').sum().plot.line()
    
trendy('Kobe')
print(m_counts.head())
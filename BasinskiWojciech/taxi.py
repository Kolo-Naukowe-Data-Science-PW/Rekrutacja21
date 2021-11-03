# -*- coding: utf-8 -*-

# -- Sheet --

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline
import seaborn as sns
from scipy import stats


df = pd.read_csv('green_tripdata_2021-01.csv')
df.describe(include='all')

def reject_outliers(data, m=2):
    return data[abs(data - np.mean(data)) < m * np.std(data)] 

dff=reject_outliers(df)

sns.heatmap(df[['passenger_count','trip_distance','fare_amount','extra','mta_tax','tip_amount','ehail_fee','payment_type','total_amount','improvement_surcharge','payment_type','trip_type','congestion_surcharge']].corr(), annot=True, cmap = 'Reds')

plt.show().set_size_inches(18.5, 10.5)

df['payment_type'].value_counts(normalize=True)

#plot the pie chart of education categories
dff['payment_type'].value_counts(normalize=True).plot.pie()

plt.title('Payment type')
plt.legend()

plt.show()

counts=df['payment_type'].value_counts() #counts the elements
percent = df['payment_type'].value_counts(normalize=True) #gives percentage as a fraction
percent100 = df['payment_type'].value_counts(normalize=True).mul(100).round(1).astype(str) + '%' #gives percentage as %
pd.DataFrame({'counts': counts, 'per': percent, 'per%': percent100})

dfFilteredAmount = [x for x in dff['total_amount'] if (x >0)]


sns.displot(dfFilteredAmount)
plt.title('Total amount paid during a service')
plt.xlabel('Total amount paid')
plt.ylabel('Number of transactions')





g=sns.relplot(x=abs(dff['total_amount']), y=abs(dff['tip_amount']))
g.fig.set_size_inches(10,10)

plt.title('Total amount paid vs amount of the tip')

plt.xlabel('Total amount paid')
plt.ylabel('Amount of tip paid by client')
plt.show()

def reject_outliers(data, m=2):
    return data[abs(data - np.mean(data)) < m * np.std(data)] 

dat=reject_outliers(dff['trip_distance'])
sns.relplot(x=abs(dff['total_amount']), y=dat, data=dff)
plt.title('Total distance vs total amount paid')

plt.ylabel('Total amount paid')
plt.xlabel('The total distance of the path')
plt.show()




sns.catplot(x="passenger_count", y=df['tip_amount'],
            kind="bar",  data=df)

plt.xlabel('The number of passengers')
plt.ylabel('Amount of tip paid by client')
plt.show()



sns.catplot(x=abs(dff['extra']), y=abs(dff['tip_amount']),
            kind="bar",  data=dff)

plt.xlabel('The number of passengers')
plt.ylabel('Amount of tip paid by client')
plt.show()

#outliers

sns.catplot(x=abs(dff["mta_tax"]), y=np.abs(dff["total_amount"]),
            kind="box",  data=df,showfliers = False).set(title='Title of Plot')

#outliers
g=sns.catplot(x="payment_type", y="total_amount", 
            kind="box",  data=dff,showfliers = False)

g.fig.set_size_inches(12,12)




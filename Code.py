

import pandas as pd
import seaborn as sns

df6 = sns.load_dataset('tips')

df6.head(3)

gp = df6.groupby('time').agg({"tip":"mean"})
sns.heatmap(gp)
plt.show()

sns.countplot(data = df6, x = 'time',hue ='sex')
plt.show()

sns.violinplot(data = df6, y='tip')
plt.show()

sns.pairplot(data = df6, hue = 'sex')
plt.show()

import seaborn as sns
abc = sns.load_dataset('tips')

abc.head(3)

import matplotlib.pyplot as plt

sns.stripplot(data = abc, x = 'day', y = 'total_bill', hue = 'sex', dodge = True, jitter = 0.1)
plt.show()

sns.boxplot(data = abc, x = 'sex',y = 'tip',orient = 'vertical', hue ='size')
plt.show()

sns.catplot(data = abc, x = 'day')
plt.show()

df3 = sns.load_dataset('exercise')

df3.head()

sns.palplot(sns.color_palette('spring'))

sns.set_style(style ='ticks')
sns.set_style(style ='whitegrid')
sns.barplot(data = df3, x= 'time',y= 'pulse')
plt.show()

#sns.FacetGrid(abc,col ='day',height = 2)
a = sns.FacetGrid(abc,col = 'time',height = 2, hue = 'sex')
a.map(sns.barplot,'day','tip')
plt.show()

sns.relplot(data = abc, x='tip',y = 'total_bill', hue = 'sex',col ='day',size ='smoker')
plt.show()

sns.swarmplot(data = abc, x = 'day', y= 'total_bill',hue = 'sex',dodge = True)
plt.show()

sns.kdeplot(data = abc, x = 'total_bill',hue='day', multiple = 'fill')
plt.show()

df6.to_csv('tips.csv')

from google.colab import files

# Download the CSV file
files.download('tips.csv')
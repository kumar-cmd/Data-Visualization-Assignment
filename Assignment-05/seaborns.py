# -*- coding: utf-8 -*-
"""Data Visualization assg-05.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/12pnLXrwmi7FhmztY0q3pf2wkPx5cOFvE
"""

import numpy as np
import pandas as pd

r = pd.read_csv('auto-mpg.csv')
r['horsepower'] = r['horsepower'].map(lambda x : 88 if x =='?' else int(x))

r[['mpg','cylinders','horsepower','weight','model year']].to_json(orient="records")

r.info()

r.describe()

m = r['mpg'].unique()
print(m.min(),m.max(),m.size)
c = r['cylinders'].unique()
print(c.min(),c.max(),c.size)
w = r['weight'].unique()
print(w.min(),w.max(),w.size)
h = r['horsepower'].unique()
print(h.min(),h.max(),h.size)
y = r['model year'].unique()
print(y.min(),y.max(),y.size)



print(r['mpg'].to_list())

print(r['model year'].to_list())

viz = pd.DataFrame({'x':r['model year'],'y':r['mpg']})

viz.to_json(orient="records")

radius =r['weight'].map(lambda x : (x/800)*5)
print(radius.round(1).to_list())

colordict = {3:'#86fb4b' , 4:'#fb8503',5:'#02ffff', 6:'#ff00ff', 8:'#6a3dff'}
color =r['cylinders'].map(lambda x : colordict[x])
print(color.to_list())

import seaborn as sns
import matplotlib.pyplot as plt
sns.set_theme()
sns.set(rc={'figure.figsize':(10,8)})

# Define data
# x = [1, 2, 3, 4, 5]
# y = [10, 20, 30, 40, 50]
# size = [100, 200, 300, 400, 500]
# color = ['r', 'g', 'b', 'm', 'y']

# Create scatter plot
sns.scatterplot(x=r['model year'], y=r['mpg'], s=radius*20, hue=color,  linewidth=1, palette="deep")

# Add labels and title
plt.xlabel('Model Year')
plt.ylabel('Miles Per Gallon')
plt.title('MPG, Cylinder, HorsePower, Weight, Model Year')

# Show plot
plt.show()

vegalite = pd.DataFrame({"x": r['model year'], "y": r['mpg'], "size": radius*2, "color": color})

print(vegalite.to_json(orient="records"))
# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd 
import seaborn as sns 
import matplotlib.pyplot as plt 
import warnings 
warnings.filterwarnings("ignore")

stroke_data = pd.read_csv("C:/Users/kmiller018/Documents/MSDS670/strokedata.csv")
stroke_data.head(10)

stroke_data.shape # 5110 rows and 12 columns

sns.color_palette("rocket")

# Count of Patients that had a stroke and those that did not have a stroke
sns.set(rc={'figure.figsize':(18,10)})
seaborn_plot = sns.countplot(stroke_data['stroke'])
seaborn_plot.set_xlabel("Stroke",fontsize=20)
seaborn_plot.set_ylabel("Count of Patient",fontsize=20)
seaborn_plot.set_title("Stroke Count", fontsize=26)

#comparison of heart disease and strokes
print(stroke_data['heart_disease'].value_counts())
sns.set(rc={'figure.figsize':(18,10)})
seaborn_plot = sns.countplot(stroke_data['heart_disease'], hue = stroke_data['stroke'])
seaborn_plot.set_xlabel("heart_disease",fontsize=20)
seaborn_plot.set_ylabel("Count of Patient",fontsize=20)
seaborn_plot.set_title("Heart Disease and Strokes", fontsize=26)

#comparison of work type and stroke
print(stroke_data['work_type'].value_counts())
sns.countplot(stroke_data['work_type'], hue = stroke_data['stroke'])
seaborn_plot.set_title("Workt Type and Strokes", fontsize=26)

#Correlation heat map of age, hypertension and bmi
fig, ax = plt.subplots(figsize=(7, 7))
heatmap = sns.heatmap(stroke_data[['age', 'hypertension', 'bmi']].corr(), vmax=1, annot=True,ax = ax)
heatmap.set_title('Correlation Heatmap')

#Scatterplot of age and bmi
sns.set_style("darkgrid")
sns.FacetGrid(stroke_data, hue="stroke", height=5).map(plt.scatter, "age", "bmi").add_legend()
plt.title('Age vs BMI')
plt.show()





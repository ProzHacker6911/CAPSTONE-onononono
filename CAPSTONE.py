import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
print(sns.get_dataset_names())
df=sns.load_dataset("penguins")
print(df.head(10))
print(df.shape)
print(df.isnull().sum())
print(df.describe())
print(df.dtypes)
print(df.info())
#print(df.corr())
#sns.heatmap(df.corr(),cmap="wistia",annot=True)
df.hist(figsize=(12,8))
df.plot(kind="box")
print(df.island.value_counts())
print(df.species.value_counts())
sns.countplot(data=df,x="island",palette="summer")
plt.show()
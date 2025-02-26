import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Tải dữ liệu
df = pd.read_csv("Churn_Modelling.csv")

# Xem thông tin cơ bản của dữ liệu
print(df.info())

# Xem 5 dòng đầu tiên
print(df.head())

# Xóa các cột không cần thiết
df.drop(['RowNumber', 'CustomerId', 'Surname'], axis=1, inplace=True)

# Chuyển đổi dữ liệu category sang số
df['Gender'] = df['Gender'].map({'Male': 1, 'Female': 0})
df = pd.get_dummies(df, columns=['Geography'], drop_first=True)

sns.boxplot(x='Exited', y='CreditScore', data=df)
plt.title('CreditScore vs Exited')
plt.show()

print(df.groupby('Exited')['CreditScore'].mean())

sns.histplot(x='Age', hue='Exited', data=df, kde=True)
plt.title('Age vs Exited')
plt.show()

print(df.groupby('Exited')['Age'].mean())

sns.boxplot(x='Exited', y='Balance', data=df)
plt.title('Balance vs Exited')
plt.show()

print(df.groupby('Exited')['Balance'].mean())

sns.histplot(x='EstimatedSalary', hue='Exited', data=df, kde=True)
plt.title('EstimatedSalary vs Exited')
plt.show()

print(df.groupby('Exited')['EstimatedSalary'].mean())
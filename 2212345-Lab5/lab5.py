import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Tải dữ liệu từ Kaggle (hoặc tải thủ công)
url = "https://raw.githubusercontent.com/datasets/bank-customer-churn/master/Churn_Modelling.csv"
df = pd.read_csv(url)
# Hiển thị 5 dòng đầu tiên
print(df.head())
# Loại bỏ 3 cột 
df.drop(["RowNumber", "CustomerId", "Surname"], axis=1, inplace=True)

# Xem các nhóm dữ liệu trong cột 'Card Type'
print(df["Card Type"].unique())

# Phân loại cột liên tục và phân loại
categorical_columns = ["Geography", "Gender", "NumOfProducts", "HasCrCard", "IsActiveMember", "Exited", "Complain", "Card Type"]
continuous_columns = ["CreditScore", "Age", "Tenure", "Balance", "EstimatedSalary"]
print("Cột dữ liệu phân loại:", categorical_columns)
print("Cột dữ liệu liên tục:", continuous_columns)

#Biểu đồ Pie về khách hàng rời đi
df["Exited"].value_counts().plot.pie(autopct="%1.1f%%", colors=["lightblue", "salmon"])
plt.title("Tỷ lệ khách hàng rời đi")
plt.ylabel("")
plt.show()

#Biểu đồ Pie phân bố nam nữ
df["Gender"].value_counts().plot.pie(autopct="%1.1f%%", colors=["pink", "lightblue"])
plt.title("Tỷ lệ phân bố nam nữ")
plt.ylabel("")
plt.show()

#Biểu đồ Pie phân bố địa lý
df["Geography"].value_counts().plot.pie(autopct="%1.1f%%", colors=["gold", "skyblue", "lightgreen"])
plt.title("Tỷ lệ khách hàng theo quốc gia")
plt.ylabel("")
plt.show()

#Tỷ lệ khách hàng có thẻ tín dụng (CreditCard)
credit_card_count = df["HasCrCard"].value_counts(normalize=True) * 100
print(credit_card_count)

#Histogram cho CreditScore, Balance, Age, Salary
columns = ["CreditScore", "Balance", "Age", "EstimatedSalary"]
for col in columns:
    plt.figure(figsize=(6,4))
    sns.histplot(df[col], bins=30, kde=True)
    plt.title(f"Phân bố {col}")
    plt.show()


#Biểu đồ countplot - Mối quan hệ Exited và các biến phân loại
plt.figure(figsize=(12,6))
sns.countplot(data=df, x="Geography", hue="Exited")
plt.title("Xu hướng rời đi theo quốc gia")
plt.show()
# Quốc gia nào có xu hướng khách hàng rời đi nhiều nhất?
plt.figure(figsize=(6,4))
sns.countplot(data=df, x="Gender", hue="Exited")
plt.title("Xu hướng rời đi theo giới tính")
plt.show()
#Nam hay nữ có xu hướng rời đi cao hơn?
plt.figure(figsize=(6,4))
sns.countplot(data=df, x="NumOfProducts", hue="Exited")
plt.title("Xu hướng rời đi theo số sản phẩm")
plt.show()

#Biểu đồ Boxplot
#CreditScore có ảnh hưởng đến việc rời đi không?
plt.figure(figsize=(6,4))
sns.boxplot(data=df, x="Exited", y="CreditScore")
plt.title("Mối quan hệ giữa CreditScore và Exited")
plt.show()
# Độ tuổi nào có xu hướng rời đi cao?
plt.figure(figsize=(6,4))
sns.boxplot(data=df, x="Exited", y="Age")
plt.title("Mối quan hệ giữa Age và Exited")
plt.show()
#Quốc gia nào có số dư cao nhất?
plt.figure(figsize=(6,4))
sns.boxplot(data=df, x="Geography", y="Balance")
plt.title("Mối quan hệ giữa Geography và Balance")
plt.show()

#Xu hướng khách hàng có số dư cao rời bỏ ngân hàng?
plt.figure(figsize=(8,6))
sns.boxplot(data=df, x="Geography", y="Balance", hue="Exited")
plt.title("Xu hướng khách hàng có Balance cao rời bỏ ngân hàng theo quốc gia")
plt.show()


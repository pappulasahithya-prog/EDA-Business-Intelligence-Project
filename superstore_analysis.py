import pandas as pd

df = pd.read_csv(r"C:\Users\sahit\Downloads\Online Retail Data Set.csv")

print(df.head())
print(df.info())
print(df.describe())
print(df.isnull().sum())
print(df.columns)
import matplotlib.pyplot as plt

df['Country'].value_counts().head(10).plot(kind='bar')
plt.title("Top 10 Countries")
plt.show()
import matplotlib.pyplot as plt

plt.hist(df['Quantity'], bins=20)
plt.title("Quantity Distribution")
plt.xlabel("Quantity")
plt.ylabel("Frequency")
plt.show()
top_products = df['Description'].value_counts().head(10)

top_products.plot(kind='bar')

plt.title("Top 10 Products")
plt.show()
df['Revenue'] = df['Quantity'] * df['UnitPrice']

top_countries_revenue = df.groupby('Country')['Revenue'].sum().sort_values(ascending=False).head(10)

top_countries_revenue.plot(kind='bar')

plt.title("Top 10 Countries by Revenue")
plt.xlabel("Country")
plt.ylabel("Revenue")
plt.show()
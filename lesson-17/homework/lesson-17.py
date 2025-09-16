# homework-1

import pandas as pd
import numpy as np

# 1
df.rename(columns={'First Name': 'first_name', 'Age': 'age'}, inplace=True)
# 2
print(df.head(3))
# 3
mean_age = df['age'].mean()
# 4
print(df[['first_name', 'City']])
# 5
df['Salary'] = np.random.randint(50000, 100000, size=len(df))
# 6
print(df.describe(include='all'))

# Homework--2

 # 1
data = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr'],
    'Sales': [5000, 6000, 7500, 8000],
    'Expenses': [3000, 3500, 4000, 4500]
}
sales_and_expenses = pd.DataFrame(data)

# 2
max_sales = sales_and_expenses['Sales'].max()
max_expenses = sales_and_expenses['Expenses'].max()
# 3
min_sales = sales_and_expenses['Sales'].min()
min_expenses = sales_and_expenses['Expenses'].min()
# 4
avg_sales = sales_and_expenses['Sales'].mean()
avg_expenses = sales_and_expenses['Expenses'].mean()


# Homework-3

import pandas as pd
# 1. DataFrame yaratish
data = {
    'Category': ['Rent', 'Utilities', 'Groceries', 'Entertainment'],
    'January': [1200, 200, 300, 150],
    'February': [1300, 220, 320, 160],
    'March': [1400, 240, 330, 170],
    'April': [1500, 250, 350, 180]
}


expenses = pd.DataFrame(data)

# 2

expenses = expenses.set_index('Category')

# 3
max_expenses = expenses.max(axis=1)
# 4
min_expenses = expenses.min(axis=1)
# 5
avg_expenses = expenses.mean(axis=1)

import pandas as pd

data_list_of_dicts = [{'Name': 'Alice', 'Age': 25, 'City': 'New York'},
                        {'Name': 'Bob', 'Age': 30, 'City': 'San Francisco'},
                        {'Name': 'Charlie', 'Age': 35, 'City': 'Los Angeles'}]
df1 = pd.DataFrame(data_list_of_dicts)

df = pd.read_csv('iris.csv')
# print(df)

#get a singular colum 
specificColumn = df['petal_length']
print(specificColumn)

specificType = df1.select_dtypes(include='object')
print(specificType)
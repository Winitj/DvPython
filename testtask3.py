import pandas as pd


file_path = 'test1.xlsx'  
df = pd.read_excel(file_path)

filtered_data = df[(df['Salary'] >= 30000) & (df['Salary'] <= 75000) & (df['Experience(In Year)'] > 5)]


result_json = filtered_data[['Name', 'City']].set_index('Name').to_dict()['City']

print(result_json)

import pandas as pd
import json

# Load the Excel file
excel_file = 'Tesco_Health_Score_P12_CZ.xlsx'
df = pd.read_excel(excel_file)

# Convert the DataFrame to a JSON file
json_data = df.to_json(orient='records')

# Save the JSON data to a file
with open('products.json', 'w') as f:
    f.write(json_data)

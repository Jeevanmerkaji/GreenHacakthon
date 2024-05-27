import pandas as pd
import qrcode

# Load the Excel file
excel_file = 'Tesco_Health_Score_P12_CZ.xlsx'
df = pd.read_excel(excel_file)

# Base URL of your GitHub Pages site
base_url = 'https://yourusername.github.io/products/'

# Generate QR codes
for index, row in df.iterrows():
    product_code = row['product_code']
    url = f'{base_url}{product_code}.html'
    qr = qrcode.make(url)
    qr.save(f'qr_codes/{product_code}.png')

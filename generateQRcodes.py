import pandas as pd
import qrcode
import os

# Load the Excel file
excel_file = 'Tesco_Health_Score_P12_CZ.xlsx'
df = pd.read_excel(excel_file)

# Base URL of your GitHub Pages site
base_url = 'https://jeevanmerkaji.github.io/GreenHacakthon/'

folder = f'qr_codes/'

os.makedirs(folder, exist_ok=True)


# Generate QR codes
for index, row in df.iterrows():
    product_code = row['Slad Tpnb']
    url = f'{base_url}{product_code}.html'
    qr = qrcode.make(url)
    qr.save(f'{folder}/{product_code}.png')
    if index == 10:
        break

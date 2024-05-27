import pandas as pd
import os

# Load the Excel file
excel_file = 'Tesco_Health_Score_P12_CZ.xlsx'
df = pd.read_excel(excel_file)

# # Template for the product detail page
# template = """
# <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <meta name="viewport" content="width=device-width, initial-scale=1.0">
#     <title>Product Details</title>
#     <link rel="stylesheet" href="../styles.css">
# </head>
# <body>
#     <div class="product-detail">
#         <h1>{product_name}</h1>
#         <p>Type: {product_type}</p>
#         <p>Health: {product_health_label}</p>
#         <a href="../index.html">Back to list</a>
#     </div>
# </body>
# </html>
# """
def get_nutritional_facts(df):
    nutri_value = pd.DataFrame()
    nutri_value = df[['Description ENG','Energy','Fibre','Protein','Salt','Saturates','Sugars']]
    return nutri_value
# Folder to save the nutritional facts pages
nutri_folder = 'nutritional_facts/'
os.makedirs(nutri_folder, exist_ok=True)

nutritional_facts_template_base = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Nutritional Facts - {product_name}</title>
    <style>
        .container {
            max-width: 600px;
            margin: auto;
            background-color: #ffffff;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }

        h1 {
            text-align: center;
            color: #333333;
        }

        table {
            border-collapse: collapse;
            width: 100%;
            margin-top: 20px;
        }

        th, td {
            border: 1px solid #dddddd;
            text-align: left;
            padding: 8px;
        }

        th {
            background-color: #f2f2f2;
        }

        a {
            display: block;
            text-align: center;
            margin-top: 20px;
            text-decoration: none;
            color: #1a73e8;
        }

        body {
            font-family: Arial, sans-serif;
            background-color: #f0f0f0;
            margin: 0;
            padding: 20px;
        }

    </style>
</head>
"""
nutritional_facts_template_variable = """
<body>
    <div class="container">
        <h1>Nutritional Facts for {product_name}</h1>
        <table>
            <tr>
                <th>Nutrient</th>
                <th>Value</th>
            </tr>
            <tr>
                <td>Energy</td>
                <td>{energy}</td>
            </tr>
            <tr>
                <td>Fibre</td>
                <td>{fibre}</td>
            </tr>
            <tr>
                <td>Protein</td>
                <td>{protien}</td>
            </tr>
            <tr>
                <td>Salt</td>
                <td>{salt}</td>
            </tr>
            <tr>
                <td>Saturates</td>
                <td>{saturates}</td>
            </tr>
            <tr>
                <td>Sugars</td>
                <td>{sugar}</td>
            </tr>
        </table>
        <a href=f'{folder}/{product_code}.html'>Back to Home</a>
    </div>
</body>
</html>
"""

base_template1 = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Product Information & Health Score Bar</title>
    <style>
        /* CSS styles for product information */
        .container-product {
            max-width: 600px;
            margin: 20px auto;
            background-color: #ffffff;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }

        .logo {
            text-align: center;
            margin-bottom: 20px;
        }

        .logo img {
            max-width: 200px;
            height: auto;
        }

        h1 {
            color: #333333;
            text-align: center;
        }

        .product {
            margin-bottom: 20px;
        }

        .product-name {
            font-size: 24px;
            font-weight: bold;
            color: #1a73e8;
            margin-bottom: 10px;
        }

        .property {
            font-size: 18px;
            color: #666666;
            margin-bottom: 5px;
        }

        .property-name {
            font-weight: bold;
        }

        /* CSS styles for health score bar */
        body {
            font-family: Arial, sans-serif;
            display: flex;
            flex-direction: column;
            align-items: center;
            background-color: #f0f0f0;
            margin: 0;
            padding: 20px;
        }

        .container-health {
            text-align: center;
            margin-top: 50px;
        }

        .health-bar {
            position: relative;
            width: 300px;
            height: 30px;
            background: linear-gradient(to right, red, yellow, green);
            border-radius: 15px;
            margin: 20px auto;
        }

        .needle {
            position: absolute;
            top: -10px;
            left: 75%; /* Position the needle according to the health score */
            width: 2px;
            height: 50px;
            background-color: black;
        }

        .score {
            font-size: 1.5em;
            font-weight: bold;
        }
    </style>
</head>
<body>
<!-- Product Information Section -->
<div class="container-product">
    <div class="logo">
        <img src="tesco.jpeg" alt="Logo">
    </div>
"""

variable_template1 = """
    <h1>Product Information</h1>

    <div class="product">
        <div class="product-name">{product_name}</div>
        <div class="property">
            <span class="property-name">Product type:</span> {product_type}
        </div>
        <div class="property">
            <span class="property-name">Health label:</span> {product_health_label}
        </div>
          <div class="property">
            <span class="property-name">TESCO Product:</span> {tesco_label}
        </div>

        <!-- Button and link for nutritional facts -->
        <div class="nutritional-facts">
            <button onclick="window.location.href= f'{nutri_folder}/{product_code}_facts.html'">Nutritional Facts</button>
        </div>
    </div>
</div>
"""

base_template2 = """
<!-- Health Score Bar Section -->
<div class="container-health">
    <h1>Health Score Bar</h1>

    <div class="health-bar">
        <div class="needle" id="needle"></div>
    </div>
    <div class="score" id="score">75</div>
</div>

<script>
    // Function to update the health score
    function updateHealthScore(score) {
        const needle = document.getElementById('needle');
        const scoreDisplay = document.getElementById('score');
        needle.style.left = score + '%';
        scoreDisplay.textContent = score;
    }
"""

variable_template2 = """
    // Example: Updating the health score
    const healthScore = {health_score}; // Change this value to update the score
    updateHealthScore(healthScore);
</script>

</body>
</html>
"""


folder = f'products/'
os.makedirs(folder, exist_ok=True)
# Generate individual product pages
for index, row in df.iterrows():
    product_code = row['Slad Tpnb']
    variable_template_updated = variable_template1.format(
        nutri_folder = nutri_folder,
        product_code = row['Slad Tpnb'],
        product_name=row['Description ENG'],
        product_type=row['Section'].split()[1],
        product_health_label=row['Healthy Flag'],
        tesco_label = ("Yes" if (row['Own Brand'] == 'Y') else "No")
    )
    variable_template_updated2 = variable_template2.format(
        health_score=row['Health Score']
    )

    nutritional_facts_template_updated = nutritional_facts_template_variable.format(
         folder  = folder,
          product_code = row['Slad Tpnb'],
         product_name=row['Description ENG'],
         energy = row['Energy'],
         fibre = row['Fibre'],
         salt = row['Salt'],
         saturates = row['Saturates'],
         sugar = row['Sugars'],
         protien = row['Protein']
)
    # Save HTML content to file
    with open(f'{nutri_folder}/{product_code}_facts.html', 'w') as f:
        f.write(nutritional_facts_template_base)
        f.write(nutritional_facts_template_updated)
        if index ==10:
            break
    with open(f'{folder}/{product_code}.html', 'w') as f:
        f.write(base_template1)
        f.write(variable_template_updated)
        f.write(base_template2)
        f.write(variable_template_updated2)
        if index == 10:
            break

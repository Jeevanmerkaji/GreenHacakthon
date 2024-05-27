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
        product_name=row['Description ENG'],
        product_type=row['Section'].split()[1],
        product_health_label=row['Healthy Flag'],
        tesco_label = ("Yes" if (row['Own Brand'] == 'Y') else "No")
    )
    variable_template_updated2 = variable_template2.format(
        health_score=row['Health Score'],
    )

    with open(f'{folder}/{product_code}.html', 'w') as f:
        f.write(base_template1)
        f.write(variable_template_updated)
        f.write(base_template2)
        f.write(variable_template_updated2)
        if index == 10:
            break

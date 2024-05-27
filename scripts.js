fetch('products.json')
    .then(response => response.json())
    .then(data => {
        const productList = document.getElementById('product-list');
        data.forEach(product => {
            const productDiv = document.createElement('div');
            productDiv.className = 'product';
            productDiv.innerHTML = `
                <h2>${product.product_name}</h2>
                <p>Type: ${product.product_type}</p>
                <p>Health: ${product.product_health_label}</p>
                <img src="qr_codes/${product.product_code}.png" alt="QR Code">
            `;
            productList.appendChild(productDiv);
        });
    });

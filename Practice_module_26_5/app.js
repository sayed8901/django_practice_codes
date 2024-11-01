const loadAllProducts = () => {
  fetch("https://fakestoreapi.com/products")
    .then((res) => res.json())
    .then((data) => displayAllProducts(data));
};

const displayAllProducts = (products) => {
  // console.log(products);

  products.forEach((product) => {
    // console.log(product);

    const parent = document.getElementById("products-container");
    const div = document.createElement("div");
    div.classList.add("product-card");

    div.innerHTML = `
            <div class="card shadow h-100">
                <div>
                  <img
                    src="${product.image}"
                    class="card-img-top"
                    loading="lazy"
                    alt="card image"
                  />
                </div>
                <div class="card-body p-3 p-xl-5">
                  <h3 class="card-title h5">${product.title}</h3>
                  <h4 class="card-title h5">Category: ${product.category}</h4>
                  <p class="card-text">
                    ${product.description.slice(0, 100)}
                  </p>
                  <a target="_blank" href="product_details.html?productId=${
                    product.id
                  }" class="btn btn-primary">View Details</a>
                </div>
            </div>
        `;

    parent.appendChild(div);
  });
};

loadAllProducts();

const getParems = () => {
  const param = new URLSearchParams(window.location.search).get("productId");
  //   console.log(param);

  fetch(`https://fakestoreapi.com/products/${param}`)
    .then((res) => res.json())
    .then((data) => displayDoctorDetails(data));
};

const displayDoctorDetails = (product) => {
  // showing details
  console.log(product);

  parent = document.getElementById("product-details");
  const div = document.createElement("div");
  div.classList.add("product-details-container");
  div.innerHTML = `
       <div class="product-img">
        <img src="${product.image}" alt="">
       </div>
       <div class="product-info">
        <h2>${product.title}</h2>
        <h4 class="card-title h5">Category: ${product.category}</h4>
        <p class="my-3">Rating: ${product.rating.rate}</p>
        
        <p class="my-3">${product.description}</p>
        <h4>Fees: ${product.price} BDT</h4>
        
       </div>
    `;
  parent.appendChild(div);
};

getParems();

const products = [
  {
    name: "Your Career",
    price: 280.0,
    img: "https://plus.unsplash.com/premium_photo-1722686516461-46770349c814?q=80&w=2564&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
  },
  {
    name: "Designing Your Life",
    price: 260.0,
    img: "https://images.pexels.com/photos/799443/pexels-photo-799443.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
  },
  {
    name: "Learn Gym & Fitness",
    price: 150.0,
    img: "https://images.pexels.com/photos/681795/pexels-photo-681795.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
  },
  {
    name: "Your Life in London",
    price: 90.0,
    img: "https://images.pexels.com/photos/1275929/pexels-photo-1275929.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
  },
  {
    name: "Control of Your Ideas",
    price: 120.0,
    img: "https://images.pexels.com/photos/2047905/pexels-photo-2047905.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
  },
  {
    name: "Service Honey Restaurant",
    price: 150.0,
    img: "https://images.pexels.com/photos/2002339/pexels-photo-2002339.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
  },
  {
    name: "Building Future",
    price: 380.0,
    originalPrice: 415.0,
    sale: true,
    img: "https://images.pexels.com/photos/2531237/pexels-photo-2531237.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
  },
  {
    name: "Basic",
    price: 199.0,
    img: "https://images.pexels.com/photos/21856199/pexels-photo-21856199/free-photo-of-infinity-pool-with-view-of-the-palm-islands-in-dubai.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
  },
];

const products2 = [
  {
    name: "Stanndard",
    price: 499.0,
    img: "https://plus.unsplash.com/premium_photo-1722686516461-46770349c814?q=80&w=2564&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
  },
  {
    name: "Extended",
    price: 799.0,
    img: "https://images.pexels.com/photos/799443/pexels-photo-799443.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
  },
  {
    name: "Company",
    price: 399.0,
    img: "https://images.pexels.com/photos/681795/pexels-photo-681795.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
  },
  {
    name: "Enterprise",
    price: 550.0,
    img: "https://images.pexels.com/photos/1275929/pexels-photo-1275929.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
  },
  {
    name: "Business",
    price: 699.0,
    img: "https://images.pexels.com/photos/2047905/pexels-photo-2047905.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
  },
];

const dropdowns = document.querySelectorAll(".dropdown");

dropdowns.forEach((dropdown) => {
  const select = dropdown.querySelector(".select");
  const caret = dropdown.querySelector(".caret");
  const menu = dropdown.querySelector(".menu");
  const options = dropdown.querySelectorAll(".menu li");
  const selected = dropdown.querySelector(".selected");

  select.addEventListener("click", () => {
    select.classList.toggle("select-clicked");
    caret.classList.toggle("caret-rotate");
    menu.classList.toggle("menu-open");
  });

  options.forEach((option) => {
    option.addEventListener("click", () => {
      selected.innerText = option.innerText;
      select.classList.toggle("select-clicked");
      caret.classList.toggle("caret-rotate");
      menu.classList.toggle("menu-open");

      options.forEach((option) => {
        option.classList.remove("active");
      });
      option.classList.add("active");
    });
  });
});

function createProductElement(product) {
  const col = document.createElement("div");
  col.className = "col-md-3 col-sm-6";

  col.innerHTML = `
        <div class="product-item">
        <div class="img-and-name">
        <div class="img-and-badge">
            ${product.sale ? '<span class="sale-badge">SALE!</span>' : ""}
            <img src="${product.img}" alt="${product.name}">
  </div>
            <h6>${product.name}</h6>
            <p class="m-0">
                ${
                  product.sale
                    ? `<s class="original-price">$${product.originalPrice.toFixed(
                        2
                      )}</s> `
                    : ""
                }
                <span class="sale-price">$${product.price.toFixed(2)}</span>
            </p>
            <button class="add-to-cart">Add to Cart</button>
        </div>
        </div>
    `;

  return col;
}

function displayProducts(productsToShow) {
  const productList = document.getElementById("product-list");
  productList.innerHTML = "";

  productsToShow.forEach((product) => {
    productList.appendChild(createProductElement(product));
  });
}

function goToPage1() {
  displayProducts(products);
  updatePagination(1);
  updateArrowVisibility(1);
}

function goToPage2() {
  displayProducts(products2);
  updatePagination(2);
  updateArrowVisibility(2);
}

function updatePagination(activePageNumber) {
  const pagination = document.querySelector(".pagination");
  const pageItems = pagination.querySelectorAll(".page-item");

  pageItems.forEach((item, index) => {
    if (index === activePageNumber) {
      item.classList.add("active");
    } else {
      item.classList.remove("active");
    }
  });
}

function updateArrowVisibility(pageNumber) {
  const leftArrow = document.getElementById("left-arrow");
  const rightArrow = document.getElementById("right-arrow");
  if (pageNumber === "1" || pageNumber === 1) {
    leftArrow.style.display = "none";
    rightArrow.style.display = "block";
  } else if (pageNumber === "2" || pageNumber === 2) {
    leftArrow.style.display = "block";
    rightArrow.style.display = "none";
  } else {
    leftArrow.style.display = "block";
    rightArrow.style.display = "block";
  }
}

document.addEventListener("DOMContentLoaded", () => {
  goToPage1();
  updateArrowVisibility(1);

  document.querySelector(".pagination").addEventListener("click", (e) => {
    if (e.target.classList.contains("page-link")) {
      const pageNumber = e.target.textContent;
      if (pageNumber === "1") {
        goToPage1();
      } else if (pageNumber === "2") {
        goToPage2();
      }
    }
  });
});


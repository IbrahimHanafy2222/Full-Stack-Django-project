// Add to Cart alert with product name
document.querySelectorAll(".add-cart").forEach(btn => {
  btn.addEventListener("click", () => {
    let productName = btn.closest(".card").querySelector(".card-title").textContent;
    alert(`${productName} has been added to your cart!`);
  });
});

// script.js
let lastScrollTop = 0;
const navbar = document.querySelector('.navbar');

window.addEventListener('scroll', function() {
  let scrollTop = window.pageYOffset || document.documentElement.scrollTop;

  if (scrollTop > lastScrollTop && scrollTop > 50) {
    // Scrolling down -> hide navbar
    navbar.style.top = "-100px";
  } else {
    // Scrolling up -> show navbar
    navbar.style.top = "0";
  }

  lastScrollTop = scrollTop <= 0 ? 0 : scrollTop; // Prevent negative scroll
});

document.addEventListener("scroll", () => {
  const section = document.querySelector(".product-scroll-section");
  const images = section.querySelectorAll("img");

  // Get scroll progress inside the section
  const rect = section.getBoundingClientRect();
  const scrollTop = window.scrollY - section.offsetTop;
  const scrollHeight = section.offsetHeight;
  const progress = Math.min(Math.max(scrollTop / scrollHeight, 0), 1);

  // Pick which image to show based on scroll
  const index = Math.floor(progress * images.length);

  images.forEach((img, i) => {
    img.classList.toggle("active", i === index);
  });
});


function changeQty(val) {
  let qty = document.getElementById("qtyInput");
  let newVal = parseInt(qty.value) + val;
  if (newVal >= 1) qty.value = newVal;
}

//Handle Sold Out Sizes
document.querySelectorAll(".size-btn.sold-out").forEach(btn => {
  btn.addEventListener("click", () => {    alert("Sold Out");
  });
});

// Handle Color Selection (jump to image)
document.querySelectorAll(".color-circle").forEach(circle => {
  circle.addEventListener("click", () => {
    let colorName = circle.getAttribute("data-color");
    let targetId = circle.getAttribute("data-target");

    // Update color text
    document.getElementById("selectedColor").textContent = "Color: " + colorName;

    // Highlight selected
    document.querySelectorAll(".color-circle").forEach(c => c.classList.remove("selected"));
    circle.classList.add("selected");

    // Jump to the target image (like thumbnail click)
    let targetImg = document.querySelector(targetId);
    if (targetImg) {
      // Hide all, show target
      document.querySelectorAll(".product-images-sequence img")
        .forEach(img => img.classList.remove("active"));
      targetImg.classList.add("active");

      // Smooth scroll into view
      targetImg.scrollIntoView({ behavior: "smooth", block: "center" });
    }
  });
});



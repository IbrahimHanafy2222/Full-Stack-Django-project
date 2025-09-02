
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


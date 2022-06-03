////////////////////////////////////////////////////////////
// Hamburger Nav Menu
let menuOpen = false;
const burgerButton = document.querySelector('.burger-button');
const menu = document.querySelector('.menu');

burgerButton.addEventListener('click', (e) => {
    menu.classList.toggle('open');
})

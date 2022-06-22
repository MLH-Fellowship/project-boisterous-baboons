////////////////////////////////////////////////////////////
// Hamburger Nav Menu
let menuOpen = false;
const burgerButton = document.querySelector('.burger-button');
const menu = document.querySelector('.menu');

burgerButton.addEventListener('click', () => {
    menu.classList.toggle('open');
})

const slideMenu = document.querySelector('.slide-menu');

slideMenu.addEventListener('click', (e) => {
    e.preventDefault();
    const link = e.target.closest('li');
    if (link?.classList.contains('nav__link')) {
        const id = link.querySelector('a').getAttribute('href');
        document.querySelector(id).scrollIntoView({
            behavior: 'smooth'
        })
    }
})

////////////////////////////////////////////////////////////
// Reveal Elements on Scroll
const sections = document.querySelectorAll('section:not(:first-child)');
let cards = [];

sections.forEach((section) => {
    section.querySelectorAll('div').forEach((card) => card.classList.add('hide-card'))
})

const revealSection = function (entries) {
    entries.forEach((entry) => {
        if (entry.isIntersecting) {
            entry.target.querySelectorAll('div').forEach((card) => card.classList.remove('hide-card'))
        } else {
            entry.target.querySelectorAll('div').forEach((card) => card.classList.add('hide-card'))
        }
    })
}

const sectionObserver = new IntersectionObserver(revealSection, {
    root: null,
    threshold: 0.3
});

sections.forEach((section) => {
    sectionObserver.observe(section);
})


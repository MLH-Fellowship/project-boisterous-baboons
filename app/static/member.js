////////////////////////////////////////////////////////////
// Hamburger Nav Menu
let menuOpen = false;
const burgerButton = document.querySelector('.burger-button');
const menu = document.querySelector('.menu');

burgerButton.addEventListener('click', () => {
    menu.classList.toggle('open');
})


////////////////////////////////////////////////////////////
// Map
const map = L.map('map').setView([40, 0], 2.2);

L.tileLayer('https://tiles.stadiamaps.com/tiles/alidade_smooth_dark/{z}/{x}/{y}{r}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);

const colours = {
    "juan": "violet",
    "noah": "blue",
    "malik": "orange"
}

let visited;
const member = window.location.href.split('/').slice(-1)[0];

const memberIcon = new L.Icon({
    iconUrl: `https://raw.githubusercontent.com/pointhi/leaflet-color-markers/master/img/marker-icon-${colours[member]}.png`,
    iconSize: [25, 41],
    iconAnchor: [12, 41],
    popupAnchor: [1, -34],
    shadowSize: [41, 41]
});

fetch(`/visited/${member}`)
    .then((res) => res.json())
    .then((data) => {
        visited = data.visited;
        visited.forEach((place) => {
            L.marker(place[1], { icon: memberIcon }).addTo(map)
        })
    })
    .catch(err => console.log(err))

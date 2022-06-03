////////////////////////////////////////////////////////////
// Map
const map = L.map('map').setView([40, 0], 2.2);

L.tileLayer('https://tiles.stadiamaps.com/tiles/alidade_smooth_dark/{z}/{x}/{y}{r}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);

const juanVisited = [["Canada", [56.13, -106.34]], ["Venezuela", [6.423, -66.58]], ["Spain", [40.46, -3.749]], ["England", [52.35, -1.17]], ["Peru", [-9.18, -75.0]], ["USA", [37.09, -95.71]]];
const malikVisited = [["USA", [37.09, -95.71]], ["Jamaica", [18.1, -77.29]]];
const noahVisited = [["Brazil", [-14.235, -51.925]], ["Mexico", [23.63, -102.5]], ["Germany", [51.16, 10.45]], ["England", [52.35, -1.17]], ["Venezuela", [6.423, -66.58]], ["Dominican Republic", [18.73, -70.16]], ["Canada", [56.13, -106.34]]];


juanVisited.forEach((place) => {
    L.marker(place[1]).addTo(map)
})

malikVisited.forEach((place) => {
    L.marker(place[1]).addTo(map)
})

noahVisited.forEach((place) => {
    L.marker(place[1]).addTo(map)
})
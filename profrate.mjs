import { profData } from './data.js';

function Print() {
    var x = getElementById("search").value;
    alert("You searched for " + x);
}

function createFacultyCard(faculty) {
    const card = document.createElement('div');
    card.className = 'faculty-card';

    const img = document.createElement('img');
    img.src = faculty.headshot;
    img.alt = faculty.name;
    img.className = 'faculty-image';
    card.appendChild(img);

    const name = document.createElement('h3');
    name.className = 'faculty-name';
    name.textContent = faculty.name;
    card.appendChild(name);

    const position = document.createElement('p');
    position.className = 'faculty-position';
    position.textContent = faculty.position;
    card.appendChild(position);

    //card.onclick = seeOneProf(faculty);
    return card;
}

function renderFacultyGallery() {
    const gallery = document.getElementById('faculty-gallery');

    profData.forEach(faculty => {
        const card = createFacultyCard(faculty);
        card.onclick = function () {
            window.location.href = `viewProfProfile.html?name=${encodeURIComponent(faculty.name)}`;
        };
        gallery.appendChild(card);
    });
}

function onclick() {

}
function seeOneProf(profName) {

    profData.forEach(faculty => {
        if (faculty.name == profName) {

            window.location.href = 'viewProfProfile.html';
        }
    })
    //console.(prof)
    // const dataToSend = prof
    //const displayElement = document.getElementById('prof-name');

    //if (profName) {
    //const thisProf = createFacultyCard(profName)
    // }

    //window.location.href = 'viewProfProfile.html';

}

document.addEventListener('DOMContentLoaded', renderFacultyGallery);

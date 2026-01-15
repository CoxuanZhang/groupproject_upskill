import { profData } from './data.js';

function Print(){
    var x = getElementById("search").value;
    alert("You searched for " + x );
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

    return card;
}

function renderFacultyGallery() {
    const gallery = document.getElementById('faculty-gallery');
    
    profData.forEach(faculty => {
        const card = createFacultyCard(faculty);
        gallery.appendChild(card);
    });
}

document.addEventListener('DOMContentLoaded', renderFacultyGallery);

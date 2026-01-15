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

function renderFacultyGallery(facultyList = profData) {
    console.log('Rendering gallery with', facultyList.length, 'faculty members');
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
function handleSearch() {
    const searchInput = document.getElementById('search-input');
    const searchTerm = searchInput.value;
    const results = searchFaculty(searchTerm);
    renderFacultyGallery(results);
}

function searchFaculty(searchTerm) {
    const term = searchTerm.toLowerCase().trim();
    
    // If search is empty, show all
    if (term === '') {
        return profData;
    }
    
    // Filter faculty by name
    const results = profData.filter(faculty => 
        faculty.name.toLowerCase().includes(term)
    );
    
    return results;
}


document.addEventListener('DOMContentLoaded', function(){
    renderFacultyGallery();

    const searchButton = document.getElementById('search-button');
    searchButton.addEventListener('click', handleSearch);
    const searchInput = document.getElementById('search-input');
    
    searchInput.addEventListener('keypress', function(e) {
        if (e.key === 'Enter') {
            handleSearch();
        }
    });

});

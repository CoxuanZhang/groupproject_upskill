import { profData } from './data.js';

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

function renderFacultyGallery(facultyList = profData) {
    console.log('Rendering gallery with', facultyList.length, 'faculty members');
    const gallery = document.getElementById('faculty-gallery');
    const noResults = document.getElementById('no-results');

    // Clear existing cards
    gallery.innerHTML = '';

    if (facultyList.length === 0) {
        noResults.style.display = 'block';
        return;
    }
    noResults.style.display = 'none';
    
    facultyList.forEach(faculty => {
        const card = createFacultyCard(faculty);
        gallery.appendChild(card);
    });
}

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

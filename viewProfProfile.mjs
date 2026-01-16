import { profData } from './data.js';

document.addEventListener('DOMContentLoaded', () => {
    const params = new URLSearchParams(window.location.search);
    const nameParam = params.get('name');
    if (!nameParam) {
        console.error('Missing ?name= query parameter');
        return;
    }

    const decodedName = decodeURIComponent(nameParam).trim().toLowerCase();
    const prof = profData.find(p => p.name && p.name.trim().toLowerCase() === decodedName);

    let container = document.getElementById('prof-name');
    if (!container) {
        container = document.createElement('div');
        container.id = 'prof-name';
        document.body.appendChild(container);
    }
    container.innerHTML = ''; 

    if (!prof) {
        const msg = document.createElement('p');
        msg.textContent = `Professor "${decodeURIComponent(nameParam)}" not found.`;
        container.appendChild(msg);
        return;
    }

    const card = document.createElement('div');
    card.className = 'faculty-card';

    const nameEl = document.createElement('h2');
    nameEl.className = 'faculty-name';
    nameEl.textContent = prof.name || '';
    card.appendChild(nameEl); 

    const img = document.createElement('img');
    img.id = 'prof-image';
    img.className = 'faculty-image';
    img.src = prof.headshot || '';
    img.alt = prof.name || 'Professor headshot';
    card.appendChild(img);

    

    const posEl = document.createElement('p');
    posEl.className = 'faculty-position';
    posEl.textContent = prof.position || '';
    card.appendChild(posEl);

    //card.style.backgroundColor = '#b15454ff';
    // Add any other fields from prof (except name/headshot/position)
    const skip = new Set(['name', 'headshot', 'position']);
    Object.entries(prof).forEach(([key, value]) => {
        if (skip.has(key) || value == null) return;
        const field = document.createElement('p');
        field.className = `prof-${key}`;
    //format
        const label = key.replace(/([A-Z])/g, ' $1').replace(/^\w/, c => c.toUpperCase());
        field.innerHTML = `<strong>${label}:</strong> ${String(value)}`;
        card.appendChild(field);
    });

    
    card.style.marginLeft = '10px';
    container.style.backgroundColor = '#CFDBD5';
    container.style.width = '75%';
    container.style.marginLeft = '10%';
    container.style.alignContent= 'center';
    container.style.borderRadius = '10px';


    container.appendChild(card);

});
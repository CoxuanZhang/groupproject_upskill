import { profData } from './data.js';
const params = new URLSearchParams(window.location.search);
const nameParam = params.get('name');

document.addEventListener('DOMContentLoaded', () => {
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


    //card.style.marginLeft = '10px';
   // container.style.backgroundColor = '#CFDBD5';
    //container.style.width = '75%';
    //container.style.marginLeft = '10%';
    //container.style.alignContent = 'center';
    //container.style.borderRadius = '10px';


    container.appendChild(card);
});

const slider = document.getElementById('grade');
const gradeLabels = ['F', 'P', 'C-', 'C', 'C+', 'B-', 'B', 'B+', 'A-', 'A', 'A+'];
let selectedGrade = gradeLabels[0];
let professorName = nameParam ? decodeURIComponent(nameParam).trim() : 'Unknown';

document.addEventListener('DOMContentLoaded', () => {
    // Initialize slider listener after DOM loads
    if (slider) {
        slider.addEventListener('input', function() {
            selectedGrade = gradeLabels[this.value];
            console.log('Selected grade updated to:', selectedGrade);
        });
    }
    
    // Call updateAllGraphs after DOM is ready
    updateAllGraphs();
});

const CRITERIA = {
    1: 'pace', 
    2: 'procrastination',
    3: 'prior_experience'
};

async function loadGraph(graphNumber, criteria) {
    const response = await fetch('http://127.0.0.1:5000/generate-graph', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            professor: professorName,
            criteria: criteria,
            lowest_grade: selectedGrade
        })
    });
    if (!response.ok) {
        console.error(`HTTP error! status: ${response.status}`);
        throw new Error(`HTTP error! status: ${response.status}`);
    }
    const data = await response.json();
    console.log(`DEBUG: Graph ${graphNumber} response:`, data);
    
    if (!data.success) {
        console.error(`Failed to generate graph ${graphNumber}:`, data.error);
        return;
    }
    
    const graphImg = document.getElementById(`graph-${graphNumber}`);
    if (!graphImg) {
        console.error(`Image element graph-${graphNumber} not found`);
        return;
    }
    
    graphImg.src = 'data:image/png;base64,' + data.image;
    graphImg.style.display = 'block';
    console.log(`DEBUG: Graph ${graphNumber} loaded successfully`);
}

async function updateAllGraphs() {
    console.log('updateAllGraphs called');
    const updateBtn = document.getElementById('update-btn');
    if (!updateBtn) {
        console.error('update-btn not found');
        return;
    }
    updateBtn.disabled = true;
    
    try {
        await Promise.all([
            loadGraph(1, CRITERIA[1]),
            loadGraph(2, CRITERIA[2]),
            loadGraph(3, CRITERIA[3])
        ]);
    } catch (error) {
        console.error('Error updating graphs:', error);
    } finally {
        updateBtn.disabled = false;
    }
}

// Make updateAllGraphs globally accessible for the onclick handler
window.updateAllGraphs = updateAllGraphs;

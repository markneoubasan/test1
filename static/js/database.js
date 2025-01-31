function ShowDashboard() {
    document.getElementById('dashboard').style.display = 'block';
    document.getElementById('user').style.display = 'none';
    document.getElementById('post').style.display = 'none';
    document.getElementById('course').style.display = 'none';
    document.getElementById('enrollment').style.display = 'none';
    document.getElementById('instructor').style.display = 'none';
}

function showSection(section) {
    document.querySelectorAll('.content-section').forEach(function(sec) {
        sec.style.display = 'none';
    });
    document.getElementById(section).style.display = 'block';
}

window.onload = function() {
    const urlParams = new URLSearchParams(window.location.search)
    const section = urlParams.get('section');
    if (section) {
        showSection(section)
    }
    else {
        showSection('dashboard');
    }
}

function showSection(sectionId) {
    // Hide all sections
    let sections = document.querySelectorAll('.content-section');
    sections.forEach(section => {
        section.style.display = 'none';
    });

    // Show the selected section
    let section = document.getElementById(sectionId);
    section.style.display = 'block';
}

function ShowDashboard() {
    showSection('dashboard');
}

document.addEventListener("DOMContentLoaded", function () {
    const navIcon = document.getElementById('nav-icon3');
    const menu = document.getElementById('menu');
    const bg = document.getElementById('black-bg');


    navIcon.addEventListener('click', function () {
        navIcon.classList.toggle('open');
        menu.classList.toggle('menu-open');
        bg.classList.toggle('open');
    });
    bg.addEventListener('click', function () {
        bg.classList.toggle('open');
        navIcon.classList.toggle('open');
        menu.classList.toggle('menu-open');
    });
});






const pillContainer = document.querySelector('.pill-container');
const numberOfPills = 100; // Adjust the number of pills as desired

const pillImages = [
    'pill1.png',
    'pill2.png',
    'pill3.png'
];



function createFloatingPills() {
    for (let i = 0; i < numberOfPills; i++) {
        const pill = document.createElement('img');
        pill.classList.add('pill');

        // Randomly select a pill image
        const randomImageIndex = Math.floor(Math.random() * pillImages.length);
        pill.src = 'images/' + pillImages[randomImageIndex];

    // Randomize initial positions
        const randomLeft = Math.random() * 100;
        const randomTop = Math.random() * 100;
        pill.style.left = `${randomLeft}vw`;
        pill.style.top = `${randomTop}vh`;

        // Randomize animation duration and delay
        const randomDuration = Math.random() * 3 + 2;
        const randomDelay = Math.random() * 3;
        pill.style.animationDuration = `${randomDuration}s`;
        pill.style.animationDelay = `-${randomDelay}s`; // Use a negative delay for a staggered start

        pillContainer.appendChild(pill);
    }
}

window.onload = function() {
    createFloatingPills(); // Call the function when the page is fully loaded
};

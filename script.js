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
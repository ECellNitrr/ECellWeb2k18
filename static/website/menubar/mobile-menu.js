let menuTrigger = document.querySelector('.menu-trigger');
let menubar = document.querySelector('.menubar');

menuTrigger.addEventListener('click', function () {
    if (menubar.style.display == 'none' || !menubar.style.display) {
        menubar.style.display = 'flex';
        menuTrigger.classList.add('menu-close');
    } else {
        menubar.style.display = 'none';
        menuTrigger.classList.remove('menu-close');
    }
});
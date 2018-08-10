// these 2 are declared in the modal-dom js
// let menuTrigger = document.querySelector('.menu-trigger');
// let menubar = document.querySelector('.menubar');

menuTrigger.addEventListener('click', function () {
    if (menubar.style.display == 'none' || !menubar.style.display) {
        menubar.style.display = 'flex';
        menuTrigger.classList.add('menu-close');
        loggedin_user_box.style.display = 'block'
    } else {
        menubar.style.display = 'none';
        menuTrigger.classList.remove('menu-close');
        loggedin_user_box.style.display = 'none'
    }
});
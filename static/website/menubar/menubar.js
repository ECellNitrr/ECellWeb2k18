// these 2 are declared in the modal-dom js
let menuTrigger = document.querySelector('.menu-trigger');
let menubar = document.querySelector('.menubar');

menuTrigger.addEventListener('click', function () {
    menuTrigger.classList.toggle('menu-close');
    menubar.classList.toggle('menu-close');

    // if(window.innerWidth<500) {
    //     mobile_menu_toggle()
    // }else {
    //     desktop_menu_toggle()
    // }
});

var mobile_menu_toggle = () => {
    if (menubar.style.display == 'none' || !menubar.style.display) {
        menubar.style.display = 'flex';
        menuTrigger.classList.toggle('menu-close');
    } else {
        menubar.style.display = 'none';
        menuTrigger.classList.remove('menu-close');
    }
}

var desktop_menu_toggle = () => {
    menuTrigger.classList.toggle('menu-close')
}
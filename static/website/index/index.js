var cover = document.querySelector('.cover');
var header = document.querySelector('header');
var innerHeight = Number(window.innerHeight);
var innerWidth = Number(window.innerWidth);


if (innerWidth < 700) {
    if (innerHeight > 550) {
        innerHeight = 550;
    }
}

console.log(innerHeight);

header.style.height = `${innerHeight}px`;
cover.style.height = `${innerHeight}px`;

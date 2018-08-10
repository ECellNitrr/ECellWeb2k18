// display the svg after the background has been loader
document.querySelector('svg').style.display = 'block'
var body = document.querySelector('body')
body.style.background = 'white'
body.style.color = 'black'

// draw the lines
var lineDrawing = anime({
    targets: 'path',
    strokeDashoffset: [anime.setDashoffset, 0],
    easing: 'easeInOutQuad',
    duration: 2000,
    delay: function (el, i) {
        return i * 100 + 500
    },
    direction: 'alternate',
    loop: false
});

// show the circles
var circles = document.querySelectorAll('circle');
var i = 1
circles.forEach(circle => {
    i += 1
    setTimeout(() => {
        circle.style.opacity = 1
    }, 800 + i * 1000 / 20);
})

// show the texts
var texts = document.querySelectorAll('text');
texts.forEach(text => {
    i += 1
    setTimeout(() => {
        text.style.opacity = 1
    }, i * 1000 / 20);
})

// animate the logo
var logo = document.querySelector('#logo');
logo.style.stroke = 'yellowgreen'
setTimeout(() => {
    setTimeout(() => {
        logo.style['stroke-width'] = 3
    }, 3300);
})

// hide the loader
setTimeout(() => {
    document.querySelector('.loader').style.transform = 'translateY(-125vh)';
    document.querySelector('.loader svg').style.opacity = 0;
    body.style['overflow-y']='auto'
    body.style.height='auto'
    document.querySelector('#menubar').style.display='block'
// }, 4300)
}, 0)    

setTimeout(()=>{
    document.querySelector('.loader').remove();
// },5000)
},0)

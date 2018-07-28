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
    }, 500 + i * 1000 / 20);
})

// show the texts
var texts = document.querySelectorAll('text');
texts.forEach(text => {
    i += 1
    setTimeout(() => {
        text.style.opacity = 1
    }, i * 1000 / 20);
})

// color path
var paths = document.querySelectorAll('.loader path');
paths.forEach(path => {
    path.style['stroke'] = "#"+((1<<24)*Math.random()|0).toString(16)
})

// animate the logo
var logo = document.querySelector('#logo');
logo.style.stroke = 'gold'
setTimeout(() => {
    setTimeout(() => {
        // logo.style.fill = 'gold'
        logo.style['stroke-width'] = 3
    }, 3300);
})

// hide the loader
setTimeout(() => {
    document.querySelector('.loader').style.transform = 'translateY(-100vh)';
    document.querySelector('.loader svg').style.opacity = 0;
    body.style.overflow='auto'
    body.style.height='auto'
    document.querySelector('#menubar').style.display='block'
}, 3700)

    // flash the background colors
    // var bgclrs = ['#18181c','olive','darkslateblue','grey','orange','darkred']
    // var loader =  document.querySelector('.loader');
    // var i = bgclrs.length-1;
    // setInterval(()=> {
    //   if(i>=0){
    //     loader.style.background = bgclrs[i];
    //     console.log(bgclrs[i]);
    //     i -=1;
    //   }
    // }, 300)
// show the gallery
var gallery_div = document.querySelector('#gallery')
for (var i = 0; i < 12; i++) {
    gallery_div.innerHTML += `
        <div class='gimg'>
            <img src='/static/website/gallery/img/${i + 1}.jpg'>
        </div>
    `
}

// on click show big img
var gimgs = document.querySelectorAll('.gimg img')
var bimg = document.querySelector('#big_img')
var bcontainer = document.querySelector('#big_container')
var bcloseBtn = document.querySelector('#bcloseBtn')

gimgs.forEach(gimg => {
    gimg.addEventListener('click', function (e) {
        e.preventDefault()
        bimg.src = gimg.src
        bcontainer.style.top = 0
        bimg.style.height = '90%'
    })
})


bcontainer.addEventListener('click', (e) => {
    e.preventDefault()
    // if clicked on img return 
    if (e.target != bcontainer) return
    // if clicked on the container
    bcontainer.style.top = "-100vh"
    bimg.style.height = '0%'
})

bcloseBtn.addEventListener('click', (e) => {
    e.preventDefault()
    console.log('bcloseBtn')
})
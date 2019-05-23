var gallery = document.querySelector('#lightgallery')
var spinnner = document.querySelector('#spinner')

fetch('/gallery_api/').then(d => d.json())
    .then(d => {
        console.log(d)
        spinnner.parentNode.removeChild(spinnner)
        d.forEach((ele,i) => {
            gallery.innerHTML += `
<h4 class="category">
   <a href="/gallery/${i}/">${ele.name}</a>                 
</h4>
            `
        })
    })



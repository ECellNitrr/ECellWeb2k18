const spinner = document.querySelector('#spinner')
var gallery = document.querySelector(('#lightgallery'))

fetch('/gallery_api/').then(d=>d.json())
    .then(d=>{
        console.log(d)
        spinner.parentNode.removeChild(spinner)

        data = d[cid]

        for(var i=1; i<=data.count; i++){
            gallery.innerHTML += `
                <a href='/${data.url+i+"a.jpg"}'>
                <img src="/${data.url+i+'ab.jpg'}>          
                </a> `
        }
    })
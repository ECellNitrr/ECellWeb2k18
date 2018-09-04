var startups_div = document.querySelector('#startups')
var cover = document.querySelector('#cover')
var modal = document.querySelector('#modal')

fetch('/startups/list/')
    .then(d => d.json())
    .then(d => {
        console.log(JSON.stringify(d, null, 2))
    })
    .catch(err => console.error(err))
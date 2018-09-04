var startups_div = document.querySelector('#startups')
var cover = document.querySelector('#cover')
var modal = document.querySelector('#modal')
var spinner = document.querySelector('#spinner')

var startups = []

fetch('/startups/list/')
    .then(d => d.json())
    .then(d => {
        spinner.remove()
        startups = d.startups
        create_startups(startups)
    })
    .catch(err => console.error(err))

create_startups = (items) => {
    items.forEach((i) => {
        startups_div.innerHTML +=  `
            <div class=startup>
                <div class=img-holder>
                    <img src=${i.pic}>
                </div>
                <h3 class=title>${i.name}</h3>
                <p class=desc>${i.details}</p>
                <button class=more data-id=${i.id}>more</button>
            </div>
        `
    })
}
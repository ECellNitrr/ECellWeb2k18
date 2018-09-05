var startups_div = document.querySelector('#startups')
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
                <div class=mimg-holder>
                    <img src=${i.pic}>
                </div>
                <h3 class=title>${i.name}</h3>
                <p class=desc>${i.details}</p>
                <button class=more data-id=${i.id}>more</button>
            </div>
        `
    })

    // this adds the event listeners for more btn
    startup_modal()
}
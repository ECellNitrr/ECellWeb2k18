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
            <div class='iholder'>
                <img src=${i.pic}>
            </div>
            <div class= 'details'>
                <button class='more text-right' data-id=${i.id}>read more</button>
            </div>
        </div>
        `
    })

    // this adds the event listeners for more btn
    startup_modal()
}
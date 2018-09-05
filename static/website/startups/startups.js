var startups_div = document.querySelector('#startups')
var spinner = document.querySelector('#spinner')

var startups = []
var regsitered_startups = []

// fetch already registered startups
if (user.innerHTML[0] == '@') {
    console.log('fetching startups')
    fetch('/startups/userstartups')
        .then(d => d.json())
        .then(d => {
            regsitered_startups = d.id
            update_color()
        })
        .catch(err => console.error(err))
}

// fetch list of startups
fetch('/startups/list/')
    .then(d => d.json())
    .then(d => {
        spinner.remove()
        startups = d.startups
        create_startups(startups)
    })
    .catch(err => console.error(err))

// display the startups
create_startups = (items) => {
    items.forEach((i) => {
        startups_div.innerHTML += `
        <div class=startup>
            <div class='iholder'>
                <img src=${i.pic}>
            </div>
            <button class='more' data-id=${i.id}>read more</button>
        </div>
        `
    })

    // this adds the event listeners for read more btn
    startup_modal()
}
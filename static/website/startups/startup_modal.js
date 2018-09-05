// startups arr  is in startups.js

var cover = document.querySelector('#cover')
var modal = document.querySelector('#modal')
var modal_container = document.querySelector('#modal_container')
var more_btns;

// adding events listeners to more btns
startup_modal = () => {
    more_btns = document.querySelectorAll('.more')
    more_btns.forEach(btn => {
        btn.addEventListener('click', (e) => {
            e.preventDefault()
            show_modal(btn.dataset.id)
        })
    })

    show_modal(1)
}

show_modal = (id) => {
    var i = startups.find((startup) => startup.id == id)

    modal.innerHTML = `
    <h3 class='title mt-5 text-center text-uppercase'>${i.name}</h3>
    <div class='row'>
        <div class='mimg-holder text-center col-md-5'>
            <img src=${i.pic}>
        </div>
        <div class='col-md-7'>
            <p><strong>Founder:</strong> ${i.founder}</p>
            <p><strong>Contact:</strong> ${i.contact}</p>
            <p><strong>Email:</strong> ${i.email}</p>
            <p><strong>Address:</strong> ${i.address}</p>
            <p id=desc>${i.details}</p>
        </div>
    </div>
    <div class='text-center btns'>
        <button class='register green' data-sid=${i.id}>Register</button>
        <button class=mclose>Close</button>
    </div>
    `
    // add the show class
    modal_container.classList.add('show')
}


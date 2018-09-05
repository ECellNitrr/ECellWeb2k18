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
    <div id='in_modal' class='row'>
        <div class='mimg-holder col-md-5'>
            <img src=${i.pic}>
            <div class='text-center'>
                <button class=register>Register</button>
                <button class=mclose>Close</button>
            </div>
        </div>
        <div class='col-md-7'>
            <h3 class=title>${i.name}</h3>
            <p>Founder: ${i.founder}</p>
            <p>Contact: ${i.contact}</p>
            <p>Email: ${i.email}</p>
            <p>Address: ${i.address}</p>
            <p class=desc>${i.details}</p>
        </div>
    </div>
    `
    // add the show class
    modal_container.classList.add('show')
}


// startups arr  is in startups.js

var cover = document.querySelector('#cover')
var modal = document.querySelector('#modal')
var modal_container = document.querySelector('#modal_container')
var more_btns;

startup_modal = () => {
    more_btns = document.querySelectorAll('.more')
    more_btns.forEach(btn => {
        btn.addEventListener('click', (e) => {
            e.preventDefault()
            show_modal(btn.dataset.id)
        })
    })
}

show_modal = (id) => {
    console.log(id)
    var i = startups.find((startup) => startup.id == id)

    modal.innerHTML = `
    <div id=in_modal>
        <div class=mimg-holder>
            <img src=${i.pic}>
        </div>
        <h3 class=title>${i.name}</h3>
        <p>Founder: ${i.founder}</p>
        <p>Contact: ${i.contact}</p>
        <p>Email: ${i.email}</p>
        <p>Address: ${i.address}</p>
        <p class=desc>${i.details}</p>
        <button class=register>register</button>
    </div>
    `
    // add the show class
    modal_container.classList.add('show')
}


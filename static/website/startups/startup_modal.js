// startups arr  is in startups.js

var cover = document.querySelector('#cover')
var modal = document.querySelector('#modal')
var modal_container = document.querySelector('#modal_container')
var more_btns, register_btn, close_btn;

// update colors 
update_color = () => {
    more_btns.forEach(i => {
        var flag = regsitered_startups.find(rs => rs == i.dataset.id)
        if (flag) {
            i.classList.add('greeny')
        } else {
            i.classList.remove('greeny')
        }
    })


    if (register_btn) {
        var flag = regsitered_startups.find(rs => rs == register_btn.dataset.sid)
        if (flag) {
            register_btn.innerHTML = 'Deregister'
            register_btn.classList.add('green')
        } else {
            register_btn.innerHTML = 'Register'
            register_btn.classList.remove('green')
        }
    }

}


// adding events listeners to more btns
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
    var i = startups.find((startup) => startup.id == id)

    modal.innerHTML = `
        <h3 class='title mt-5 mb-0 text-center text-uppercase'>${i.name}</h3>
        <hr>
        <div class='row'>
            <div class='mimg-holder text-center col-md-5'>
                <img src=${i.pic}>
            </div>
            <div class='col-md-7 detail'>
                <p><strong>Founder:</strong> ${i.founder}</p>
                <p><strong>Contact:</strong> ${i.contact}</p>
                <p><strong>Email:</strong> ${i.email}</p>
                <p><strong>Address:</strong> ${i.address}</p>
                <p id=desc>${i.details}</p>
            </div>
        </div>
        <div class='text-center btns'>
            <button class='register' data-sid=${i.id}>Register</button>
            <button class=mclose>Close</button>
        </div>
    `
    // add the show class
    modal_container.classList.add('show')
    register_btn = document.querySelector('#modal .register')
    close_btn = document.querySelector('#modal .mclose')
    update_color()
    // monitor for events
    events()
}

events = () => {
    // close modal
    close_btn.addEventListener('click', (e) => {
        modal_container.classList.remove('show')
    })

    // register event
    register_btn.addEventListener('click', (e) => {
        e.preventDefault()

        // edge cases
        if (user.innerHTML[0] === '#') {
            modal_container.classList.remove('show')
            o_cont.classList.add('show')
            return false
        } else if (user.innerHTML[0] === 'L') {
            modal_container.classList.remove('show')
            l_cont.classList.add('show')
            return false
        }

        // take action
        console.log(register_btn.innerHTML)
        if (register_btn.innerHTML == 'Register') {
            register_btn.innerHTML = "<i class='fa fa-cog fa-spin'></i>"
            register_btn.disabled = true
            register_event()
        } else {
            register_btn.innerHTML = "<i class='fa fa-cog fa-spin'></i>"
            register_btn.disabled = true
            deregister_event()
        }

    })
}

register_event = () => {
    fetch(`/startups/register/${register_btn.dataset.sid}/`)
        .then(d => {
            update_color()
            register_btn.disabled = false
            return d.json()
        })
        .then(d => {
            if (d.success) {
                register_btn.disabled = false
                regsitered_startups.push(register_btn.dataset.sid)
                update_color()
            } else {
                alert(d.message ? d.message : "something went wrong")
            }
        })
        .catch(err => {
            console.error(err)
        })
}

deregister_event = () => {
    fetch(`/startups/unregister/${register_btn.dataset.sid}/`)
        .then(d => {
            update_color()
            register_btn.disabled = false
            return d.json()
        })
        .then(d => {
            if (d.success) {
                register_btn.disabled = false
                regsitered_startups.splice(
                    regsitered_startups.indexOf(
                        register_btn.dataset.sid
                    ),1
                )
                update_color()
            } else {
                alert(d.message ? d.message : "something went wrong")
            }
        })
        .catch(err => {
            console.error(err)
        })
}
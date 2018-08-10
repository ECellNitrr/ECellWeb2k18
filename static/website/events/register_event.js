
register_stuff = (data) => {
    var rbtns = document.querySelectorAll('.register_btn')
    // color based on event registration
    color_based_on_previous_reg(data)
    // attach event listeners
    rbtns.forEach(btn => {
        btn.addEventListener('click', (e) => {
            e.preventDefault()
            console.log('register event clicked')

            var eid = btn.getAttribute('data-eid')

            if (localStorage.ecell_nitrr_user) {
                btn.innerHTML = '<i class="fa fa-1x fa-spinner fa-spin"></i>'
                if (localStorage[localStorage.ecell_nitrr_user + eid]) {
                    console.log('giveup event')
                    giveup_event(eid, btn)
                } else {
                    console.log('register event')
                    register_event(eid, btn)
                }
            } else {
                alert('plz login to access this feature')
                return
            }
        })
    })
}

register_event = (eid, btn) => {
    fetch('/add/' + eid)
        .then(data => data.json())
        .then(data => {
            if (data.success) {
                console.log(data, 'success event r')
                localStorage[localStorage.ecell_nitrr_user + eid] = true

                btn.innerText = 'Registered'
                btn.style.border = '2px solid green'
                btn.style.background = 'green'
                btn.style.color = 'white'
                btn.style.boxShadow = '0 0 25px green'
            } else {
                btn.innerText = 'err plz retry'
                console.log(data, 'retry')
            }
        })
        .catch(e => {
            btn.innerText = 'err plz retry'
            console.error(e)
        })
}

giveup_event = (eid, btn) => {
    fetch('/remove/' + eid)
        .then(data => data.json())
        .then(data => {
            if (data.success) {
                console.log(data, 'success event giveup')
                localStorage[localStorage.ecell_nitrr_user + eid] = false

                btn.innerText = 'Register'
                btn.style.border = '2px solid black'
                btn.style.background = 'transparent'
                btn.style.color = 'black'
                btn.style.boxShadow = '0'
            } else {
                btn.innerText = 'err plz retry'
                console.log(data, 'retry')
            }
        })
        .catch(e => {
            btn.innerText = 'err plz retry'
            console.error(e)
        })
}

color_based_on_previous_reg = (eventshtml) => {
    console.log('color_based_on_previous_reg')
    // getting list of registered events
    fetch('/cart/')
        .then(data => data.json())
        .then(data => {
            console.log(data)
            data.events.forEach(re=> {
                // finding id for the registered event
                var re_id = eventshtml.Events.find(e=> e.name==re)
                // finding the re_btn with the id found
                var re_btn = document.querySelector(`[data-eid='${re_id.id}']`) 
                console.log(re_btn)
                
                re_btn.innerText = 'Registered'
                re_btn.style.border = '2px solid green'
                re_btn.style.background = 'green'
                re_btn.style.color = 'white'
                re_btn.style.boxShadow = '0 0 25px green'
            })
        })
        .catch(e => console.error(e))

}
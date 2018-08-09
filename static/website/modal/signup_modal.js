// close signup modal
signup_modal_close_btn.addEventListener('click', (e) => {
    e.preventDefault()

    body.style['overflow'] = 'none'
    body.style.height = 'auto'
    signup_modal.style.top = '-100vh'
})

// alternative
s2l_btn.addEventListener('click', (e) => {
    e.preventDefault()

    // hide other models
    modal_bg.forEach(m => m.style.top = "-100vh")
    // show signup model
    login_modal.style.top = 0
})

// show signup modal
signup_trigger.addEventListener('click', (e) => {
    e.preventDefault()
    console.log('signup triggered')
    // hide other models
    modal_bg.forEach(m=> m.style.top="-100vh")
    // show the model
    body.style['overflow'] = 'hidden'
    body.style.height = '100vh'
    signup_modal.style.top = 0
})

// do signup req
signup_btn.addEventListener('click', (e) => {
    e.preventDefault()
    console.log('login req sent')
    commence_signup()
})

commence_signup = () => {
    console.log('fetching user')
    signup_btn.innerHTML = '<i class="fa fa-1x fa-spinner fa-spin"></i>';
    signup_btn.disabled = true

    fetch('/register/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json; charset=utf-8'
        },
        body: JSON.stringify({
            'email': semail.value,
            'password': spassword1.value,
            'contactno': scontactno.value
        })
    })
        .then(response => response.json())
        .then(data => {
            console.log(data)
            signup_btn.disabled = false

            if (data.success) {
                signup_success_handler()
            } else {
                signup_failure_hander()
            }
        })
        .catch(error => console.error('fetch error', error))
}

signup_success_handler = () => {
    body.style['overflow'] = 'none'
    body.style.height = 'auto'
    signup_modal.style.top = '-100vh'
    // change btn text from login to logut
    login_trigger.innerText='logout'
    // store the cookie
    loggedin_user.innerText = semail.value.split('@')[0]
    localStorage.ecell_nitrr_user = semail.value
}

signup_failure_hander = () => {
    modal_h2.innerText = 'plz check the input'
    modal_h2.style.color = 'red'
}
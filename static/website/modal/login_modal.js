// mobile login modal
mlogin_trigger.addEventListener('click', (e) => {
    e.preventDefault()
    // close the god damn menubar in mobile
    close_mobile_menubar()
    // show the mobile login modal 
    show_login_modal(e)
})

// close login modal
login_modal_close_btn.addEventListener('click', (e) => {
    e.preventDefault()

    body.style['overflow'] = 'none'
    body.style.height = 'auto'
    login_modal.style.top = '-200vh'
})

// alternative go to signup
l2s_btn.addEventListener('click', (e) => {
    e.preventDefault()

    // hide other models
    modal_bg.forEach(m => m.style.top = "-200vh")
    // show signup model
    signup_modal.style.top = 0
})

// if the loggedin username is clicked
loggedin_user_box.addEventListener('click', e => {
    show_login_modal(e)
})

// website show login model
wlogin_trigger.addEventListener('click', (e) => {
    show_login_modal(e)
})

// login process
show_login_modal = (e) => {
    e.preventDefault()
    // if logged in show logout modal
    if (localStorage.ecell_nitrr_user) {
        show_logout_modal()
        return
    }
    // hide other models
    modal_bg.forEach(m => m.style.top = "-200vh")
    // show the model

    body.style['overflow'] = 'hidden'
    body.style.height = '100vh'
    login_modal.style.top = 0
}

// do login req
login_btn.addEventListener('click', (e) => {
    e.preventDefault()
    commence_login()
})

commence_login = () => {

    // perform validation
    if (!email_regex.exec(lemail.value)) {
        alert('please enter a proper email')
        return
    }
    if (lpass.value.length < 8) {
        alert('please enter a porper password')
        return
    }

    // after validation
    console.log('login commenced')
    login_btn.innerHTML = '<i class="fa fa-1x fa-spinner fa-spin"></i>';
    // disable login btn to prevent multiple requests
    login_btn.disabled = true

    fetch('/login/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json; charset=utf-8'
        },
        body: JSON.stringify({
            'email': lemail.value,
            'password': lpass.value,
            // 'email': 'mitsum@gmail.com',
            // 'password': 'ldappass',
        })
    })
        .then(response => response.json())
        .then(data => {
            console.log(data)
            login_btn.innerHTML = 'login'
            login_btn.disabled = false

            if (data.success) {
                login_success_handler()
            } else {
                alert(data.message)
            }
        })
        .catch(error => {
            console.error(error)
            // alert('error! please refresh and try again')
        })
}

login_success_handler = () => {
    body.style['overflow'] = 'none'
    body.style.height = 'auto'
    login_modal.style.top = '-200vh'
    // show the loggin username
    loggedin_user.innerText = semail.value.split('@')[0]
    // change btn text from login to logout
    wlogin_trigger.innerText = 'logout'
    mlogin_trigger.innerText = 'logout'
    // store the cookie
    loggedin_user.innerText = lemail.value.split('@')[0]
    localStorage.ecell_nitrr_user = lemail.value
    localStorage.ecell_nitrr_pass = lpass.value
    // enable login btnagain
    login_btn.disabled = false
}

login_failure_hander = () => {
    modal_h2.innerText = 'incorrect email/password'
    modal_h2.style.color = 'red'
    lemail.value = ''
    lpass.value = ''
    lpass.removeAttribute.style
}

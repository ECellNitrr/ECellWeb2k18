var signup_trigger = document.querySelector('#signup_trigger')
var signup_btn = document.querySelector('#signup_btn')
var modal_h2 = document.querySelector('.signup_modal h2')
var body = document.querySelector('body')
var semail = document.querySelector('#semail')
var spassword1 = document.querySelector('#spassword1')
var spassword2 = document.querySelector('#spassword2')
var scontactno = document.querySelector('#scontactno')
var login_modal = document.querySelector('#login_modal')
var signup_modal = document.querySelector('#signup_modal')
var signup_modal_close_btn = document.querySelector('#signup_modal_close_btn')

signup_modal_close_btn.addEventListener('click', (e) => {
    e.preventDefault()

    body.style['overflow'] = 'none'
    body.style.height = 'auto'
    signup_modal.style.top = '-100vh'
})

signup_trigger.addEventListener('click', (e) => {
    e.preventDefault()
    console.log('signup triggered')
    login_modal.style.top = '-100vh'

    body.style['overflow'] = 'hidden'
    body.style.height = '100vh'
    signup_modal.style.top = 0
})

signup_btn.addEventListener('click', (e) => {
    e.preventDefault()
    console.log('do signup req')
    commence_signup()
})

commence_signup = () => {
    console.log('fetching user')
    signup_btn.innerHTML = '<i class="fa fa-2x fa-spinner fa-spin"></i>';
    signup_btn.disabled = true

    fetch('register/', {
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

    login_user.innerText = semail.value.split('@')[0]
    localStorage.ecell_nitrr_user = semail.value
}

signup_failure_hander = () => {
    modal_h2.innerText = 'plz check the input'
    modal_h2.style.color = 'red'
}
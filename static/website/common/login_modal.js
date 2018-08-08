var login_trigger = document.querySelector('#login_trigger')
var login_btn = document.querySelector('#login_btn')
var lemail = document.querySelector('#lemail')
var lpass = document.querySelector('#lpass')
var modal_h2 = document.querySelector('.login_modal h2')
var body = document.querySelector('body')
var login_user = document.querySelector('#login_user span')
var signup_modal = document.querySelector('#signup_modal')
var login_modal = document.querySelector('#login_modal')
var login_modal_close_btn = document.querySelector('#login_modal_close_btn')


login_modal_close_btn.addEventListener('click', (e) => {
    e.preventDefault()

    body.style['overflow'] = 'none'
    body.style.height = 'auto'
    login_modal.style.top = '-100vh'
})

login_trigger.addEventListener('click', (e) => {
    e.preventDefault()
    signup_modal.style.top = '-100vh'

    body.style['overflow'] = 'hidden'
    body.style.height = '100vh'
    login_modal.style.top = 0
})

login_btn.addEventListener('click', (e) => {
    e.preventDefault()
    commence_login()
})

commence_login = () => {
    console.log('fetching user')
    console.log(lemail.value, lpass.value)
    login_btn.innerHTML = '<i class="fa fa-2x fa-spinner fa-spin"></i>';
    login_btn.disabled = true

    fetch('login/', {
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
            login_btn.innerHTML = 'login'
            login_btn.disabled = false

            if (data.success) {
                login_success_handler()
            } else {
                login_failure_hander()
            }
        })
        .catch(error => console.error('fetch error', error))
}

login_success_handler = () => {
    body.style['overflow'] = 'none'
    body.style.height = 'auto'
    login_modal.style.top = '-100vh'

    login_user.innerText = lemail.value.split('@')[0]
    localStorage.ecell_nitrr_user = lemail.value
}

login_failure_hander = () => {
    modal_h2.innerText = 'incorrect email/password'
    modal_h2.style.color = 'red'
    lemail.value = ''
    lpass.value = ''
    lpass.removeAttribute.style
}


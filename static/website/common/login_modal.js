var login_trigger = document.querySelector('#login_trigger')
var login_btn = document.querySelector('#login_btn')
var lemail = document.querySelector('#lemail')
var lpass = document.querySelector('#lpass')
var center_the_modal = document.querySelector('.center_the_modal')
var modal_h2 = document.querySelector('.center_the_modal h2')
var body = document.querySelector('body')

login_trigger.addEventListener('click', (e) => {
    e.preventDefault()
    body.style['overflow'] = 'hidden'
    body.style.height = '100vh'
    center_the_modal.style.top = 0
})

login_btn.addEventListener('click', (e) => {
    e.preventDefault()
    commence_login()
})

commence_login = () => {
    console.log('fetching user')
    console.log(lemail.value, lpass.value)
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
            if (data.success) {
                login_success_handler()
            } else {
                login_failure_hander()
            }
        })
        .catch(error => console.error('fetch error', error))

}

login_success_handler = () => {
    login_btn.innerText = 'success'
    login_btn.style.background = 'green'
    body.style['overflow'] = 'none'
    body.style.height = 'auto'
    setTimeout(() => {
        center_the_modal.style.top = '-100vh'
    }, 1000)
}

login_failure_hander = () => {
    modal_h2.innerText = 'incorrect email/password'
    modal_h2.style.color = 'red'
    lemail.style.border = '2px solid red'
    lpass.style.border = '2px solid red'
    lemail.value = ''
    lpass.value = ''
    lpass.removeAttribute.style
}


var login_trigger = document.querySelector('#login_trigger')
var login_btn = document.querySelector('#login_btn')
var lemail = document.querySelector('#lemail')
var lpass = document.querySelector('#lpass')
var center_the_modal = document.querySelector('.center_the_modal')

login_btn.addEventListener('click', (e) => {
    e.preventDefault()
    commence_login()
})

login_trigger.addEventListener('click', (e) => {
    e.preventDefault()
    center_the_modal.style.top = 0
})

commence_login = () => {
    console.log('fetching user')
    console.log(lemail.value,lpass.value)
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
            if (data.success){
                login_success_handler()
            } else {
                login_failure_hander()
            }
        })
        .catch(error => console.error('fetch error', error))

}

login_success_handler = () => {
    center_the_modal.style.top = '-100vh'
}

login_failure_hander = () => {
    console.log('failure')
}
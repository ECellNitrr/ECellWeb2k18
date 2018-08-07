login_modal = () => {
    var lemail = document.querySelector('#lemail')
    var lpass = document.querySelector('#lpass')
    // var lcsrf = document.querySelector('#login_modal [name=csrfmiddlewaretoken]')

    console.log('fetching user')
    fetch('login/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json; charset=utf-8'
        },
        body: JSON.stringify({
            // 'email': lemail.value,
            // 'password': lpass.value,
            'email': 'mitsum@gmail.com',
            'password': 'ldappass',
        })
    })
        .then(response => response.json())
        .then(data => {
            console.log(data)
        })
        .catch(error => console.error('fetch error', error))

}

login_modal()
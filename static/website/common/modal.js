login_modal = () => {
    var lemail = document.querySelector('#lemail')
    var lpass = document.querySelector('#lpass')
    var lcsrf = document.querySelector('#login_modal [name=csrfmiddlewaretoken]')

    fetch('message/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json; charset=utf-8',
            "X-CSRFToken": lcsrf.value
        },
        body: JSON.stringify({
            // 'email': lemail.value,
            // 'password': lpass.value,
            'email': 'naveennvrgu',
            'password': ,
        })
    })
        .then(response => response.json())
        .then(data => {
            console.log(data)
        })
        .catch(error => console.error('fetch error', error))

    console.log(lpass, lemail)
}

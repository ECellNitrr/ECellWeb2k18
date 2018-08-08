var cover = document.querySelector('.cover');
var header = document.querySelector('header');
var innerHeight = Number(window.innerHeight);
var innerWidth = Number(window.innerWidth);


if (innerWidth < 700) {
    if (innerHeight > 550) {
        innerHeight = 550;
    }
}

// console.log(innerHeight);

header.style.height = `${innerHeight}px`;
cover.style.height = `${innerHeight}px`;

// send user's message to backend

submit_btn.addEventListener('click', (e) => {
    e.preventDefault()

    var submit_btn = document.querySelector("#submit_btn")
    var name = document.querySelector('#username')
    var email = document.querySelector('input[name=email]')
    var msg = document.querySelector('textarea[name=msg]')
    var csrf = document.querySelector('input[name=csrfmiddlewaretoken]')

    console.log('testing fetch')
    submit_btn.innerHTML = '<i class="fa fa-2x fa-spinner fa-spin"></i>'
    submit_btn.style.width = '75px'
    submit_btn.style.borderRadius = '10px'
    submit_btn.disabled = true

    fetch('message/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json; charset=utf-8',
            "X-CSRFToken": csrf.value
        },
        body: JSON.stringify({
            'name': name.value,
            'email': email.value,
            'msg': msg.value,
        })
    })
        .then(response => response.json())
        .then(data => {
            console.log(data)

            name.value=''
            email.value=''
            msg.value=''

            // style the button
            submit_btn.disabled = false
            TweenMax.to("#submit_btn", 1, {
                width: 'auto',
                borderRadius: 0,
                background: 'green',
                boxShadow: '0 0 30px green'
            });
            setTimeout(() => {
            submit_btn.innerHTML = 'successfully submitted'
            },500)
        })
        .catch(error => console.error('fetch error', error))
})
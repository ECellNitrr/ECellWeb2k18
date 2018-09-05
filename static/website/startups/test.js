console.log('testing')

fetch('/loginweb/', {
    'method': 'POST',
    body: JSON.stringify({
        "email": "pupale@gmail.com",
        "password": "jervismk2"
    })
})
    .then(d => d.json())
    .then(d => {
        console.log(d)
        register()

    })
    .catch(err => console.error(err))

register = () => {
    fetch('/startups/register/3/')
        .then(d => d.json())
        .then(d => {
            console.log(d)
        })
        .catch(err => console.error(err))
}
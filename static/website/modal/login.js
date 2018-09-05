var login_btn = document.querySelector('#login_btn')
var logout_bnt = document.querySelector('#logout_bnt')

// login form data
var l_email = document.querySelector('#l_email')
var l_p1 = document.querySelector('#l_p1')

login_btn.addEventListener('click', (e) => {
    e.preventDefault()
    signup_btn.innerHTML = '<i class="fa fa-cog fa-spin"></i>'

    fetch("/loginweb/", {
        method: 'post',
        body: JSON.stringify({
            email: l_email.value,
            password: l_p1.value
        })
    })
        .then(d => {
            signup_btn.innerHTML = 'Login'
            return d.json()
        })
        .then(d => {
            console.log(d)
            if (d.success) {
                user.innerText = "@" + l_email.value.split('@')[0]
                m_basic.forEach(div => div.classList.remove('show'))
            } else {
                alert(d.message ? d.message: "something went wrong")
            }
        })
        .catch(err => {
            console.error(err)
        })
})
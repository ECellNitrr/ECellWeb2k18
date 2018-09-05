var login_btn = document.querySelector('#login_btn')
var logout_btn = document.querySelector('#logout_btn')

// logout action
logout_btn.addEventListener('click', (e) => {
    e.preventDefault()
    user.innerText = 'Login/Signup'
})

// login form data
var l_email = document.querySelector('#l_email')
var l_p1 = document.querySelector('#l_p1')

login_btn.addEventListener('click', (e) => {
    e.preventDefault()
    signup_btn.innerHTML = '<i class="fa fa-cog fa-spin"></i>'

    fetch("/loginweb/", {
        method: 'POST',
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
                user.innerText = "#" + l_email.value.split('@')[0]
                close_modals()

                o_cont.classList.add('show')
            } else {
                alert(d.message ? d.message: "something went wrong")
            }
        })
        .catch(err => {
            console.error(err)
        })
})

// verify otp
verify_btn.addEventListener('click', (e) => {
    e.preventDefault()
    verify_btn.innerHTML = '<i class="fa fa-cog fa-spin"></i>'

    fetch("/web_verify_otp/", {
        method: 'POST',
        body: JSON.stringify({
            otp: o_otp.value,
        })
    })
        .then(d => {
            verify_btn.innerHTML = 'Verify OTP'
            return d.json()
        })
        .then(d => {
            console.log(d)
            if (d.success) {
                close_modals()
                user.innerText = "@" + l_email.value.split('@')[0]
                alert('You have successfully verified the OTP')
            } else {
                alert(d.message ? d.message: "something went wrong")
            }
        })
        .catch(err => {
            console.error(err)
        })
})


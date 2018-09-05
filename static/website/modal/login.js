var login_btn = document.querySelector('#login_btn')
var logout_btn = document.querySelector('#logout_btn')

// logout action
logout_btn.addEventListener('click', (e) => {
    e.preventDefault()
    close_modals()
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
            if (d.success && d.status) {
                // if otp verification is done close all modals
                sessionStorage.user = "@" + l_email.value.split('@')[0]
                user.innerText = sessionStorage.user
                close_modals()
            } else if (d.success && !d.status) {
                // if the otp verification is not done show otp modal
                sessionStorage.user = "#" + l_email.value.split('@')[0]
                user.innerText = sessionStorage.user

                close_modals()
                o_cont.classList.add('show')
            } else {
                alert(d.message ? d.message : "something went wrong")
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

                sessionStorage.user = "@" + l_email.value.split('@')[0]
                user.innerText = sessionStorage.user
            } else {
                alert(d.message ? d.message : "something went wrong")
            }
        })
        .catch(err => {
            console.error(err)
        })
})

// incorrect phno case
var ic_phno = document.querySelector('#ic_phno')

ic_phno.addEventListener('click', (e) => {
    e.preventDefault()
    var new_phno = prompt('Please enter the correct phone no:')
    if(!cno_regex.test(new_phno)){
        alert("please try again with proper phno")
        return false
    }
    verify_btn.innerHTML = '<i class="fa fa-cog fa-spin"></i>'

    fetch('/new_conno/', {
        method: 'post',
        body: JSON.stringify({
            contact_no: new_phno
        })
    })
        .then(d => {
            verify_btn.innerHTML = 'Verify OTP'
            return d.json()
        })
        .then(d => {
            console.log(d)
        })
        .catch(err => {
            console.error(err)
        })
})

// resend otp case
var rs_otp = document.querySelector('#rs_otp')

rs_otp.addEventListener('click', (e) => {
    e.preventDefault()
    verify_btn.innerHTML = '<i class="fa fa-cog fa-spin"></i>'

    fetch('/resend_otp/')
        .then(d => {
            verify_btn.innerHTML = 'Verify OTP'
            return d.json()
        })
        .then(d => {
            console.log(d)
        })
        .catch(err => {
            console.error(err)
        })
})
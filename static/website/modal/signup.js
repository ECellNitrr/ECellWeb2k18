var signup_btn = document.querySelector('#signup_btn')
var verify_btn = document.querySelector('#verify_btn')

// signup form data
var s_name = document.querySelector('#s_name')
var s_email = document.querySelector('#s_email')
var s_cno = document.querySelector('#s_cno')
var s_p1 = document.querySelector('#s_p1')
var s_p2 = document.querySelector('#s_p2')

var o_otp = document.querySelector('#o_otp')

signup_btn.addEventListener('click', (e) => {
    e.preventDefault()
    signup_btn.innerHTML = '<i class="fa fa-cog fa-spin"></i>'

    fetch("/register/", {
        method: 'POST',
        body: JSON.stringify({
            email: s_email.value,
            password: s_p1.value,
            contact_no: s_cno.value
        })
    })
        .then(d => {
            signup_btn.innerHTML = 'Signup'
            return d.json()
        })
        .then(d => {
            console.log(d)
            if (d.success) {
                m_basic.forEach(div => div.classList.remove('show'))
                o_cont.classList.add('show')
            } else {
                alert(d.message ? d.message: "something went wrong")
            }
        })
        .catch(err => {
            console.error(err)
        })
})

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
                m_basic.forEach(div => div.classList.remove('show'))
                alert('You have successfully completed the signup process. Please proceed to login!')
            } else {
                alert(d.message ? d.message: "something went wrong")
            }
        })
        .catch(err => {
            console.error(err)
        })
})


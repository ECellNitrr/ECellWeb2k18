var forget_password = document.querySelector('#to_forget_password')
var fg_email = document.querySelector('#fg_email')
var fg_otp = document.querySelector('#fg_otp')
var fg_newpas = document.querySelector('#fg_new_pas')
var fg_getotp_btn = document.querySelector('#fg_getotp_btn')
var fg_verifyotp_btn = document.querySelector('#fg_verify_btn')


fg_getotp_btn.addEventListener('click', (e) => {
    e.preventDefault()

    fg_getotp_btn.innerHTML = '<i class="fa fa-cog fa-spin"></i>'
    fg_getotp_btn.disabled = true


    fetch('/forget_password_send_otp/', {
        method: 'post',
        body: JSON.stringify({
            email: fg_email.value
        })
    })
        .then(d => {
            return d.json()
        })
        .then(d => {
            alert(d['msg'])
            console.log(d)
        })
        .catch(err => {
            alert(err)
            console.error(err)
        })
        .finally(() => {
            fg_getotp_btn.innerHTML = 'Get OTP'
            fg_getotp_btn.disabled = false        
        })
})

fg_verifyotp_btn.addEventListener('click', (e) => {
    e.preventDefault()

    fg_verifyotp_btn.innerHTML = '<i class="fa fa-cog fa-spin"></i>'
    fg_verifyotp_btn.disabled = true

    fetch('/forget_password_verify_otp/', {
        method: 'post',
        body: JSON.stringify({
            email: fg_email.value,
            password: fg_newpas.value,
            otp: fg_otp.value
        })
    })
        .then(d => {
            return d.json()
        })
        .then(d => {
            alert(d['msg'])
            console.log(d)
        })
        .catch(err => {
            alert(err)
            console.error(err)
        })
        .finally(()=>{
            fg_verifyotp_btn.innerHTML = 'Change Password'
            fg_verifyotp_btn.disabled = false    
            close_modals()
        })
})
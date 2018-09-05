var signup_btn = document.querySelector('#signup_btn')

// signup form data
var s_name = document.querySelector('#s_name')
var s_email = document.querySelector('#s_email')
var s_cno = document.querySelector('#s_cno')
var s_p1 = document.querySelector('#s_p1')
var s_p2 = document.querySelector('#s_p2')

signup_btn.addEventListener('click', (e) => {
    e.preventDefault()
    signup_btn.innerHTML = '<i class="fa fa-cog fa-spin"></i>'

    fetch("/register/", {
        method: 'post',
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
                user.innerText = "@" + s_email.value.split('@')[0]
                m_basic.forEach(div => div.classList.remove('show'))
            } else {
                alert(d.message ? d.message: "something went wrong")
            }
        })
        .catch(err => {
            console.error(err)
        })

})
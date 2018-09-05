var user = document.querySelector('#loggedin_user')

// core models stuff
var m_basic = document.querySelectorAll('.m_basic')
var l_cont = document.querySelector('#l_cont')
var s_cont = document.querySelector('#s_cont')
var x_cont = document.querySelector('#x_cont') 

// extras
var covers = document.querySelectorAll('.cover')
var close_btns = document.querySelectorAll('.close_btn')

// alts
var to_signup = document.querySelector('#to_signup')
var to_login = document.querySelector('#to_login')

// clicking on loggedin_user unveils the modal
user.addEventListener('click', (e) => {
    e.preventDefault()

    console.log('show', user.innerHTML.toLowerCase())
    if (user.innerHTML.toLowerCase() == 'login/signup') {
        s_cont.classList.add('show')
    } else {
        x_cont.classList.add('show')
    }
})

// clicking on close btn closes modal
close_btns.forEach((btn) => {
    btn.addEventListener('click', (e) => {
        e.preventDefault()
        m_basic.forEach(div => div.classList.remove('show'))
    })
})

// clicking on cover closes modal
covers.forEach((cover) => {
    cover.addEventListener('click', (e) => {
        e.preventDefault()
        m_basic.forEach(div => div.classList.remove('show'))
    })
})

// alternatives
to_signup.addEventListener('click', (e) => {
    e.preventDefault()
    m_basic.forEach(div => div.classList.remove('show'))
    s_cont.classList.add('show')
})
to_login.addEventListener('click', (e) => {
    e.preventDefault()
    m_basic.forEach(div => div.classList.remove('show'))
    l_cont.classList.add('show')
})
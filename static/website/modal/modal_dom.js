// trigger
var wlogin_trigger = document.querySelector('#wlogin_trigger')
var wsignup_trigger = document.querySelector('#wsignup_trigger')

var mlogin_trigger = document.querySelector('#mlogin_trigger')
var msignup_trigger = document.querySelector('#msignup_trigger')
// btn to send the ajax request
var login_btn = document.querySelector('#login_btn')
var signup_btn = document.querySelector('#signup_btn')
var logout_btn = document.querySelector('#logout_btn')
// details
var lemail = document.querySelector('#lemail')
var lpass = document.querySelector('#lpass')

var semail = document.querySelector('#semail')
var spassword1 = document.querySelector('#spassword1')
var spassword2 = document.querySelector('#spassword2')
var scontactno = document.querySelector('#scontactno')
// modal html
var login_modal = document.querySelector('#login_modal')
var signup_modal = document.querySelector('#signup_modal')
var logout_modal = document.querySelector('#logout_modal')
// modal h2
var modal_h2 = document.querySelector('.login_modal h2')
// respective modal close btn
var login_modal_close_btn = document.querySelector('#login_modal .close_btn')
var signup_modal_close_btn = document.querySelector('#signup_modal .close_btn')
var logout_modal_close_btn = document.querySelector('#logout_modal .close_btn')
// login vs signup
var l2s_btn = document.querySelector('#login_modal .alternative_btn')
var s2l_btn = document.querySelector('#signup_modal .alternative_btn')
// menubar
let menuTrigger = document.querySelector('.menu-trigger');
let menubar = document.querySelector('.menubar');
// miscellaneous
var body = document.querySelector('body')
var loggedin_user = document.querySelector('#loggedin_user span') // used to show the logged in user
var loggedin_user_box = document.querySelector('#loggedin_user')
var modal_bg = document.querySelectorAll('.center_the_modal')
var user_modal = document.querySelector('.user_modal')


// validation
var email_regex = /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$/
var phno_regex = /^[0-9]{10}$/

// click on modal_bg to disable disable the modal
modal_bg.forEach(bg => bg.addEventListener('click', (e) => {
    if (e.target != bg) {
        return
    }
    // hide other models
    modal_bg.forEach(m => m.style.top = "-200vh")
    // show the model
    body.style['overflow'] = 'none'
    body.style.height = 'auto'
}))

// close mobile menubar
close_mobile_menubar = () => {
    menubar.style.display = 'none'
    menuTrigger.classList.remove('menu-close')
    loggedin_user_box.style.display = 'none'
}
// trigger
var login_trigger = document.querySelector('#login_trigger')
var signup_trigger = document.querySelector('#signup_trigger')
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
var modal_h2 = document.querySelector('.signup_modal h2')
// respective modal close btn
var login_modal_close_btn = document.querySelector('#login_modal .close_btn')
var signup_modal_close_btn = document.querySelector('#signup_modal .close_btn')
var logout_modal_close_btn = document.querySelector('#logout_modal .close_btn')

// miscellaneous
var body = document.querySelector('body')
var login_user = document.querySelector('#login_user span') // used to show the logged in user
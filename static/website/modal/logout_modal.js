show_logout_modal = () => {
    // hide other modals
    modal_bg.forEach(m=> m.style.top="-100vh")    
    // show modal
    logout_modal.style.top = 0
    body.style.overflow = 'hidden'
    body.style.height = '100vh'
}

logout_btn.addEventListener('click', (e) => {
    e.preventDefault()
    console.log('perform logout')

    localStorage.removeItem('ecell_nitrr_user')
    loggedin_user.innerText = 'Anonymous'
    // change logout to login in btn
    wlogin_trigger.innerText='login'
    // hide the modal
    logout_modal.style.top = '-100vh'
    body.style.overflow = 'none'
    body.style.height = 'auto'
})

logout_modal_close_btn.addEventListener('click', (e) => {
    e.preventDefault()

    // hide the modal
    logout_modal.style.top = '-100vh'
    body.style.overflow = 'none'
    body.style.height = 'auto'
})

logout_modal.style.top=0
body.style.overflow='hidden'
body.style.height='100vh'

logout_btn.addEventListener('click', (e) => {
    e.preventDefault()
    console.log('perform logout')
})

logout_modal_close_btn.addEventListener('click', (e) => {
    e.preventDefault()
    console.log('close the logout model')
})

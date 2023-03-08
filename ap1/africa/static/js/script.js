const buttonMenu = document.querySelector('.button')
const navbar = document.querySelector('.container-header-navbar')

console.log(navbar)

buttonMenu.addEventListener('click', () =>{
    if(navbar.classList.contains('active')){
        buttonMenu.innerHTML = 'menu'
        navbar.classList.remove('active')
    }else{
        navbar.classList.add('active')
        buttonMenu.innerHTML = 'close'
    }
})
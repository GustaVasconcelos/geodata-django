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

let count = 1
document.getElementById('radio1').checked = true

setInterval(() =>{
    nextImage()
},3500)


const nextImage = () =>{
    count++
    if(count>4){
        count = 1
    }

    document.getElementById('radio'+count).checked = true
}
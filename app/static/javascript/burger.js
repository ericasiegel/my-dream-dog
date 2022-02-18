let burger = document.querySelector('.burger')
let menu = document.querySelector('#navbarMenuHeroA')

function burger_menu () {
    burger.classList.toggle('is-active');
    menu.classList.toggle('is-active')
}

burger.addEventListener('click', burger_menu)
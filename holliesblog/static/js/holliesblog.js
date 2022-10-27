

const navBtn = document.querySelector('.nav-btn');
const mobNav = document.querySelector('.mobile-nav');
let navOpen = false;

navBtn.addEventListener('click', () => {

    if (!navOpen) {
        navBtn.classList.add('open');
        mobNav.classList.add('open');
        navOpen = true;
    }
    else {
        navBtn.classList.remove('open');
        mobNav.classList.remove('open');
        navOpen = false;
    }
})



const point = document.querySelector('#user_profile');

const card = document.querySelector('.User_profile');

point.addEventListener('mouseenter', e => {
    if(e){
        card.classList.add('showUser');
    }
})


document.addEventListener('click', e => {
    if (e.target.closest('.User_profile') || e.target.closest('.user') || e.target.closest('#user_profile')) {
        card.classList.add('showUser');
    }else {
        card.classList.remove('showUser');
    }
})

document.addEventListener('keydown', e => {
    if (e.key === 'Escape') {
        card.classList.remove('showUser');
    }
})
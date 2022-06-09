const show_password = document.querySelector('.show_password')
const new_password = document.querySelector('#new_password');

const btn = document.querySelector('#newPic');
const info = document.querySelector('#change_info');
const renew = document.querySelector('#renew');

const newSlide = document.querySelector('.card')
const form = document.querySelector('.change_info');
const form_password = document.querySelector('.change_password')

const label = btn.nextElementSibling;

const confirmed = document.querySelector('.load_btn');
const accept = document.getElementById('submit_password');

const cancel = document.querySelector('.load_btn_cancel');
const nochange = document.querySelector('#back');
const no_re = document.querySelector('#no_re');

confirmed.style.display = "none";
cancel.style.display = "none";
form.style.display = "none";
form_password.style.display = "none";

btn.addEventListener('change', e => {
    if (e){
        label.style.display = "none";
        confirmed.style.display = "";
        cancel.style.display = "";
    }
});

cancel.addEventListener('click', e => {
    if (e){
        label.style.display = "";
        confirmed.style.display = "none";
        cancel.style.display = "none";
    }
});

confirmed.addEventListener('click', e => {
    if (e){
        label.style.display = "";
        confirmed.style.display = "none";
        cancel.style.display = "none";
    }
});

info.addEventListener('click', e => {
    if(e){
        newSlide.style.display = "none";
        form_password.style.display = "none";
        form.style.display = "";

    }
});

nochange.addEventListener('click', e => {
    if(e){
        newSlide.style.display = "";
        form.style.display = "none";
    }
});

renew.addEventListener('click', e => {
    if(e){
        newSlide.style.display = "none";
        form.style.display = "none";
        form_password.style.display = "";
    }
})

const check_password = new_password.parentNode.previousElementSibling;
let compaire = check_password.children;

compaire[1].addEventListener('keyup', e => {
    if(e){

        let before = compaire[1].value
        let after = new_password.value
        
        let message = new_password.nextElementSibling;

        if (before != after){
            accept.disabled = true;
            accept.style.filter = "grayscale(50%)";
            message.innerHTML = "Password must match!";
            message.style.color = "#ff4e00";
        }else {
            console.log(before + after)
            accept.disabled = false;
            accept.style.filter = "grayscale(0%)";
            message.innerHTML = "Password is match!";
            message.style.color = "green";
        }
    }
})

new_password.addEventListener('keyup',e => {
    if(e){

        let before = compaire[1].value
        let after = new_password.value
        
        let message = new_password.nextElementSibling;

        if (before != after){
            accept.disabled = true;
            accept.style.filter = "grayscale(50%)";
            message.innerHTML = "Password must match!";
            message.style.color = "#ff4e00";
        }else {
            console.log(before + after)
            accept.disabled = false;
            accept.style.filter = "grayscale(0%)";
            message.innerHTML = "Password is match!";
            message.style.color = "green";
        }
    }
})

const eye = show_password.previousElementSibling;
eye.addEventListener('click', e => {
    if(e){
        const check_password = new_password.parentNode.previousElementSibling;
        let compaire = check_password.children;
        if(show_password.style.display == "none"){
            show_password.style.display = "";
            compaire[1].type = "password"
            new_password.type = "password"
        }else{
            show_password.style.display = "none";
            compaire[1].type = "text"
            new_password.type = "text"
        }
    }
})

no_re.addEventListener('click', e => {
    if(e){
        newSlide.style.display = "";
        form_password.style.display = "none";
    }
});

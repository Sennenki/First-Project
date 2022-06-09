const show_password = document.querySelector('.show_password')
const check_password = document.querySelector('#set_password')
const new_password = document.querySelector('#new_password');
const message = document.querySelector('.guide');
const accept = document.querySelector('.login_button');

const eye = show_password.previousElementSibling;

check_password.addEventListener('keyup', e => {
    if(e){

        let before = check_password.value
        let after = new_password.value
        
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

        let before = check_password.value
        let after = new_password.value
        
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
eye.addEventListener('click', e => {
    if(e){
        if(show_password.style.display == "none"){
            show_password.style.display = "";
            check_password.type = "password"
            new_password.type = "password"
        }else{
            show_password.style.display = "none";
            check_password.type = "text"
            new_password.type = "text"
        }
    }
})
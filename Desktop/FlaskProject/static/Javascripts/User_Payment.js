const payInfo = document.querySelector('#payInfo');
const payEmail = document.querySelector('#payEmail');
const payPhone = document.querySelector('#payPhone');

const showInfo = payInfo.nextElementSibling;
const showEmail = payEmail.nextElementSibling;
const showPhone = payPhone.nextElementSibling;

showInfo.value = payInfo.innerHTML;
showEmail.value = payEmail.innerHTML;
showPhone.value = payPhone.innerHTML;

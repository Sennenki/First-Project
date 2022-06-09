const subTotalPrice = document.querySelectorAll('.col_five');
const amount = document.querySelectorAll('.col_four');
let total = 0

for (let i = 0 ; i < subTotalPrice.length ; i++) {
    let num = parseInt(subTotalPrice[i].textContent);
    let coef = parseInt(amount[i].textContent);
    let newPrice = coef * num;

    subTotalPrice[i].innerHTML = newPrice + " THB";

    total = total + newPrice 
} 

total = total + 100 

const sum = document.getElementById('sumAll');

sum.innerHTML =  "TOTAL " + total + " THB";
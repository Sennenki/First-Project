const subTotalPrice = document.querySelectorAll('#result');
const btn = document.querySelector('.btn_payment');
let total = 0

for (let i = 0 ; i < subTotalPrice.length ; i++) {
    let num = parseInt(subTotalPrice[i].textContent);
    total = total + num
} 

const postPrice = document.getElementById('all_price');
postPrice.innerHTML= total + ' THB';

const shipping = document.getElementById('shipping_price');

const all_total_price = document.getElementById('amount_price');

let sum = +total + +parseInt(shipping.textContent);
all_total_price.innerHTML = sum;


const container = document.querySelector('.list_item');

container.addEventListener('click', e => {
    if (e.target.closest('#remove')) {

        const removeItem = e.target.closest('#remove');
        const input = removeItem.parentNode.nextElementSibling;
        const priceThisItem = removeItem.parentNode.previousElementSibling;
        const price = parseInt(priceThisItem.textContent);
        const totalPrice = removeItem.parentNode.nextElementSibling;
    
        const quantityToRemove = removeItem.nextElementSibling.value;
        let decrease = quantityToRemove - 1;
        
        if (decrease < 0) {
            decrease = 0;
        }
        else {
            input.value = decrease;
        }

        let newPrice = price * input.value;
        totalPrice.textContent = newPrice + " THB";

        let newTotal = 0;
        for (let i = 0 ; i < subTotalPrice.length ; i++) {
            let num = parseInt(subTotalPrice[i].textContent);
            newTotal = newTotal + num
        } 

        postPrice.innerHTML= newTotal + ' THB';

        let sum = +newTotal + +parseInt(shipping.textContent);
        all_total_price.innerHTML = sum;

        if (parseInt(all_total_price.textContent) <= '100') {
            btn.disabled = true;
            btn.classList.add('lock')
        }else {
            btn.disabled = false;
            btn.classList.remove('lock')
        }

    }
    
    else if (e.target.closest('#more')) {


        const addItem = e.target.closest('#more');
        const input = addItem.previousElementSibling;
        const priceThisItem = addItem.parentNode.previousElementSibling;
        const price = parseInt(priceThisItem.textContent);
        const totalPrice = addItem.parentNode.nextElementSibling;

        const quantityToAdd = addItem.previousElementSibling.value;
        
        let increse = +quantityToAdd + +1;
        
        input.value = increse;
        
        let newPrice = price * input.value;
        totalPrice.textContent = newPrice + " THB";
        
        let newTotal = 0;
        for (let i = 0 ; i < subTotalPrice.length ; i++) {
            let num = parseInt(subTotalPrice[i].textContent);
            newTotal = newTotal + num
        } 
        
        postPrice.innerHTML= newTotal + ' THB';
        
        let sum = +newTotal + +parseInt(shipping.textContent);
        all_total_price.innerHTML = sum;
        
        if (parseInt(all_total_price.textContent) <= '100') {
            btn.disabled = true;
            btn.classList.add('lock')
        }else {
            btn.disabled = false;
            btn.classList.remove('lock')
        }
    }

})

if (parseInt(all_total_price.textContent) <= '100') {
    btn.disabled = true;
    btn.classList.add('lock')
}else {
    btn.disabled = false;
    btn.classList.remove('lock')
}




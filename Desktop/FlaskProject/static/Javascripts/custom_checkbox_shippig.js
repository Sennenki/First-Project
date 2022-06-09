
    //  calls checked box
    var tax_check = document.getElementById('check_tax');
    var toMe_check = document.getElementById('sendMe');
    var Other_check = document.getElementById('sendYou');
    
    //  set checked box for default unchecked 
    toMe_check.checked = true;
    tax_check.checked = false;
    
    function taxCheck() {
        // Get the checkbox
        var slide_tax = document.getElementById('fill_tax');
        var thenCheckTax = document.getElementById('taxCheck');
        
        // If the checkbox is checked, display the output text
        if (tax_check.checked == true) {
            thenCheckTax.classList.toggle('req_tax');
            slide_tax.classList.toggle('fill_tax')
        }
        else {
            thenCheckTax.classList.remove('req_tax');
            slide_tax.classList.remove('fill_tax')
            tax_check.checked = false;
        }
    }
    
    
    function toMeCheck(){
        // Get the checkbox
        var slide_send_other = document.getElementById('fill_send');
        var iSend = document.getElementById('sendMe');
        var itMe = document.getElementById('checkForMe');
        var itYou = document.getElementById('checkForYou');
        
        // If the checkbox is checked, display the output text
        if (iSend.checked == true) {
            itMe.classList.toggle('send_to_me');
            itYou.classList.remove('send_to_other');
            slide_send_other.classList.remove('fill_send');
            Other_check.checked = false;
        }
        else {
            itMe.classList.remove('send_to_me');
            itYou.classList.toggle('send_to_other');
            slide_send_other.classList.toggle('fill_send');
            Other_check.checked = true;
        }
    }
    
    function toOtherCheck() {
        // Get the checkbox
        var slide_send_other = document.getElementById('fill_send');
        var itMe = document.getElementById('checkForMe');
        var whoSend = document.getElementById('sendYou');
        var itYou = document.getElementById('checkForYou');
    
        // If the checkbox is checked, display the output text
        if (whoSend.checked == true) {
            itYou.classList.toggle('send_to_other');
            slide_send_other.classList.toggle('fill_send');
            itMe.classList.remove('send_to_me');
            toMe_check.checked = false;
        } else {
            itYou.classList.remove('send_to_other');
            slide_send_other.classList.remove('fill_send');
            itMe.classList.toggle('send_to_me');
            toMe_check.checked = true;
        }
    }
    
    function Onchecked() {
        // Get the checkbox
        var checkBox = document.getElementById('check_toggle');
        var new_check = document.getElementById('customCheck');
    
        // If the checkbox is checked, display the output text
        if (checkBox.checked == true) {
            new_check.classList.toggle('active');
        }
        else {
            new_check.classList.remove('active');
        }
        
    } 
    
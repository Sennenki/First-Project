function Onchecked() {
    // Get the checkbox
    const checkBox = document.getElementById('check_toggle');
    const new_check = document.getElementById('customCheck');

    // If the checkbox is checked, display the output text
    if (checkBox.checked == true) {
        new_check.classList.toggle('active');
    }
    else {
        new_check.classList.remove('active');
    }
    
} 

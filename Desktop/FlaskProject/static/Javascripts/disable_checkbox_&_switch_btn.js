// ======================================
//              set variable
// ======================================

// ========= select to checkbox =========
var self_check = document.getElementById('sendMe');
var other_check = document.getElementById('sendYou');
// ======================================
//              set function
// ======================================

// ========= set self checkbox disable to be default =========
self_check.disabled = true;

self_check.onchange = function(){
    if(self_check.checked == true){
        // ========= set self checkbox disable =========
        
        self_check.disabled = true;
        
    }
}

other_check.onchange = function(){
    if(other_check.checked == true){
        // ========= set other checkbox disable =========
        
        self_check.disabled = false;
        
    }
}

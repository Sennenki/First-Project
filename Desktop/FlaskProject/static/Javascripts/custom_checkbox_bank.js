function circleToggle() {
    const boxA = document.getElementById('aCheck');
    const markA = document.getElementById('KTB');
    const boxB = document.getElementById('bCheck');
    const markB = document.getElementById('SCB');
    const boxC = document.getElementById('cCheck');
    const markC = document.getElementById('KSK');
    const boxD = document.getElementById('dCheck');
    const markD = document.getElementById('BBL');

    
    boxA.onchange = function(){
        if (boxA.checked == true) {
            markA.classList.toggle('active');
            markB.classList.remove('active');
            markC.classList.remove('active');
            markD.classList.remove('active');
            boxB.checked = false;
            boxC.checked = false;
            boxD.checked = false;
        }
    
        else {
            markA.classList.remove('active');
            boxA.checked = false;
        }
    }
    boxB.onchange = function(){
        if (boxB.checked == true) {
            markB.classList.toggle('active');
            markA.classList.remove('active');
            markC.classList.remove('active');
            markD.classList.remove('active');
            boxA.checked = false;
            boxC.checked = false;
            boxD.checked = false;
        }
    
        else {
            markB.classList.remove('active');
            boxB.checked = false;
        }
    }
    boxC.onchange = function(){
        if (boxC.checked == true) {
            markC.classList.toggle('active');
            markA.classList.remove('active');
            markB.classList.remove('active');
            markD.classList.remove('active');
            boxB.checked = false;
            boxA.checked = false;
            boxD.checked = false;
        }
    
        else {
            markC.classList.remove('active');
            boxC.checked = false;
        }
    }
    boxD.onchange = function(){
        if (boxD.checked == true) {
            markD.classList.toggle('active');
            markA.classList.remove('active');
            markB.classList.remove('active');
            markC.classList.remove('active');
            boxB.checked = false;
            boxC.checked = false;
            boxA.checked = false;
        }
    
        else {
            markD.classList.remove('active');
            boxD.checked = false;
        }
    }
}

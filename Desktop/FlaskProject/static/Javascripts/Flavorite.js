const heart = document.querySelectorAll(".flavorite");

for(let i = 0 ; i < heart.length ; i++){
    heart[i].style.filter = "grayscale(70%)";
}

heart.forEach(E => {
    E.addEventListener('click', e => {
        if(e){
            let getStyle = E.getAttribute("style").split(";");
            getShade = getStyle[0].split(":");
            if( getShade[0] == "filter"){
                console.log("yes")
                E.style.filter = "";
            }else{
                console.log("no")
                E.style.filter = "grayscale(70%)";
            }
        }
    });
});

const openImg = document.getElementById('viewPic');
const closeImg = document.getElementById('btn-close');
const Img = document.getElementById('fileImg');

openImg.onclick  = function(){
    Img.style.display = "block";
    Img.style.animation = "FadeIn 300ms forwards";
    closeImg.style.display = "block";
    closeImg.style.animation = "FadeIn 300ms forwards";
}


closeImg.onclick  = function(){
    Img.style.display = "none";
    closeImg.style.display = "none";
}


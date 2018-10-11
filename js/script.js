
var modal = document.getElementById('myModal');
var btn = document.getElementById("myBtn");
var btn1 = document.getElementById("myBtn1");
var btn2 = document.getElementById("myBtn2");
var btn3 = document.getElementById("myBtn3");
var btn4 = document.getElementById("myBtn4");
var btn5 = document.getElementById("myBtn5");
var span = document.getElementsByClassName("close")[0];

btn.onclick = function(){
    modal.style.display = "block";
}

btn1.onclick = function(){
    modal.style.display = "block";
}

btn2.onclick = function(){
    modal.style.display = "block";
}

btn3.onclick = function(){
    modal.style.display = "block";
}

btn4.onclick = function(){
    modal.style.display = "block";
}

btn5.onclick = function(){
    modal.style.display = "block";
}

span.onclick = function(){
    modal.style.display = "none";
}

window.onclick = function(event){
    if(event.target == modal){
        modaly.style.display = "none";
    }
}


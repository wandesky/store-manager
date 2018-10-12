var modal = document.getElementById('myModal');
var updateModal = document.getElementById('updateModal');
var deleteModal = document.getElementById('deleteModal');
var updateBtn = document.getElementById("update");

var btn = document.getElementById("myBtn");
var btn1 = document.getElementById("myBtn1");
var btn2 = document.getElementById("myBtn2");
var btn3 = document.getElementById("myBtn3");
var btn4 = document.getElementById("myBtn4");
var btn5 = document.getElementById("myBtn5");

var delbtn1 = document.getElementById("del1");
var delbtn2 = document.getElementById("del2");
var delbtn3 = document.getElementById("del3");
var delbtn4 = document.getElementById("del4");

var span = document.getElementsByClassName("close")[0];

updateBtn.onclick = function(){
    updateModal.style.display = "block";
}

delbtn1.onclick = function(){
    deleteModal.style.display = "block";
}

delbtn2.onclick = function(){
    deleteModal.style.display = "block";
}

delbtn3.onclick = function(){
    deleteModal.style.display = "block";
}

delbtn4.onclick = function(){
    deleteModal.style.display = "block";
}

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

// delbtn1.onclick = function(){
//     modal.style.display = "block";
// }

span.onclick = function(){
    modal.style.display = "none";
}

window.onclick = function(event){
    if(event.target == modal){
        modal.style.display = "none";
    }
}


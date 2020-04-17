function ajaxGetRequest(path, callback) {
    let request = new XMLHttpRequest();
    request.onreadystatechange = function() {
  	  if (this.readyState===4 && this.status ===200) {
	      callback(this.response);
	    }
    }
    request.open("GET", path);
    request.send();
}
function ajaxPostRequest(path, data, callback){
    let request = new XMLHttpRequest();
    request.onreadystatechange = function(){
        if (this.readyState === 4 && this.status === 200){
            callback(this.response);
        }
    };
    request.open("POST", path);
    request.send(data);
}


function submitting(){
  let values = [document.getElementById("name").value,
  document.getElementById("email").value,
  document.getElementById("kage").value,
  document.getElementById("fkids").value,
  document.getElementById("mkids").value,
  document.getElementById("knames").value,
  document.getElementById("location").value,
  document.getElementById("ethnP").value,
  document.getElementById("ethnK").value,
];
console.log(values)
ajaxPostRequest("/trainerdata", JSON.stringify(values),sub);
}

function sub(response){

// window.location.href ="/match";

}




document.getElementById("query").oninput = function(e){
    loadData();
};

function display() {
    var result = document.getElementById("result_area");
    result.innerHTML = this.responseText;
}

function loadData(){
    var queryValue = document.getElementById("query").value;
    if(queryValue.length > 0) {
        var xhr = new XMLHttpRequest();
        xhr.addEventListener("load", display);
        xhr.open("GET","query?name=" + queryValue);
        xhr.send();
    } else {
        document.getElementById("result_area").innerHTML = "";
    }
}

function checkIfLoadedExternally() {
    try {
        return window.self !== window.top;
    } catch (e) {
        return true;
    }
}

function swapTextInputType() {
    if(checkIfLoadedExternally()) {
        document.getElementById("query").type = "password";
    }
}

// On initial load
loadData();
swapTextInputType();
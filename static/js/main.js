window.onload = function replace_new_line(){
    var answer = document.getElementById('answer').textContent;
    document.getElementById('answer').innerHTML = answer.split("|").join("<br>");
}

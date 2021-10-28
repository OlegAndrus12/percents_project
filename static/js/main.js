function replace_new_line(){
    var body = document.getElementById('body').textContent;
    var answer = document.getElementById('answer').textContent;
    document.getElementById('body').innerHTML = body.split("|").join("<br>");
    document.getElementById('answer').innerHTML = answer.split("|").join("<br>");
}

replace_new_line();
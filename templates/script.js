function submit()
{
    var xhr = new XMLHttpRequest();
    xhr.open("POST", yourUrl, true);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.send(JSON.stringify(
        {
            "name": document.getElementById("name_input").value,
            "reason": document.getElementById("reason_input").value,
            "details": document.getElementById("details_input").value,
            "password": document.getElementById("password_input").value,
        }
    ));
}
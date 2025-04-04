function verify() {
    fetch('/verify')
        .then(response => response.json())
        .then(data => {
            document.getElementById('result').innerText = data.status;
        })
        .catch(err => {
            document.getElementById('result').innerText = "Error: " + err;
        });
}

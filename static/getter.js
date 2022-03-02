let i = 1;

function getInfo() {
    let data = fetch("/api")
        .then(resp => resp.json())
        .then(d => writeInfo(d));
}

function writeInfo(data) {
    console.log(data)
    let target = document.querySelector("#number")
    target.innerText = data.temp;
}

let update = true;

function myLoop() {
    setTimeout(function() {
        getInfo();
        i++;
        if (update) {
            myLoop();
        }
    }, 500)
}

myLoop(); 
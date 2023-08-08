
let myNumber = window.prompt('type your number:')
let secnumber = window.prompt('secand number')
myNumber = Number(myNumber)
secnumber = Number(secnumber)

document.getElementById('su').onclick = function(){
    let z = myNumber+ secnumber;

    document.getElementById('su').innerHTML = z;

}

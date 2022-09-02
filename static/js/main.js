
(function(proxied) {
    window.alert = function() {
      // do something here
      document.getElementById("flags").textContent = "{{flags}}";
      return proxied.apply(this, arguments);
    };
  })(window.alert);

  let dice;
let count=5;
let negcount=6;
function randnum(){
    let randomnum= getrandnum()
    dice= randomnum
}
randnum();
document.querySelectorAll('img')[0].setAttribute('src','assets/num.png')

function getrandnum(){
    return Math.floor(Math.random()*6) + 1
}
function result() {
    var numberValue = document.getElementById("txtInput").value;
    if(isNaN(numberValue) || numberValue.replaceAll(' ', '').length == 0 || numberValue<=0|| numberValue>=7){
        alert("Please Enter Number")
    }
    else if (!(dice==numberValue)){
        console.log("oops wrong" + numberValue + "right was" + dice);
        const diceimg = 'assets/dice' + dice + '.png';
        document.querySelectorAll('p')[0].innerHTML = 'Incorrect Guess'
        document.querySelectorAll('img')[0].setAttribute('src',diceimg)
        document.querySelectorAll('p')[1].innerHTML = 'Number was '+ dice
        randnum()
        negcount=negcount-1
        if (negcount==0){
            alert("Oppps You were not able to solve the challenge")
            negcount =6;
            count=5;
        }
    }
    else{
        const diceimg = 'assets/dice' + numberValue + '.png';
        document.querySelectorAll('img')[0].setAttribute('src',diceimg)
        document.querySelectorAll('p')[0].innerHTML = 'Wooohoo Correct Guess'
        document.querySelectorAll('p')[1].innerHTML = 'Number was '+ dice
        console.log("Woohoo"+dice+"ss"+numberValue);
        count=count-1;
        randnum();
        if (count>=4){
            alert("It was just Luck")
        }
        else if (count>=1){
            alert("Woow your to close to bet this Challenge")
        }
        else{
            alert("Congratulation, you done it")
        }
    }
      
 }
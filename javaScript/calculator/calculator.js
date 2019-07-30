let myForm = document.getElementById('myForm')
let myButton = document.getElementById('myButton')
let myDiv = document.getElementById('myDiv')
let numCount = 0
let firstNum = 0
let secondNum = 0
let sum = 0
let prevClickedButton = ''

function displayClickedButton(clicked_button) {
  if ( clicked_button != "+" && clicked_button != "=" ) {
    displayDigits(prevClickedButton, clicked_button)
  }
  else {
    if ( clicked_button == "+" ) {
      if (numCount == 0) {
        firstNum = parseInt(myDiv.innerHTML)
        numCount++
      } else {
        calculateSum()
      }

    } else {
      calculateSum()
    }
  }
  prevClickedButton = clicked_button
}

function calculateSum() {
  firstNum = firstNum + parseInt(myDiv.innerHTML)
  sum = firstNum
  myDiv.innerHTML = ''
  myDiv.innerHTML += sum
}

function displayDigits(prevClickedButton, clicked_button) {
  if (prevClickedButton == "+" || prevClickedButton == "=") {
    myDiv.innerHTML = ''
  }
  myDiv.innerHTML += clicked_button
}

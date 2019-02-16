"use strict";


onload();


function onload() {
    $("#calendar").fullCalendar();

    let radioButtons = document.querySelectorAll("input[type='radio']");

    for (let radioButton of radioButtons) {
        radioButton.addEventListener("click", radioButtonListener);
    }
}


function radioButtonListener() {
    displayCalendar(this.value);
}


function displayCalendar(provider) {
}

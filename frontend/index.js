"use strict";


onload();


function onload() {
    $("#calendar").fullCalendar();

    let radioButtons = document.querySelectorAll("input[type='radio']");

    for (let radioButton of radioButtons) {
        radioButton.addEventListener("click", radioButtonListener);
    }

    displayCalendar("bcbs");
}


function radioButtonListener() {
    displayCalendar(this.value);
}


function displayCalendar(provider) {
    fetchEvents(provider, (eventsJSON) => {
        console.log(eventsJSON);
    });
}

function fetchEvents(provider, callback) {
    fetch("http://localhost:5000/api/events", {method: "get"}).then(response => {
        response.json().then(callback);
    });
}

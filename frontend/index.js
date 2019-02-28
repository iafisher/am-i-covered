"use strict";


onload();


function onload() {
    $("#calendar").fullCalendar();

    let radioButtons = document.querySelectorAll("input[type='radio']");

    for (let radioButton of radioButtons) {
        radioButton.addEventListener("click", radioButtonListener);
    }

    // TODO: Need to actually find the radio button that is selected.
    displayCalendar("bcbs");
}


function radioButtonListener() {
    displayCalendar(this.value);
}


function displayCalendar(provider) {
    fetchEvents(provider, (eventsJSON) => {
        $("#calendar").fullCalendar("removeEvents");
        $("#calendar").fullCalendar("addEventSource", {events: eventsJSON});
    });
}

function fetchEvents(provider, callback) {
    let opts = {method: "get"}
    fetch("http://localhost:5000/api/events/" + provider, opts).then(response => {
        response.json().then(callback);
    });
}

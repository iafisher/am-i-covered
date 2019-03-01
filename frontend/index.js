"use strict";


onload();


function onload() {
    // Initalize the JS calendar app.
    $("#calendar").fullCalendar();

    // Attach the event listener to every radio button.
    let radioButtons = document.querySelectorAll("input[type='radio']");
    for (let radioButton of radioButtons) {
        radioButton.addEventListener("click", radioButtonListener);
    }

    // Display the events for the initially selected provider.
    let selectedProvider = document.querySelector('input[name="provider"]:checked').value;
    displayCalendar(selectedProvider);
}


// Callback that is invoked whenever a radio button is selected.
function radioButtonListener() {
    displayCalendar(this.value);
}


// Display the events on the calendar that match the given insurance provider.
function displayCalendar(provider) {
    fetchEvents(provider, (eventsJSON) => {
        $("#calendar").fullCalendar("removeEvents");
        $("#calendar").fullCalendar("addEventSource", {events: eventsJSON});
    });
}


// Fetch the events that match the given provider from the back-end.
function fetchEvents(provider, callback) {
    let opts = {method: "get"}
    fetch("http://localhost:5000/api/events/" + provider, opts).then(response => {
        response.json().then(callback);
    });
}

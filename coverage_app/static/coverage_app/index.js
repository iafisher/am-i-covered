"use strict";


const BASE_URL = "/demos/am-i-covered/";


onload();


function onload() {
    // Initalize the JS calendar app.
    let calendarElem = $("#calendar");
    let calendar = new FullCalendar.Calendar(calendarElem, {
        allDaySlot: false,
        defaultView: "agendaWeek",
        eventClick: clickHandler,
        height: "auto",
        minTime: "08:00:00",
        maxTime: "18:00:00",
        nowIndicator: true,
        weekends: false,
    });
    calendar.render();

    // Attach the event listener to every radio button.
    let radioButtons = document.querySelectorAll("input[type='radio']");
    for (let radioButton of radioButtons) {
        radioButton.addEventListener("click", (event) => {
            displayCalendar(calendar, event.target.value);
        });
    }

    // Display the events for the initially selected provider.
    let selectedProvider = document.querySelector('input[name="provider"]:checked').value;
    displayCalendar(calendar, selectedProvider);
}


// Callback that is invoked whenever a calendar event is clicked.
function clickHandler(event, jsEvent, view) {
    const nurse = encodeURI(event.title);
    const time = encodeURI(event.start.format());
    window.open(BASE_URL + "appointment?nurse=" + nurse + "&start=" + time, "_blank");
}


// Display the events on the calendar that match the given insurance provider.
function displayCalendar(calendar, provider) {
    fetchEvents(provider, (eventsJSON) => {
        calendar.removeEventSources();
        calendar.addEventSource(eventsJSON);
        calendar.render();
    });
}


// Fetch the events that match the given provider from the back-end.
function fetchEvents(provider, callback) {
    let opts = {method: "get"}
    fetch(BASE_URL + "api/events/" + provider, opts).then(response => {
        response.json().then(callback);
    });
}

"use strict";


const BASE_URL = "/demos/am-i-covered/";


onload();


function onload() {
    // Initalize the JS calendar app.
    let calendarElem = $("#calendar");
    let options = {
        allDaySlot: false,
        eventClick: clickHandler,
        height: "auto",
        minTime: "08:00:00",
        maxTime: "18:00:00",
        nowIndicator: true,
        views: {
            agendaThreeDay: {
                type: "agenda",
                duration: { days: 3 },
                buttonText: "3 day",
            },
        },
        weekends: false,
    };
    if (!smallWindow()) {
        options["defaultView"] = "agendaWeek";
    } else {
        // Display a three-day calendar on smaller devices.
        options["defaultView"] = "agendaThreeDay";
        options["scrollTime"] = "12:00:00";
    }
    let calendar = new FullCalendar.Calendar(calendarElem, options);
    calendar.render();

    window.addEventListener("resize", function (event) {
        if (smallWindow() && calendar.getView().name === "agendaWeek") {
            calendar.changeView("agendaThreeDay");
        } else if (!smallWindow() && calendar.getView().name !== "agendaWeek") {
            calendar.changeView("agendaWeek");
        }
    });

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


function smallWindow() {
    return window.innerWidth <= 600;
}


// Fetch the events that match the given provider from the back-end.
function fetchEvents(provider, callback) {
    let opts = {method: "get"}
    fetch(BASE_URL + "api/events/" + provider, opts).then(response => {
        response.json().then(callback);
    });
}

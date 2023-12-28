/*document.addEventListener('DOMContentLoaded', function() {
    var calendarEl = document.getElementById('calendar');
    var calendar = new FullCalendar.Calendar(calendarEl, {
        initialView: 'dayGridMonth'
    });
    calendar.render();
}); */

document.addEventListener('DOMContentLoaded', function() {
    $(document).ready(function () {
        // Initialize FullCalendar
        $('#calendar').fullCalendar({
            header: {
                left: 'prev,next today',
                center: 'title',
                right: ''
            },
            defaultView: 'agendaWeek',
            events: '/get_events',  // URL to fetch events
            height: 300,
        });
        $('.fc-next-button').html('<i class="material-icons">navigate_next</i>');
        $('.fc-prev-button').html('<i class="material-icons">navigate_before</i>');
    });
});
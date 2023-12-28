/*document.addEventListener('DOMContentLoaded', function() {
    var shifts = {{ shifts | tojson|safe }};

    $('#calendar').fullCalendar({
        defaultView: 'month',
        events: shifts.map(function(shift) {
            return {
                title: shift.location,
                start: shift.date + 'T' + shift.start_time,
                end: shift.date + 'T' + shift.end_time,
            };
        })
    });
});*/

document.getElementById("signup-link").addEventListener("click", changeSL);
document.getElementById("login-link").addEventListener("click", changeSLA);
document.getElementById("login-link1").addEventListener("click", changeSLA);
document.getElementById("login-link2").addEventListener("click", changeSLA);
document.getElementById("signup-link1").addEventListener("click", changeSL);
document.getElementById("signup-continue-button").addEventListener("click", part2);

function changeSL() {
    document.getElementById("signup").style.display = "block";
    document.getElementById("login").style.display = "none";
    document.getElementById("part1").style.display = "block";
    document.getElementById("part2").style.display = "none";
}

function changeSLA() {
    document.getElementById("signup").style.display = "none";
    document.getElementById("login").style.display = "block";
}

function part2() {
    document.getElementById("part1").style.display = "none";
    document.getElementById("part2").style.display = "block";
}


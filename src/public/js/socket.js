var socket = new WebSocket("ws://" + location.host + "/scoresocket");

socket.onmessage = function(event) {
    var teams = $.parseJSON( event.data );
    if(teams["flag"])
    {
        alert("Congrats! Your flag is: " + teams["flag"]);
        return;
    }

    for (team in teams) {

        if ($('#scoreboard tbody #' + team).length) {
            $('#scoreboard tbody #' + team + ' #team-score').text(teams[team]);
        } else {
            $('#scoreboard tbody').append('<tr id="' + team + '"><td id="team-name">' + team + '</td><td id="team-score">' + teams[team] + '</td></tr>');
        }
    }
}

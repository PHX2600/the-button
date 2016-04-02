var socket = new WebSocket("ws://" + location.host + "/scoresocket");
socket.onmessage = function(event)
{
    var msg = $.parseJSON( event.data );
    //var msg = JSON.parse(event.data);
    //alert(JSON.stringify(msg));

    //Get rid of the current scoreboard
    scoreboard = document.getElementById("scoreboard")
    // while( scoreboard.firstChild )
    // {
    //     scoreboard.removeChild( scoreboard.firstChild );
    // }

    for (var i in scoreboard.length) {
        scoreboard.deleteRow(i);
    }


    var tr;
    for (var key in msg) {
        var newRow = scoreboard.insertRow(0);
        var newCell1 = newRow.insertCell(0);
        var newText1  = document.createTextNode(key);
        newCell1.appendChild(newText1);
        var newCell2 = newRow.insertCell(0);
        var newText2  = document.createTextNode(msg[key]);
        newCell2.appendChild(newText2);

        // var cell1 = row.insertCell(0);
        // var cell2 = row.insertCell(1);
        // cell1.innerHTML = key;
        // cell2.innerHTML = msg[key];


        // tr = $('<tr>');
        // tr.append("<td>" + key + "</td>");
        // tr.append("<td>" + msg[key] + "</td>");
        // tr.append("</tr>")
        // $('scoreboard').append(tr);
    }
}

$(document).ready(function() {
    $("#button").click(function(){
        var team_name = document.getElementById("team").value;
        $.ajax({
            url: "/button",
            type: "POST",
            data: {team: team_name},
            statusCode: {
                200: function() {
                    ;
                },
                403: function() {
                    ;
                },
            }
        })
    });
});

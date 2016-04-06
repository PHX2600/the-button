$(document).ready(function() {


    $("#loginbutton").click(function(event){

        event.preventDefault();

        $.ajax({
            url: "/login",
            type: "POST",
            data: $("#loginform").serialize(),
            statusCode: {
                200: function() {
                    window.location.replace("button");
                },
                403: function() {
                    $("#failedlogin_message").hide();
                    $("#failedlogin_message").show(500);
                }
            }
        });

    });

    $("#the-button-form").on('click', '#button', function(event) {

        event.preventDefault();

        var team_name = document.getElementById("team").value;

        jQuery.post({
            url: "/button",
            data: {team: team_name}
        });

    });

    var now = new Date();
    var mins = now.getMinutes();
    var secs = now.getSeconds();
    var time_left = ((60 - mins - 1) * 60) + (60 - secs - 1);

    // Instantiate a coutdown FlipClock
    var clock = $('.clock').FlipClock(time_left, {
        clockFace: 'MinuteCounter',
        countdown: true
    });

});

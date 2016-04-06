$(document).ready(function() {

    $("#loginbutton").click(function(event){

        event.preventDefault();

        jQuery.post({
            url: "/login",
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

        var team_name = $("#team").value;
        var captcha_solve = $("#captcha-input").value;
        var captcha_id = $("#captcha_id").value;

        jQuery.post({
            url: "/button",
            data: {team: team_name, captcha: captcha_solve, captcha_id: captcha_id}
        });

        jQuery.get("/captcha", function(data){
          var images = $.parseJSON( data );
          $('#captcha').empty()
          for (image in images) {
            if(image == 1337){
                $('#captcha').append("<input type='text' name='captcha_id' value='" + images[image] + "' id='captcha_id' style='display: none'>");
            }
            else {
                $('#captcha').append('<img src="images/' + images[image] + '" />');
            }
          }
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

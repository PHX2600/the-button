$(document).ready(function() {

    jQuery.get("/captcha", function(data){
      var images = $.parseJSON( data );
      $('#captcha').empty()
      for (image in images) {
          if(image == 1337){
              $('#captcha').append("<input type='text' name='captcha_id' value='" + images[image] + "' id='captcha_id' style='display: none'>");
          } else {
              $('#captcha').append('<img src="images/' + images[image] + '" />')
          }
      }
    });

    $("#the-button-form").on('click', '#button', function(event) {

        event.preventDefault();

        var team_name = document.getElementById("team").value;
        var captcha_solve = document.getElementById("captcha-input").value;
        var captcha_id = document.getElementById("captcha_id").value;

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

});

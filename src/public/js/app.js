$(document).ready(function() {

    jQuery.get("/captcha", function(data){
      var images = $.parseJSON( data );
      $('#captcha').empty()
      for (image in images) {
        $('#captcha').append('<img src="images/' + images[image] + '" />')
      }
    });

    $("#the-button-form").on('click', '#button', function(event) {

        event.preventDefault();

        var team_name = document.getElementById("team").value;
        var captcha_solve = document.getElementById("captcha-input").value;

        jQuery.post({
            url: "/button",
            data: {team: team_name, captcha: captcha_solve}
        });

        jQuery.get("/captcha", function(data){
          var images = $.parseJSON( data );
          $('#captcha').empty()
          for (image in images) {
            $('#captcha').append('<img src="images/' + images[image] + '" />')
          }
        });

    });

});

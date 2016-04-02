$(document).ready(function() {

    $("#the-button-form").on('click', '#button', function(event) {

        event.preventDefault();

        var team_name = document.getElementById("team").value;

        jQuery.post({
            url: "/button",
            data: {team: team_name}
        });

    });

});

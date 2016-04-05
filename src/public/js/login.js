$(document).ready(function() {
    $("#loginbutton").click(function(){
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
                },
            }
        })
    });
});

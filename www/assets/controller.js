$(document).ready(function () {
    //Display Speak Message
    eel.expose(displayMessage)
    function displayMessage(message){
        $(".siri-message li:first").text(message);
        $(".siri-message").textillate('start');
    }

    eel.expose(show)
    function show(){
        $('#Oval').attr("hidden",false);
        $('#SiriWave').attr("hidden",true);
    }
});
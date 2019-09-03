$(document).ready(function () {


    // Hides the skill level checkboxes upon load.


    $(function () {
        $(".skill-options").hide();
    });

    // Function that toggles the next set of skill level checkboxes 
    // after a skill box has been selected. Only one skill options list
    // can be open at any given time

    $(function () {
        $(".skill-field").on("click", function () {
            $(".skill-options").fadeOut();
            let clicked = $(this).next(".skill-options")
            $(clicked).slideToggle("slow");

            return false;
        });

    });



});
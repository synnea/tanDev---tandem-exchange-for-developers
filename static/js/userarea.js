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
            var clicked = $(this).next(".skill-options");
            $(clicked).slideToggle("slow");

            return false;
        });

    });


    // change the display classes of the unpublish button in the user area.
    // This button appears in two different locations depending on screen width.

    $(function () {
        if ($(window).width() < 1000) {
            $("#desktop-unpublish").addClass("d-none");
            $("#mobile-unpublish").removeClass("d-none");
        } else {

            $("#desktop-unpublish").removeClass("d-none");
            $("#mobile-unpublish").addClass("d-none");

        }
    });

    // Call the same functions upon window resize.
    $(function () {
        $(window).on('resize', function () {

            if ($(window).width() < 1000) {
                $("#desktop-unpublish").addClass("d-none");
                $("#mobile-unpublish").removeClass("d-none");
            } else {

                $("#desktop-unpublish").removeClass("d-none");
                $("#mobile-unpublish").addClass("d-none");

            }
        });
    });

});